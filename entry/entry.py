from flask_cors import CORS, cross_origin
from flask import Flask, request
from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
    return 'Hello from Flask!'

@app.route('/comment/<name>')
@cross_origin()
def comment(name):
    pon = f"{request.view_args['name']}"
    output = model.generate(pon, max_tokens=30)
    print(output)
    return output
