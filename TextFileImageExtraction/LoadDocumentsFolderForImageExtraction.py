import os
from extractImagesFromText import *

def loadingDocPathsAndExtractImg(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".pdf"):
               ImgFolderPath=extract_images_from_pdf(file_path)
               print("OUTPUT DIR:",ImgFolderPath)
               loadFileImagesToCSV(ImgFolderPath)
            elif file.endswith(".docx"):
                ImgFolderPath=extract_images_from_docx(file_path)
                print("OUTPUT DIR:",ImgFolderPath)
                loadFileImagesToCSV(ImgFolderPath)

            elif file.endswith(".pptx"):
                ImgFolderPath=extract_images_from_ppt(file_path)
                print("OUTPUT DIR:",ImgFolderPath)
                loadFileImagesToCSV(ImgFolderPath)

            else:
                print("Unexpected Files Format")

