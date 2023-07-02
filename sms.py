import streamlit as st
import pickle

# -*- coding: utf-8 -*-
"""
@author: Satyala Saikishore
"""
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://c1.wallpaperflare.com/preview/528/223/653/hacker-hacking-computer-security.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

def bg():
    html_temp = """
    <div style="background-color:#07b857;padding:3px">
    <h1 style="color:white;text-align:center;">SMS Spam or Ham ML App </h1>
    </div>
    <br></br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
bg()

def main():
    p = pickle.load(open('sms_spam_or_ham.pkl', 'rb'))
    text_box = st.text_area("Enter a text to check whether this is spam or ham:")
    if st.button("Check Spam/Ham"):
        if p.predict([text_box]) == 0:
            st.title("Congratulations this not a spam.")
            st.markdown("![Alt Text](https://media.giphy.com/media/XqDOVcnMTDdU89quVn/giphy.gif)")
        else:
            st.title("Oops! This is a Spam. Be alert.")
            st.markdown("![Alt Text](https://media.giphy.com/media/6OgMpKWyTpQXr66i08/giphy.gif)")
    if st.button("About"):
        st.text("Be Happy\nBe Safe")


if __name__ == '__main__':
    main()