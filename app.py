
from flask import Flask, request, redirect, url_for, jsonify
from database import db, User, File
from user_management import UserManager
from encryption import Encryption

from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')


import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uploads.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db.init_app(app)
user_manager = UserManager(app)

encryption = Encryption()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    return user_manager.register(data['username'], data['email'], data['password'])

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    password = request.form['password']
    encrypted_content = encryption.encrypt(file.read().decode(), password)
    new_file = File(filename=file.filename, encrypted_content=encrypted_content, owner_id=data['user_id']) # Assuming user_id is retrieved properly
    db.session.add(new_file)
    db.session.commit()
    return jsonify({'message': 'File uploaded successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

