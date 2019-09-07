from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import ResNet50

app = Flask(__name__)
app.debug = True


MODEL_PATH = 'models/your_model.h5'

model = ResNet50(weights='imagenet')

@app.route('/')
def index():
	return render_template('pages/index.html')

@app.route('/image')
def image():
	return render_template('pages/image.html')

@app.route('/predictor')
def predictor():
	return render_template('pages/predictor.html')

@app.route('/trainer')
def trainer():
	return render_template('pages/trainer.html')

def model_predict(img_path, model):
	img = image.load_img(img_path)
	x = image.img_to_array(img)
	preds = model.preict(x)
	return preds

@app.route('/predict')
def upload():

	if request.method == 'POST':
	
		f = request.files['file']
		f.save(file_path)
		preds = model_predict(file_path, model)
		pred_class = decode_predictions(preds, top=1)

		return pred_class

