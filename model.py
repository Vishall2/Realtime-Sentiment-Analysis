import streamlit as st
import nltk
import base64
from load_css import local_css
from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.write("# Real Time Sentiment Analysis")


local_css("style.css")
st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        padding-top: 0rem;
    }}
   
</style>
""",
        unsafe_allow_html=True,
    )

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    width: auto;
    height: auto;
    }
  }
    
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
                                      
set_background('Analysis-4.jpg')


user_input = st.text_input("Please rate our services : ")
nltk.download("vader_lexicon")
s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

if score == 0:
    st.write(" ")
elif score["neg"] != 0:
    st.write("# Negative")
elif score["pos"] != 0:
    st.write("# Positive")
    





