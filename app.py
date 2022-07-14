import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/uploads'
IMG_NAME = 'cat.54.jpg'
upld = '../static/uploads/cat.54.jpg'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:

            return redirect(request.url)
        file = request.files['file']
        
        if file.filename == '':
            # flash('No selected file')
            
            
            return f'<h2>No selected file!!!</h2>'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # flash(f'{filename} successfully uploaded')
            # return redirect(url_for('download_file', name=filename))
            return f'<h2>{filename} uploaded successfully!!! </h2>'

    return render_template('index.html')




@app.route('/images')
def show_images():
    return render_template('images.html')


if __name__ == "__main__":
    app.run(debug=True)



