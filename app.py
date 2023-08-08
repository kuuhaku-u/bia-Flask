from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/', methods=['POST'])
def predict():
    data = request.json
    if data and 'username' in data:
        username = data['username']
        return {"prediction":username}
    else:
        return "Username not provided in JSON data "
if __name__ == '__main__':
    app.run(debug=True)
