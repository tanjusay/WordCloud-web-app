import streamlit as st 
from PyPDF2 import PdfReader 
from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
from io import BytesIO 
  
  
def extract_important_words(pdf_file): 
    # Extract text from PDF 
    pdf_reader = PdfReader(pdf_file) 
    text = "" 
    for page in pdf_reader.pages: 
        text += page.extract_text() 
  
    # Perform text processing and extract important words 
    # Replace with your own logic for extracting important words 
  
    # Example: Extract words longer than 4 characters 
    important_words = [word for word in text.split() if len(word) > 4] 
  
    return important_words 
  
  
def generate_wordcloud(important_words): 
    # Generate word cloud from important words 
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(important_words)) 
  
    # Plot word cloud 
    plt.figure(figsize=(10, 5)) 
    plt.imshow(wordcloud, interpolation='bilinear') 
    plt.axis('off') 
  
    # Convert plot to image 
    image_stream = BytesIO() 
    plt.savefig(image_stream, format='png') 
    image_stream.seek(0) 
  
    return image_stream 
  
hide_menu = """
    <style>
    #MainMenu {visibility : hidden;}
    footer {visibility : hidden ; }
    </style>
    """
st.markdown(hide_menu, unsafe_allow_html = True)

# Main application 
st.title("PDF Word Cloud Generator") 
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf") 

  
if uploaded_file is not None: 
    important_words = extract_important_words(uploaded_file) 
  
    wordcloud_image = generate_wordcloud(important_words) 
  
    st.image(wordcloud_image, caption="Word Cloud", use_column_width=True)