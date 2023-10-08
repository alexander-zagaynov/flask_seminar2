from flask import Flask, request

app = Flask(__name__)


@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похлже ты опытный игрокб раз имеешь уровень {level}<br>'

    else:
        text = 'Приветб новичок <br>'
    return  f'{text} {request.args}'


if __name__ == '__main__':
    app.run(debug=True)