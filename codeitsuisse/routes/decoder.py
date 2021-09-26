import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def evaluate_decoder():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = {"answer" : ['y', 'b', 'w', 'p', 'l']}
    logging.info("My result :{}".format(result))
    return json.dumps(result)



