import logging
from flask import Flask, jsonify, request
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

# --- Tuya Access Data (ჩასვი შენი) ---
ACCESS_ID = "yp5juctvemjk88kc9q9e"
ACCESS_KEY = "81ba0bb7686a4dc7b02b4b2b2af8972e"
ENDPOINT = "https://openapi.tuyaeu.com"
DEVICE_ID = "bfc01f692b9329892vs0u"
COMMAND_CODE = "switch_1"

# --- Tuya Init ---
TUYA_LOGGER.setLevel(logging.INFO)
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

app = Flask(__name__)

# --- ტესტი GET მეთოდით (რადგან POST ბრაუზერში არ მუშაობს) ---
@app.route("/garage/on", methods=["GET", "POST"])
def garage_on():

    # მხოლოდ ტესტისთვის, GET-ით POST-ს გავუშვებთ
    if request.method == "GET":
        return jsonify({"info": "Use POST to activate device."})

    # POST ნამდვილი მოქმედება
    body = {
        "commands": [
            {"code": COMMAND_CODE, "value": True}
        ]
    }

    resp = openapi.post(f"/v1.0/iot-03/devices/{DEVICE_ID}/commands", body)
    return jsonify(resp)

@app.route("/")
def index():
    return "Tuya Server Running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
