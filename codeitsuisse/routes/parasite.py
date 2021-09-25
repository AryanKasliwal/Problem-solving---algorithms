import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def evaluate_parasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data[1].get("room")
    logging.info("My result :{}".format(inputValue))
    return json.dumps(inputValue)



