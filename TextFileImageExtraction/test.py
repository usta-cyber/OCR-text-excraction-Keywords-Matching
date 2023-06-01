import os
import PyPDF2
import zlib
from PIL import Image
import io

import os
from docx import Document

import os
from docx import Document

import docx2txt

def extract_images_from_docx(docx_file):
    doc = Document(docx_file)
    filename = os.path.splitext(os.path.basename(docx_file))[0]  # Extracting the file name without extension

    # Create a new folder with the same name as the file
    output_dir = os.path.join("New DATA/TextToImages/DOCTextImages", filename)
    os.makedirs(output_dir, exist_ok=True)

    image_index = 0

    # Iterate over relationships to extract images linked from external files
    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            image = rel.target_part.blob
            image_filename = f"image_{image_index}.jpg"
            image_path = os.path.join(output_dir, image_filename)
            with open(image_path, "wb") as f:
                f.write(image)
            image_index += 1

    # Iterate over paragraphs and their runs to extract inline images embedded in the document
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if run.inline_shapes:
                for inline_shape in run.inline_shapes:
                    if inline_shape.has_picture:
                        image = inline_shape.image
                        image_bytes = image.blob
                        image_filename = f"image_{image_index}.jpg"
                        image_path = os.path.join(output_dir, image_filename)
                        with open(image_path, "wb") as f:
                            f.write(image_bytes)
                        image_index += 1

    # Iterate over shapes to extract images in text boxes, headers, and footers
    for section in doc.sections:
        for header in section.header_parts:
            for shape in header.shapes:
                if shape.is_picture:
                    image = shape.image
                    image_bytes = image.blob
                    image_filename = f"image_{image_index}.jpg"
                    image_path = os.path.join(output_dir, image_filename)
                    with open(image_path, "wb") as f:
                        f.write(image_bytes)
                    image_index += 1

        for footer in section.footer_parts:
            for shape in footer.shapes:
                if shape.is_picture:
                    image = shape.image
                    image_bytes = image.blob
                    image_filename = f"image_{image_index}.jpg"
                    image_path = os.path.join(output_dir, image_filename)
                    with open(image_path, "wb") as f:
                        f.write(image_bytes)
                    image_index += 1

    # Process and manipulate the extracted images as needed
    for image_filename in os.listdir(output_dir):
        image_path = os.path.join(output_dir, image_filename)
        # Example: Open the image using Pillow and perform some operations
        image = Image.open(image_path)
        # Perform additional processing on the image if desired


def sanitize_filename(filename):
    # Replace characters not allowed in file names
    invalid_chars = r'\/:*?"<>|'
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    return filename

def extract_images_from_pdf(pdf_file):
    filename=os.path.basename(pdf_file)
    output_dir = os.path.join("New DATA/TextToImages/DOCTextImages", filename)

    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    with open(pdf_file, "rb") as file:
        pdf = PyPDF2.PdfReader(file)
        
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            if "/XObject" in page["/Resources"]:
                x_object = page["/Resources"]["/XObject"].get_object()
                for obj in x_object:
                    if x_object[obj]["/Subtype"] == "/Image":
                        image = x_object[obj]

                        if "/Filter" in image:
                            filters = image["/Filter"]

                            if "/FlateDecode" in filters:
                                # Decompress the FlateDecode image data
                                image_data = zlib.decompress(image._data)
                            elif "/DCTDecode" in filters:
                                # Image is already in JPEG format, no decoding needed
                                image_data = image._data
                            else:
                                # Unsupported image encoding
                                print(f"Skipping image {obj}: Unsupported image encoding")
                                continue
                        else:
                            # No encoding specified, treat as FlateDecode
                            image_data = zlib.decompress(image._data)

                        # Create an image object from the image data
                        image_stream = io.BytesIO(image_data)
                        try:
                            image_obj = Image.open(image_stream)
                        except IOError:
                            print(f"Skipping image {obj}: Error in identifying image format")
                            continue

                        # Save the image as PNG
                        image_name = f"image_{page_num}_{sanitize_filename(obj)}.png"
                        image_path = os.path.join(output_dir, image_name)
                        image_obj.save(image_path, "PNG")

# Usage example
# extract_images_from_pdf("New DATA\\documents\\AI_Manual.pdf")
# Usage example
docx_file = "New DATA\\documents\\Material.docx"
extract_images_from_docx(docx_file)
