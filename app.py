from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
        <body>
            <h1 style="color: blue; font-family: Arial, sans-serif; text-align: center;">
                Hello, <span style="color: red;">prashobh this is from devops world!</span>
            </h1>
        </body>
    </html>
    '''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
