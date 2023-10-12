from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/hello")
def helloworld2():
    return "Hallo semuaa!!"    


# Data awal
data = ['satu', 'dua', 'tiga']

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/add_data/<string:new_data>', methods=['POST'])
def add_data(new_data):
    data.append(new_data)
    return jsonify({"message": "Data telah ditambahkan", "data": new_data})

@app.route('/update_data/<int:index>', methods=['PUT'])
def update_data(index):
    if index >= 0 and index < len(data):
        new_value = request.json.get('new_value')
        data[index] = new_value
        return jsonify({"message": "Data telah diperbarui", "data": data[index]})
    else:
        return jsonify({"message": "Indeks data tidak valid"})

@app.route('/delete_data/<int:index>', methods=['DELETE'])
def delete_data(index):
    if 0 <= index < len(data):
        deleted_value = data.pop(index)
        return jsonify({"message": "Data telah dihapus", "deleted_data": deleted_value})
    else:
        return jsonify({"message": "Indeks data tidak valid"})

    
if __name__ == "__main__":
    app.run()