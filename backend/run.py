from quart import Quart, escape, request, jsonify
from quart_cors import CORS
from daikin_aircon_pylib import daikin_aircon


app = Quart(__name__)
CORS(app)

AIRCON_ADDR='10.33.1.244'

def _get_aircon():
    return daikin_aircon.Aircon(AIRCON_ADDR)

@app.route('/api/')
async def hello():
    name = request.args.get("name", "World")
    await return jsonify('Hello')

@app.route('/api/power/start')
async def power_start():
    aircon = _get_aircon()
    aircon.set_power(True)
    await return jsonify('OK')

@app.route('/api/power/stop')
async def power_stop():
    aircon = _get_aircon()
    aircon.set_power(False)
    await return jsonify('OK')

@app.route('/api/power/status')
async def get_power_status():
    aircon = _get_aircon()
    status={}
    status['power'] = aircon.get_power()
    await return jsonify(status)
    
@app.route('/api/sensor/info')
async def get_sensor_info():
    aircon = _get_aircon()
    info = aircon.get_sensor_info()
    await return jsonify(info)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
