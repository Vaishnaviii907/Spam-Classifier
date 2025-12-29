# SMS Spam Detection System

🔗 Live Demo: https://spam-classifier-vaish.streamlit.app/

---

## Description
This project implements a machine learning system to classify SMS messages as **Spam** or **Ham** using Natural Language Processing techniques. The primary goal is to detect spam messages while avoiding incorrect classification of legitimate messages.

---

## Methodology
- Text preprocessing using NLTK (tokenization, stopword removal, stemming)
- Feature extraction using TF-IDF
- Classification using Multinomial Naive Bayes
- Model evaluation using an 80–20 train–test split

---

## Data Split
- **80% Training Data**
- **20% Testing Data**

This split provides sufficient data for learning while keeping unseen data for evaluation.

---

## Results
- Accuracy: ~97%
- Precision: 100%
- No legitimate messages were classified as spam on the test dataset

---

## Deployment
- Developed and tested locally using VS Code and a virtual environment
- User interface built using Streamlit
- Deployed online using Streamlit Community Cloud
- Trained model and vectorizer saved using Pickle

---

## Technologies Used
- Python
- Scikit-learn
- NLTK
- Streamlit
- Google Colab
- GitHub

---

## Project Structure
- Model training and experimentation were performed in a Google Colab notebook
- Deployment logic was implemented separately in a Streamlit application (`app.py`)

---

