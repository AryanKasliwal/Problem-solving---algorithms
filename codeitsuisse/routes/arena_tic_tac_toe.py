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
    messages = SSEClient(f'https://cis2021-hk-individual.herokuapp.com/tic-tac-toe/play/{battle_id}')
    return json.dumps(messages)
