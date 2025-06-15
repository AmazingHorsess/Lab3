from flask import Flask, request
from datetime import datetime
import os
app = Flask(__name__)


LOG_FILE_PATH = os.environ.get('LOG_FILE', 'app.log')

@app.route('/')
def index():
    log_message = f"Time: {datetime.now()}, Client IP: {request.remote_addr}\n"
    with open(LOG_FILE_PATH, 'a') as log_file:
        log_file.write(log_message)


    return "<h1>Hello, World! This is the main page.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)