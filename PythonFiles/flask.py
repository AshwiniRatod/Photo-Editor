from flask import Flask,render_template,request,jsonify
import cv2
import numpy as np
from crop import crop_image

app = Flask(__name__)
@app.route('/')
def index():
    render_template('index.html')
@app.route('/crop',methods = ['POST'])
def crop_route():
    file  =request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(),np.unit8),cv2.IMREAD_COLOR)
    cropped = crop_image(img)
    output_path = "static/processed.jpg"
    cv2.imwrite(output_path,cropped)
    return jsonify({"url":"/"+output_path})
if __name__ == '__main__':
    app.run(debug=True)