from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text

app = Flask(__name__)

# 🔹 Update your MySQL database credentials
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:132856@localhost/sales"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
    return jsonify({"message": "Flask API is running!"})

@app.route("/test_db")
def test_db():
    try:
        engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
        return jsonify({"message": "Database connected successfully!"})
    except Exception as e:
        return jsonify({"message": f"Error connecting to database: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Your database connection (Make sure this is correct)
DATABASE_URI = "mysql+pymysql://root:132856@localhost:3306/sales"
engine = create_engine(DATABASE_URI)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Sales API!"})

# ✅ Add this new route to fetch sales data
@app.route("/sales_data", methods=["GET"])
def get_sales_data():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM order_detail"))
            sales = [dict(row) for row in result.mappings()]
        return jsonify({"sales_data": sales})
    except Exception as e:
        return jsonify({"message": f"Error fetching sales data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text

app = Flask(__name__)

# 🔹 Update your MySQL database credentials
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:132856@localhost/sales"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
    return jsonify({"message": "Flask API is running!"})

@app.route("/test_db")
def test_db():
    try:
        engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
        return jsonify({"message": "Database connected successfully!"})
    except Exception as e:
        return jsonify({"message": f"Error connecting to database: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

# ✅ Correct Database URI (Replace with your actual database credentials)
DATABASE_URI = "mysql+pymysql://your_username:your_password@localhost:3306/your_database"
engine = create_engine(DATABASE_URI)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Sales API!"})

# ✅ FIXED: Sales Data Route
@app.route("/sales_data", methods=["GET"])
def get_sales_data():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM order_detail"))
            sales = [dict(row) for row in result.mappings()]
        return jsonify({"sales_data": sales})
    except Exception as e:
        return jsonify({"message": f"Error fetching sales data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

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
    try        query = "SELECT * FROM order_detail"
        df = pd.read_sql(query, engine)
        return jsonify(df.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"message": f"Error fetching sales data: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
