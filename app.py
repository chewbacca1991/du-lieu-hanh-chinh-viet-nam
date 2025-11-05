from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Thiết lập cơ sở dữ liệu PostgreSQL
conn = psycopg2.connect(
    dbname='yourdbname',
    user='yourusername',
    password='yourpassword',
    host='localhost',
    port='5432'
)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Logic để lấy dữ liệu từ cơ sở dữ liệu
    return jsonify({'message': 'API data retrieved successfully.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)