import streamlit as st
from send_email import send_email
import pandas

df= pandas.read_csv("topics.csv")

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    topic_option = st.selectbox(
        "What topic do you want to discuss",
        df["topic"],
        placeholder="Select contact method...")



    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email} 
Topic: {topic_option}
{raw_message}
"""

    button = st.form_submit_button("Send email")
    if button:
        send_email (message)
        st.info("Your email was sent successfully")