import streamlit as st
import pandas as pd
from simpletransformers.classification import ClassificationModel

# Set Streamlit app title
st.title("Molecule Toxicity Predictions")

# Set model path
path = '/model/chemBERTa'

# Load model from a stage
loaded_model = ClassificationModel('roberta', path, use_cuda = False)

# Predict based on the input
target_name= st.text_input('Enter a SMILES string:')
predict_toxicity = st.button('Predict Toxicity')
if predict_toxicity:
    predictions, raw_outputs = loaded_model.predict([str(target_name)])
    df_pred = pd.DataFrame({'predictions': predictions, 'raw_outputs_lowerbound': raw_outputs[0][0], 'raw_outputs_upperbound': raw_outputs[0][0]})
    st.dataframe(df_pred)
