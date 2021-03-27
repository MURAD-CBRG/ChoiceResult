from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'INFORMATION_SECURITY'


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result_page(nickname, level, rating):
    params = {
        'nickname': nickname,
        'level': level,
        'rating': rating
    }

    return render_template('result.html', params=params)


def main():
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
