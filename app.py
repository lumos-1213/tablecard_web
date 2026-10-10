from flask import Flask,request,render_template,jsonify
import paho.mqtt.publish as publish
import json

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("base/index.html")

@app.route('/publish')
def publish_page():
    return render_template("base/publish_page.html")

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    name = data.get('name', '')
    title = data.get('title', '')
    payload = json.dumps({'name': name, 'title': title})
    try:
        publish.single(
            "topic/desk/001",
            payload,
            hostname="127.0.0.1",
            auth={'username': 'pi', 'password': 'raspberry'}
        )
        return jsonify({'msg': f'已发送："{name}"'})
    except Exception as e:
        return jsonify({'msg': f'发送失败： {e}'})

if __name__ == '__main__':
    app.run()
