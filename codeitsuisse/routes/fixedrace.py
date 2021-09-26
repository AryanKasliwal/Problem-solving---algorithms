import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluate_race():
    data = request.get_data(as_text=True)
    logging.info("data sent for evaluation {}".format(data))
    # # inputList = data.split(",")
    # # result = str(data)
    # logging.info("My result :{}".format(data))
    return "Bernadine Brackin, Damien Degraff,Winfred Wilton,Karina Kuder,,Jenniffer Jen,Alayna Alberson,Eva Epping,Kimberley Kincade,Marion Mcgahan,Brice Benigno"

