import pandas as pd

def save_matched_words_to_excel(matched_words, output_file_path):
    df = pd.DataFrame(matched_words, columns=['Matched Word', 'File Name', 'File Path'])
    df.to_excel(output_file_path, index=False)
