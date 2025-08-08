import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['STATIC_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600
app.config['MAX_CONTENT_LENGTH'] = 1000* 1024 * 1024  # Max size: 1000 MB
# Some simple permission settings
deletable = False
downloadable = True

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(path):
            files.append({
                'name': filename,
                'size': calc_size(os.path.getsize(path)),
                'upload_time': os.path.getctime(path)
            })
    
    # Sorted by upload time
    files.sort(key=lambda x: x['upload_time'], reverse=True)
    print('OK')
    return render_template('index.html', files=files, downloadable=downloadable, deletable=deletable)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    
    if file:
        filename = secure_filename(file.filename or "default_filename")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File uploaded successfully')
        return redirect(url_for('index'))
    
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    if downloadable:
        return send_from_directory(
            app.config['UPLOAD_FOLDER'],
            filename,
            as_attachment=True
        )
    else:
        flash("Downloading Not Allowed!")
        return redirect(url_for('index'))

@app.route('/delete/<filename>')
def delete_file(filename):
    if deletable:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File deleted successfully')
        except FileNotFoundError:
            flash('File not found')
        return redirect(url_for('index'))
    else:
        flash('Removing Not Allowed!')
        return redirect(url_for('index'))

@app.route('/static/<path:filename>')
def static_files(filename):
     return send_from_directory(app.config['STATIC_FOLDER', filename])

def calc_size(size):
    """ Calculate the unit of the simplified file size based on the input file size(in Bytes). """
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    level = 0
    while size / 1024 > 1 and level < 4:
        size /= 1024
        level += 1
    return [size, units[level]]


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
