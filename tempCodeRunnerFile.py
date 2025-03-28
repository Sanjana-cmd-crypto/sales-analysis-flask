from flask import Flask, jsonify
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

# Database connection
DATABASE_URI = "mysql+pymysql://root:132856@localhost/sales"
engine = create_engine(DATABASE_URI)

@app.route("/")
def home():
    return "Welcome to Sales Analysis API"

@app.route("/sales_data", methods=["GET"])
def get_sales_data():
    try:
        query = "SELECT * FROM order_detail"
        df = pd.read_sql(query, engine)
        return jsonify(df.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"message": f"Error fetching sales data: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)