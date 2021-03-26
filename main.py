import pickle
from flask import Flask, request, jsonify
from loadngo import translate

app=Flask('app')

@app.route('/suggest',methods=['POST'])
def predict():
    input_sentence = request.get_json()['input_sentence']
    print(input_sentence)
    prediction = translate(input_sentence)
    return jsonify({"output":prediction})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)