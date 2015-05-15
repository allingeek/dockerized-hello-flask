from flask import Flask
app = Flask(__name__)
import os
service_port = os.getenv('PORT', 3000)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = service_port)
