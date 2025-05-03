from flask import Flask, request, jsonify, render_template
import os
from transformers import pipeline

app = Flask(__name__)

# Initialize the Hugging Face model (You can use GPT-3, T5, or another model)
summarizer = pipeline("summarization")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    if file:
        # Parse and process the resume (You can add parsing logic here)
        # For now, just return the file name
        return jsonify({"filename": file.filename, "message": "File uploaded successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5444, debug=True)
