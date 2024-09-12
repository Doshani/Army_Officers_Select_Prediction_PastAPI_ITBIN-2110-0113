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