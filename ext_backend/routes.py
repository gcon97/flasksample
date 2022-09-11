from flask import jsonify
from ext_backend import app


@app.route('/', methods = ['GET'])
def home():
    return jsonify(f"It's working! It's working!")
    
 

