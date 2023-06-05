
import streamlit as st
import io
from wordcloud import WordCloud
import PyPDF2
import textract
from docx import Document


# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in range(reader.numPages):
        text += reader.getPage(page).extractText()
    return text


# Function to extract text from TXT
def extract_text_from_txt(file):
    text = file.read()
    return text


# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = Document(file)
    paragraphs = doc.paragraphs
    text = " ".join([p.text for p in paragraphs])
    return text


# Function to generate word cloud
def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    return wordcloud


# Streamlit app
def main():
    st.title("Word Cloud Generator")
    st.write("Upload a PDF, TXT, or DOCX file to generate a word cloud.")

    # File upload
    file = st.file_uploader("Upload file", type=["pdf", "txt", "docx"])

    if file is not None:
        # File type handling
        if file.type == "application/pdf":
            text = extract_text_from_pdf(file)
        elif file.type == "text/plain":
            text = extract_text_from_txt(file)
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_docx(file)

        # Generate word cloud
        if text:
            wordcloud = generate_word_cloud(text)
            st.subheader("Word Cloud")
            st.image(wordcloud.to_image(), use_column_width=True)


if __name__ == "__main__":
    main()
