from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "API is working!"})

@app.route('/sales-prediction')
def sales_prediction():
    return jsonify({
        "total_sales": 50000,
        "predicted_sales": 55000,
        "accuracy": 0.89
    })

@app.route('/payment-analysis')
def payment_analysis():
    return jsonify([
        {"method": "Credit Card", "sales": 50000, "transactions": 200},
        {"method": "PayPal", "sales": 30000, "transactions": 150},
        {"method": "Cash", "sales": 20000, "transactions": 100}
    ])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)

