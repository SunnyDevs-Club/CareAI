from sklearn.preprocessing import LabelEncoder
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import joblib
import string


nltk.download('wordnet')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
# Create an instance of WordNetLemmatizer
wn = WordNetLemmatizer()
# label_encoder = LabelEncoder()

def clean_text(nlp):
    nlp = "".join([char.lower() for char in nlp if char not in string.punctuation ])
    token=re.split('\W+',nlp)
    stems=[wn.lemmatize(word) for word in token if word not in stop_words]
    return stems


count_vect = joblib.load('ai/count_vec.pkl')
rf_classifier = joblib.load('ai/symp.pkl')
label_encoder = joblib.load('ai/enum.pkl')


def predicting(input_word):
    clean_input=[" ".join(clean_text(input_word))]
    vect_input=count_vect.transform(clean_input)
    y_pred_encoded = rf_classifier.predict(vect_input)
    result=label_encoder.inverse_transform(y_pred_encoded)
    return result


doctor_specialization = {
    'Dermatologist': ['Psoriasis', 'Varicose Veins', 'Acne', 'Impetigo', 'Chicken Pox', 'Drug Reaction'],
    'Gastroenterologist': ['Peptic Ulcer Disease', 'Gastroesophageal Reflux Disease', 'Jaundice'],
    'Allergist': ['Allergy'],
    'Urologist': ['Urinary Tract Infection'],
    'Infectious Disease Specialist': ['Malaria', 'Dengue', 'Typhoid', 'Common Cold'],
    'Orthopedist': ['Cervical Spondylosis', 'Arthritis'],
    'Neurologist': ['Migraine'],
    'Cardiologist': ['Hypertension'],
    'Pulmonologist': ['Bronchial Asthma', 'Pneumonia'],
    'General Practitioner': ['Diabetes', 'Dimorphic Hemorrhoids']
}

def symptom_analysis(symptoms):
    disease = predicting(symptoms)
    if disease:
        disease = disease[0]
    else:
        return None

    # According to the disease, we should return the specialization
    for key, list_values in doctor_specialization.items():
        for value in list_values:
            if disease.lower() == value.lower():
                return disease, key

