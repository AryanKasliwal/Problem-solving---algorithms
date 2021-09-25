import logging
import json

from flask import request, jsonify
from sseclient import SSEClient

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tic-tac-toe', methods=['POST'])
def evaluateArena():
    battle_id_data = request.get_json()
    logging.info("data sent for evaluation {}".format(battle_id_data))
    battle_id = battle_id_data.get("battleId")
    logging.info("Battle Id :{}".format(battle_id))
    next_input = request.get_json()
    logging.info(next_input)
    return json.dumps(next_input)