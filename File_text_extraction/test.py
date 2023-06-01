import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

def match_text_in_pdf(file_path, word_list):
    pdf_text = read_pdf(file_path)

    # Convert the PDF text to lowercase for case-insensitive matching
    pdf_text_lower = pdf_text.lower()

    matched_words = []
    for word in word_list:
        # Convert the word to lowercase for case-insensitive matching
        word_lower = word.lower()

        if word_lower in pdf_text_lower:
            matched_words.append(word)

    return matched_words


# Path to the PDF document
pdf_path = 'C:\\Users\\Tajummal\\Documents\\test_doc\\d.pdf'

# List of words to match
word_list = ['tools', 'extract', 'data','yyy']

# Match the words in the PDF
matched_words = match_text_in_pdf(pdf_path, word_list)

# Print the matched words
print("Matched Words:")
for word in matched_words:
    print(word)



