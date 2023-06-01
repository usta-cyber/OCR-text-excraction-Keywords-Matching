from PIL import Image, ImageDraw, ImageFont
import os

def convert_text_to_image(text, output_path, font_size=12, font_color=(0, 0, 0), background_color=(255, 255, 255),
                          font_path=None, image_format="PNG"):
    # Define font
    if font_path is None:
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, font_size)

    # Determine image size based on text length and font size
    text_width, text_height = font.getsize(text)
    image_width = text_width + 20  # Add some padding
    image_height = text_height + 20  # Add some padding

    # Create image with specified background color
    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    # Draw text on the image
    draw.text((10, 10), text, font=font, fill=font_color)

    # Save the image
    image.save(output_path, format=image_format)

def convert_text_files_to_images(directory, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # Read the text from the file
            with open(file_path, "r") as file:
                text = file.read()

            # Determine the output file path
            output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.png")

            # Convert text to image
            convert_text_to_image(text, output_path)

# Directory containing the text files to convert
input_directory = "New DATA\\documents"

# Directory to save the converted images
output_directory = "output_images"

# Convert text files to images
convert_text_files_to_images(input_directory, output_directory)
