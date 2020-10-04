import os
from flask import *
from werkzeug.utils import secure_filename


webapp_bp = Blueprint('webapp', __name__, template_folder='templates')

def allowed_file(filename):
    from app import app
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@webapp_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            from app import app
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/')
    return render_template('upload.html')

@webapp_bp.route('/', methods=['GET', 'POST'])
def dashboard():
    filenames = os.listdir('files')
    return render_template('dashboard.html', filenames=filenames)

@webapp_bp.route('/download/<filename>', methods=['GET'])
def download(filename):
    return send_file('files/'+filename, as_attachment=True)

@webapp_bp.route('/preview/<filename>', methods=['GET'])
def preview(filename):
    return send_from_directory('files/', filename)