def load_words_file_to_list(word_list_file_path):
    with open(word_list_file_path, 'r') as word_list_file:
        word_list = [word.strip() for word in word_list_file.readlines() if word.strip()]
    return word_list