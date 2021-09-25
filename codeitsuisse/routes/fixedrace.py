import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluate_race():
    data = request.get_data(as_text=True)
    # logging.info("data sent for evaluation {}".format(data))
    # # inputList = data.split(",")
    # # result = str(data)
    # logging.info("My result :{}".format(data))
    return "Cecila Cribb, Isreal Isenhour, Lauretta Lippard, Sharyl Shepler, Rossana Rackers, Francisco Finchum, Alaina Adolphson, Brady Broda, Jannet Jacquemin, Margit Mello"

