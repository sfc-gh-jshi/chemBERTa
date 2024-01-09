# chemBERTa
Fine tune a [chemBERTa](https://arxiv.org/abs/2010.09885) model for drug discovery in Snowpark Container Services

![molecue!](/img/Molecule.png)

* The LLM we will be using for finetuning is chemBERTa.
* The dataset used for finetuning is [ClinTox](https://moleculenet.org/datasets-1): Qualitative data of drugs approved by the FDA and those that have failed clinical trials for toxicity reasons. 
* chemBERTa allows finetuning using all publicly available datasets from [MoleculeNet](https://moleculenet.org/datasets-1), predicting on a wide range of tasks from classification, regression to generate 3D coordinates of molecules.

## Prediction Example in Streamlit
![Predict!](/img/Example_predictions.png "Predict")

## Architecture
![Architecture!](/img/Architecture.png "Architecture")
