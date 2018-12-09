from flask import Flask, request, jsonify
from sklearn.externals import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
	 #receive the data
     json_ = request.json
     query_df = pd.DataFrame([json_])
     query = pd.DataFrame(np.zeros((1, 42)), columns=['ESC','IDADE','RENDA', 'RACACOR_1', 'RACACOR_2', 'RACACOR_3', 'RACACOR_4', 'RACACOR_5', 'RACACOR_6', 'REGIAO_1', 'REGIAO_2', 'REGIAO_3', 'REGIAO_4', 'REGIAO_5', 'SEXO_2', 'UF_11', 'UF_12', 'UF_13', 'UF_14', 'UF_15', 'UF_16', 'UF_17', 'UF_21', 'UF_22', 'UF_23', 'UF_24', 'UF_25', 'UF_26', 'UF_27', 'UF_28', 'UF_29', 'UF_31', 'UF_32', 'UF_33', 'UF_35', 'UF_41', 'UF_42', 'UF_43', 'UF_50', 'UF_51', 'UF_52', 'UF_53'])
     query.ESC = pd.get_dummies(query_df['ESC'])
     query.IDADE = pd.get_dummies(query_df['IDADE'])
     query.RENDA = pd.get_dummies(query_df['RENDA'])
     query.SEXO_2 = pd.get_dummies(query_df['SEXO_2'])
     query['RACACOR_'+query_df['RACACOR']] = 1
     query['REGIAO_'+query_df['REGIAO']] = 1
     query['UF_'+query_df['UF']] = 1
     

     #predict the probability of the woman be in a condition of violence according to the model
     prediction = clf.predict_proba(query)
     #return the probability
     return jsonify({'The probability of this woman be in a condition of violence ': prediction[0][0]})

if __name__ == '__main__':
     clf = joblib.load('model.pkl')
     app.run(port=8080)

