from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Setup PostgreSQL database connection
try:
    conn = psycopg2.connect(
        dbname=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        host=os.environ.get('DB_HOST', 'localhost'),
        port=os.environ.get('DB_PORT', '5432')
    )
except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")
    conn = None

@app.route('/api/data', methods=['GET'])
def get_data():
    # Logic to retrieve data from the database
    return jsonify({'message': 'API data retrieved successfully.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)