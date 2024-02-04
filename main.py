from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
data=[]

@app.route('/data', methods=['POST'])
def create_data():
    new_data = request.get_json()
    data.append(new_data)
    return jsonify({'message': 'Data created successfully'})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)