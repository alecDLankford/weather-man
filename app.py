from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_date():
    res = subprocess.check_output(['date']).decode('utf-8')
    return jsonify({'date': res.strip()})


if __name__ == '__main__':
    app.run()
