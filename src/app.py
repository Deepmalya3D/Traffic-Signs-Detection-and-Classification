from flask import Flask, request, render_template, send_file
from ultralytics import YOLO
from werkzeug.utils import secure_filename
from PIL import Image
import os
import warnings

warnings.filterwarnings("ignore")

## load the model
# with open("best.onnx", "rb") as model_file:
model = YOLO("best.onnx")

app =Flask(__name__)

UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods = ["GET", "POST"])
def road_sign_endpoint():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html", error = "No file part")
        
        file = request.files["file"]

        if file.filename == "":
            return render_template("index.html", error = "No selected file")
        
        if file:
            filename = file.filename
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            input_image = Image.open(file_path)

            output = model(input_image, imgsz = 320)
            predicted_image = Image.fromarray(output[0].plot()[..., ::-1])

            predicted_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'predicted_image.jpg')
            predicted_image.save(predicted_image_path)

            return send_file(predicted_image_path, mimetype='image/jpeg')
        

if __name__ == "__main__":
    ## Run the app
    app.run(debug = True)
