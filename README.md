# Army_Officers_Select_Prediction_PastAPI_ITBIN-2110-0113

To write an effective Medium article on “How to Deploy a Army-Officers-Select-Prediction-FastAPI Machine Learning Application in Heroku Web Services,” you should follow a structured approach. Here’s a suggested outline with instructions for each section:

 Introduction
Start by introducing the topic. Explain what the readers will learn from this article.
Mention that you will cover everything from training the machine learning model to deploying it using FastAPI and Heroku.
Provide a brief overview of the tools and technologies used, such as FastAPI, Heroku, and the DecisionTreeClassifier from scikit-learn.

 Training the Machine Learning Model
Explain the process of training the model using the provided Python code.
Include a brief description of the dataset (army.csv) used and its features. Mention how the target variable (output) is defined.
Explain each step of the code:
Loading the data using pandas.
Separating the input features (X) and output labels (y).
Initializing and training the DecisionTreeClassifier model.
Making predictions using the trained model.
Saving the trained model using “army-recommender.joblib”

Code Snippet:
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv('/content/army.csv')
data.head()

X = data.drop(columns=['output']).values # Input Data
y = data['output'] # Output Data

model = DecisionTreeClassifier()

model.fit(X, y)

predictions = model.predict([ [15,1,1,1] ])
predictions[0]

import joblib

joblib.dump(model, 'army-recommender.joblib')

odel = joblib.load("army-recommender.joblib")

predictions = model.predict([ [36,1,1,1] ])
predictions[0]

Creating a FastAPI Application
Introduce FastAPI as a modern web framework for building APIs with Python file “army.py”.
Provide a step-by-step guide on how to create a basic FastAPI app that loads the trained model and creates an endpoint for predictions.
Code Snippet:
import uvicorn
from fastapi import FastAPI
import joblib
from armyUser import armyUser

app = FastAPI()
joblib_in = open("army-recommender.joblib","rb")
model=joblib.load(joblib_in)


@app.get('/')
def index():
    return {'message': 'army Recommender ML API'}

@app.post('/army/predict')
def predict_army_type(data:armyUser):
    data = data.dict()
    Age=data['Age']
    Gender=data['Gender']
    OL=data['OL']
    AL=data['AL']

    prediction = model.predict([[Age, Gender, OL, AL ]])
    
    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
 Preparing for Deployment on Heroku
Explain the steps to prepare your FastAPI app for deployment on Heroku.
Creating Required Files:
requirements.txt: List all necessary dependencies (fastapi, joblib, scikit-learn, etc.).
Procfile: Describe how to create a Procfile to specify the command to run the FastAPI app (e.g., web: uvicorn main:app --host 0.0.0.0 --port ${PORT}).
Example of requirements.txt:
annotated-types==0.7.0
anyio==4.4.0
click==8.1.7
colorama==0.4.6
exceptiongroup==1.2.2
fastapi==0.112.2
gunicorn==23.0.0
h11==0.14.0
idna==3.8
joblib==1.4.2
numpy==1.26.4
packaging==24.1
pydantic==2.8.2
pydantic_core==2.20.1
scikit-learn==1.3.2
scipy==1.13.1
sniffio==1.3.1
starlette==0.38.4
threadpoolctl==3.5.0
typing_extensions==4.12.2
uvicorn==0.30.6

 Deploying to Heroku
Create a Heroku Account and Install the Heroku CLI: Provide a link to Heroku’s website and instructions on installing the Heroku CLI.
Login to Heroku and Create a New App: Guide on how to login to Heroku using the CLI and create a new application.
Deploy the FastAPI Application:
Initialize a Git repository and add all files.
Commit the changes and push them to Heroku’s remote repository.

Command Snippets:
uvicorn army:app --reload
pip freeze > requirements.txt
git init
git add .
git commit -m "added gunicorn and Procfile for heroku"
heroku create
git push heroku master
Testing the Deployed Application
Explain how to test the deployed application on Heroku using tools like Postman or curl.
Provide an example request to test the /predict endpoint.


Conclusion

Summarize the steps covered in the article.
Encourage readers to try deploying their own FastAPI applications and share feedback.




