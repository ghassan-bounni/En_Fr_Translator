import os
import logging

from flask import Flask, request, url_for, render_template

from model.model import En_Fr_Translator

app = Flask(__name__)

# define model path
model_path = './model/model.h5'

# create instance
model = En_Fr_Translator(model_path)
logging.basicConfig(level=logging.INFO)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/translate", methods=["GET", "POST"])
def predict():
    """Provide main prediction API route. Responds to both GET and POST requests."""
    logging.info("Predict request received!")

    en_sentence = request.args.get('en_sentence')
    prediction = model.predict(en_text=en_sentence)

    return render_template('index.html', fr_sentence=prediction, en_sentence=en_sentence)


def main():
    """Run the Flask app."""
    app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == "__main__":
    main()
