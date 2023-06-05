import streamlit as st
from wordcloud import WordCloud
from io import BytesIO
import PyPDF2
from docx import Document


def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page).extractText()
    return text



def generate_wordcloud(text):
    wordcloud = WordCloud().generate(text)
    return wordcloud


def main():
    st.title("Word Cloud Generator")
    st.write("Upload a PDF, or TXT file to generate a word cloud.")

    file = st.file_uploader("Upload File", type=["pdf", "txt"])

    if file is not None:
        file_type = file.name.split(".")[-1]

        if file_type == "pdf":
            text = extract_text_from_pdf(file)
        elif file_type == "txt":
            text = file.read().decode("utf-8")

        wordcloud = generate_wordcloud(text)

        st.subheader("Word Cloud")
        st.image(wordcloud.to_image())


if __name__ == "__main__":
    main()
