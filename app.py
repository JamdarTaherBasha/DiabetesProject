from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and preprocessing tools
model = pickle.load(open('rf_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
imputer = pickle.load(open('imputer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction_text="", color="")

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    input_array = np.array(data).reshape(1, -1)
    input_array = imputer.transform(input_array)
    input_array = scaler.transform(input_array)
    prediction = model.predict(input_array)

    if prediction[0] == 1:
        result = "Has Diabetes"
        color = "red"
    else:
        result = "No Diabetes"
        color = "green"

    # Pass result and color to HTML
    return render_template('index.html', prediction_text=f"Prediction: {result}", color=color)

if __name__ == "__main__":
    app.run(debug=True)
