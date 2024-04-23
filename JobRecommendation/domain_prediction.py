import streamlit as st
import pickle
import re
import nltk
import streamlit as st

nltk.download('punkt')
nltk.download('stopwords')
category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }


def clean_resume(resume_text):
        clean_text = re.sub('http\S+\s*', ' ', resume_text)
        clean_text = re.sub('RT|cc', ' ', clean_text)
        clean_text = re.sub('#\S+', '', clean_text)
        clean_text = re.sub('@\S+', '  ', clean_text)
        clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
        clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
        clean_text = re.sub('\s+', ' ', clean_text)
        return clean_text

@st.cache_data
def predict_domain(resume_text):
    #loading models
    clf = pickle.load(open('clf2.pkl','rb'))
    tfidfd = pickle.load(open('tfidf2.pkl','rb'))
    cleaned_resume = clean_resume(resume_text)
    input_features = tfidfd.transform([cleaned_resume])
    prediction_id = clf.predict(input_features)[0]
    # st.write(prediction_id)
    category_name = category_mapping.get(prediction_id, "Unknown")
    return category_name
    