from flask import Flask
from flask import g


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'



def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
