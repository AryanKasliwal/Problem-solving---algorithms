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
    return "Tracie Temblador, Rebekah Regnier, Franklin Filippi, Farrah Frasure, Chantel Corn, Colin Crail, Gary Ginsburg, Jesse Julio, Margit Mello, Lester Larin"

