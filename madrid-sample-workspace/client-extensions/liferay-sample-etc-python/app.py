#!/usr/bin/env python3

from flask import Flask, request, jsonify
import requests
import configparser
import jwt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Read configuration from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Extract configuration values
server_port = config.getint('default', 'server.port')
lxc_dxp_main_domain = config.get('default', 'com.liferay.lxc.dxp.mainDomain', fallback='localhost:4001')
lxc_dxp_server_protocol = config.get('default', 'com.liferay.lxc.dxp.server.protocol', fallback='http')
liferay_oauth2_jwt_secret = config.get('default', 'liferay.oauth2.jwt.secret')

# Create Flask app
app = Flask(__name__)

# Log configuration
logger.info(f"Configuration: {config._sections}")

# Middleware for decoding Liferay JWT token
def liferay_jwt(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            try:
                decoded_token = jwt.decode(token.split(' ')[1], liferay_oauth2_jwt_secret, algorithms=['HS256'])
                request.liferay_user = decoded_token
            except jwt.InvalidTokenError:
                return jsonify({'error': 'Invalid token'}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

# CORS middleware
@app.after_request
def cors_with_ready(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

# Readiness check endpoint
@app.route(config.get('default', 'readyPath'), methods=['GET'])
def ready():
    return 'READY'

# Sample endpoint
@app.route('/sample/object/action/1', methods=['POST'])
#@liferay_jwt
def sample_object_action():
    json_data = request.get_json()
    logger.info(json_data)

    # WRITE YOUR CODE HERE
    # ...

    return jsonify(json_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=server_port, debug=True)
