from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from joblib import load

app = Flask(__name__,template_folder='./templates')
model = load('model.joblib')
scaler = load('scaler.joblib')
imputer = load('imputer.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    
    json_data = request.json
    df = pd.DataFrame(json_data)
    # Handle missing values using the loaded imputer
    df_scaled = scaler.transform(df)
    df_scaled_imputed = imputer.transform(df_scaled)
    #predictions
    predictions = model.predict_proba(df_scaled_imputed)[:, 1]
    predicted_value = predictions[0]
    if predicted_value >= 0.9:
        message = "The water scarcity and drought are approaching."
    elif predicted_value >= 0.7:
        message = "The water scarcity and drought are in the near future."
    elif predicted_value >= 0.5:
        message = "The availability of water resource is vulnerable."
    else:
        message = "The water resource is available, and water scarcity is unlikely."
    
    # Return the predicted value and corresponding message as JSON
    return jsonify(predicted_value=predicted_value, message=message)

if __name__ == '__main__':
    app.run(debug=True)
