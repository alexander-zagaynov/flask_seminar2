from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from flask import PurePath, Path

app = Flask(__name__)


@app.route('/')
def index():
    return'Hello ! или Привет!'


app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filenam)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл {file_name} загружен на сервер'
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
