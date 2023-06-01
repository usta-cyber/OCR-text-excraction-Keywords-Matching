from loadWordsFile import load_words_file_to_list
from LoadFolderDocuments import loadDocFolder
from SaveMatchedText import save_matched_words_to_excel



# List of words to match
word_file="C:\\Users\\Tajummal\\Documents\\word_file.txt"
# Directory containing the files to process
directory = "C:\\Users\\Tajummal\\Documents\\test_doc"
# Path to the output Excel file to save matched results
output_file_path = 'C:\\Users\\Tajummal\\Documents\\matced_word_results.xlsx'
word_list=load_words_file_to_list(word_file)
matched_words=loadDocFolder(directory,word_list)
save_matched_words_to_excel(matched_words, output_file_path)