from flask import Flask, jsonify

app = Flask(__name__)

from ext_backend import routes