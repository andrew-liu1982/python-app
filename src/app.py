
from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

# 'api/v1/details' 
@app.route('/api/v1/details')
def details():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = socket.gethostname()
    return jsonify({'time': current_time, 'hostname': hostname})

# 'api/v1/health'
@app.route('/api/v1/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True)


