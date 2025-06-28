from flask import Flask, render_template, request, send_file
from encryption import encrypt_file, decrypt_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file:
        data = uploaded_file.read()
        encrypted = encrypt_file(data)
        path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename + '.enc')
        with open(path, 'wb') as f:
            f.write(encrypted)
    return 'File uploaded and encrypted successfully! <a href="/">Back</a>'

@app.route('/download/<filename>')
def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    with open(path, 'rb') as f:
        encrypted = f.read()
    decrypted = decrypt_file(encrypted)
    temp_path = 'decrypted_' + filename.replace('.enc', '')
    with open(temp_path, 'wb') as f:
        f.write(decrypted)
    return send_file(temp_path, as_attachment=True)
