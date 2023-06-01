import os
import shutil

# specify the path of the folder
# folder_path = 'C:/Users/This Pc/Downloads/Data_source'
output_folder_path = 'New DATA'
def file_separate(folder_path):
    # folder = 'C:/Users/This Pc/Downloads/Data_source'
    # print("Dataaaa:",folder_path)
    # print("Dataaaa:",folder)
    # if folder==folder_path:
    #     print("equal")
    # else:
    #     print("not equal",len(folder)," path=",len(folder_path))

    # create separate folders for images, documents and other files
    image_folder_path = os.path.join(output_folder_path, 'images')
    document_folder_path = os.path.join(output_folder_path, 'documents')
    other_folder_path = os.path.join(output_folder_path, 'other')
    os.makedirs(image_folder_path, exist_ok=True)
    os.makedirs(document_folder_path, exist_ok=True)
    os.makedirs(other_folder_path, exist_ok=True)

    # use os.walk() to get all the files and folders in the specified path
    for root, dirs, files in os.walk(folder_path):
        # loop through the list of files in the current directory
        for file in files:
            # construct the full path to the file
            file_path = os.path.join(root, file)

            # determine the file type by checking the file extension
            file_ext = os.path.splitext(file_path)[1].lower()

            # copy the file to the appropriate folder based on its type
            if file_ext in ('.jpg', '.jpeg', '.png', '.gif', '.bmp','.jfif','.webp'):
                destination = os.path.join(image_folder_path, file)
            elif file_ext in ('.doc', '.docx', '.pdf', '.txt', '.rtf','.txt','.csv','.json','.xml','.so','.xlsx'):
                destination = os.path.join(document_folder_path, file)
            else:
                destination = os.path.join(other_folder_path, file)

            # copy the file to the destination folder if it doesn't already exist there
            if not os.path.exists(destination):
                shutil.copy(file_path, destination)
    return image_folder_path,document_folder_path,other_folder_path