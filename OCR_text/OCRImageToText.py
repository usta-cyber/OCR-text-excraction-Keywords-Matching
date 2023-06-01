import os
import pytesseract
from PIL import Image

def perform_ocr(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def match_text_in_document(fileName,document_path, word_list):
    text = perform_ocr(document_path)
    print("===============================================")
    print("File Name=",fileName,"  File Path=",document_path)
    print("_______________________________________________")
    print(text)
    print("===============================================")
    # Match the extracted text against the word list
    for word in word_list:
        if word.lower() in text.lower():
            print(f"Match found in document: {word}")

# List of words to match
word_list = ["apple", "banana", "orange"]

# Directory containing the files to process
directory = "output_images"

# Iterate through files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        match_text_in_document(filename,file_path, word_list)
