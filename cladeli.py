from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Clash Royale Deck Library</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>User: {}</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
