from flask import Flask
app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def index():
    return 'Hello, world'

if __name__ == '__main__':
    app.debug = True
    app.run()