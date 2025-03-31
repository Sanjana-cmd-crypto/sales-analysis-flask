from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sales Prediction API
@app.route('/api/sales-prediction', methods=['GET'])
def sales_prediction():
    data = {
        "total_sales": 50000,
        "predicted_sales": 55000,
        "accuracy": 0.89
    }
    return jsonify(data)

# Payment Analysis API
@app.route('/api/payment-analysis', methods=['GET'])
def payment_analysis():
    data = [
        {"method": "Credit Card", "sales": 50000, "transactions": 200},
        {"method": "PayPal", "sales": 30000, "transactions": 150},
        {"method": "Cash", "sales": 20000, "transactions": 100}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

    from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Sales Analysis API is Running on Vercel!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

