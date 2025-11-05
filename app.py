from flask import Flask, request, jsonify
import psycopg2
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

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
    logging.critical(f"Critical error connecting to the database: {e}")
    exit(1)

@app.route('/api/data', methods=['GET'])
def get_data():
    if conn is None:
        return jsonify({'error': 'Database connection failed.'}), 500
    
    # Logic to retrieve data from the database
    try:
        # Example data retrieval logic (to be implemented)
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM your_table_name')  # Replace with actual query
            data = cursor.fetchall()  # Fetch data

        return jsonify({'data': data}), 200
    except Exception as e:
        logging.error(f"Error retrieving data: {str(e)}")
        return jsonify({'error': 'An error occurred while retrieving data.'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)