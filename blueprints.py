import os
from flask import *
from werkzeug.utils import secure_filename


webapp_bp = Blueprint('webapp_bp', __name__, template_folder='templates')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@webapp_bp.route('/upload', methods=['GET', 'POST'])
def upload():    
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(request.url)
    return render_template('upload.html')

@webapp_bp.route('/', methods=['GET', 'POST'])
def filelist():
    return render_template('upload.html')

@webapp_bp.route('/download/<filename>', methods=['GET', 'POST'])
def download_file(filename):
    pass