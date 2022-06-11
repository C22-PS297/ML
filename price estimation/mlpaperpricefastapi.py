from fastapi import FastAPI 
import uvicorn
import tensorflow as tf
from tensorflow import keras

app = FastAPI(debug=True)

@app.get('/')
def home():
    return{'text': "Book Price Prediction"}

@app.get('/ predict')
def predict(Amount: float):
    model = tf.keras.models.load_model('D:\price estimation\estpricekiloswhitepaper.h5')
    makeprediction = model.predict([Amount])
    output = makeprediction[0]
    return{"Selling price of {} kg paper = {}".format(Amount, output)}

if __name__ == '__main__':
    uvicorn.run(app)