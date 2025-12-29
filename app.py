import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# Load model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def transform_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [i for i in tokens if i.isalnum()]
    tokens = [i for i in tokens if i not in stopwords.words('english')]
    tokens = [ps.stem(i) for i in tokens]
    return " ".join(tokens)

st.title("📩 SMS Spam Detection")
st.write("Enter an SMS message to check if it is Spam or Ham.")

input_sms = st.text_area("Enter message")

if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("Please enter a message.")
    else:
        transformed = transform_text(input_sms)
        vector = tfidf.transform([transformed])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam (Ham)")
