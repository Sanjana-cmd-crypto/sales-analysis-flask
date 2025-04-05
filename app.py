from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "API is working fine ✅"})

@app.route('/sales-prediction')
def sales_prediction():
    data = {
        "total_sales": 50000,
        "predicted_sales": 55000,
        "accuracy": 0.89
    }
    return jsonify(data)

@app.route('/payment-analysis')
def payment_analysis():
    data = [
        {"method": "Credit Card", "sales": 50000, "transactions": 200},
        {"method": "PayPal", "sales": 30000, "transactions": 150},
        {"method": "Cash", "sales": 20000, "transactions": 100}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
