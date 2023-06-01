import os
from .fileTextMatching import match_text_in_word,match_text_in_pdf,match_text_in_csv,match_text_in_excel,match_text_in_json,match_text_in_xml

def loadDocFolder(directory,word_list):
    matched_words=[]
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith(".pdf"):
            matched_words.extend(match_text_in_pdf(filename,file_path, word_list))
        elif filename.endswith(".docx"):
            matched_words.extend(match_text_in_word(filename,file_path, word_list))
        elif filename.endswith(".xlsx"):
            matched_words.extend(match_text_in_excel(filename,file_path, word_list))
        elif filename.endswith(".csv"):
            matched_words.extend(match_text_in_csv(filename,file_path, word_list))
        elif filename.endswith(".json"):
            matched_words.extend(match_text_in_json(filename,file_path, word_list))
        elif filename.endswith(".xml"):
            matched_words.extend(match_text_in_xml(filename,file_path, word_list))
    return matched_words