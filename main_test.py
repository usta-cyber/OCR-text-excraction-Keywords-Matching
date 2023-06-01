
from File_text_extraction.loadWordsFile import load_words_file_to_list
from File_text_extraction.LoadFolderDocuments import loadDocFolder
from File_text_extraction.SaveMatchedText import save_matched_words_to_excel
from FileSeperator.file_separator import file_separate


allPaths=file_separate('C:\\Users\\Tajummal\\Documents\\TestDataAll')
# List of words to match
word_file="TestAndResults\\word_file.txt"
# Directory containing the files to process
doc_directory = allPaths[1]
image_directory=allPaths[0]
# Path to the output Excel file to save matched results
output_file_path = 'TestAndResults\\matced_word_results.xlsx'
word_list=load_words_file_to_list(word_file)
matched_words=loadDocFolder(doc_directory,word_list)
save_matched_words_to_excel(matched_words, output_file_path)