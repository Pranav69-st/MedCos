from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)
model = None

@app.before_first_request
def load_model():
    global model
    with open('docfee.pkl', 'rb') as f:
        model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    data = pd.DataFrame(data, index=[0])
    prediction = model.predict(data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
