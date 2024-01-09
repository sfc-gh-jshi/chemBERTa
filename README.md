# Finetuning LLMs in Snowpark Container Serices
Fine tune a [chemBERTa](https://arxiv.org/abs/2010.09885) model for drug discovery in Snowpark Container Services

![molecue!](/img/Molecule.png)

* The LLM we will fine tune is chemBERTa.
* The dataset used for finetuning is [ClinTox](https://moleculenet.org/datasets-1): Qualitative data of drugs approved by the FDA and those that have failed clinical trials for toxicity reasons. 
* chemBERTa allows finetuning using all publicly available datasets from [MoleculeNet](https://moleculenet.org/datasets-1), predicting on a wide range of tasks from classification, regression to generate 3D coordinates of molecules.

## Prediction Example in Streamlit
![Predict!](/img/Example_predictions.png "Predict")

* The fine tuned model is saved in a Snowflake internal stage.
* A Streamlit is running in Snowpark Container Services (SPCS) to load the model, allowing users to make predictions.
* For inference, input data is a SMILES string. Predictions include the predicted label (0 indicates the molecule is not toxic, 1 indicates toxic), and upper bound, lower bound of the predictions.

## Architecture
![Architecture!](/img/Architecture.png "Architecture")

