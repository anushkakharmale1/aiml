import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("Spam Detection App")

input_sms = st.text_area("Enter message")

if st.button("Predict"):

    transformed_sms = vectorizer.transform([input_sms])

    prediction = model.predict(transformed_sms)

    if prediction[0] == 1:
        st.header("Spam")
    else:
        st.header(" Not Spam")