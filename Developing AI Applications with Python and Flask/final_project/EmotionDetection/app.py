import streamlit as st

from emotion_detection import emotion_detector

st.title("Emotion Detector")

st.divider()

# Execute function
text_to_analyse = st.text_input("Enter text")

result = emotion_detector(text_to_analyse)

print(result)