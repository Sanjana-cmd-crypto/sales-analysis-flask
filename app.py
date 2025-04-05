from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from waitress import serve   # Import waitress for production server

app = Flask(__name__)
CORS(app, origins="*")  # Allow requests from any origin

@app.route('/sales-prediction', methods=['GET'])
def sales_prediction():
    data = {
        "total_sales": 50000,
        "predicted_sales": 55000,
        "accuracy": 0.89
    }
    return jsonify(data)

@app.route('/payment-analysis', methods=['GET'])
def payment_analysis():
    data = [
        {"method": "Credit Card", "sales": 50000, "transactions": 200},
        {"method": "PayPal", "sales": 30000, "transactions": 150},
        {"method": "Cash", "sales": 20000, "transactions": 100}
    ]
    return jsonify(data)

# ✅ Correct method to run Flask on Vercel
def handler(event, context):
    return app(event, context)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
