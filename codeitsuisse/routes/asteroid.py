import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluate_asteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    input_value = data.get("test_cases")
    answer = list()

    for test in input_value:
        highest_score, highest_origin = int(), int()
        for i in range(len(test)):
            if i == len(test) or i == 0:
                current_score = 1
            else:
                lower_origin, higher_origin, current_score, value = i - 1, i + 1, 1, 0
                while higher_origin < len(test) and lower_origin >= 0:
                    looping = False
                    while higher_origin < len(test) and test[lower_origin] == test[higher_origin]:
                        value += 1
                        higher_origin += 1
                        looping = True
                    if looping == True:
                        higher_origin -= 1
                    while lower_origin >= 0 and test[lower_origin] == test[higher_origin]:
                        value += 1
                        lower_origin -= 1
                    if looping == True:
                        higher_origin += 1
                    if test[lower_origin + 1] in astroids.keys():
                        if value < 10 and value >= 7:
                            value *= 1.5
                        elif value >= 10:
                            value *= 2
                        current_score += value
                        value = 0
                    if lower_origin >= 0 and highest_origin < len(test) and test[higher_origin] != test[lower_origin]:
                        break
            if current_score > highest_score:
                highest_origin = i
                highest_score = current_score
        cur_result = {"input": test, "score": highest_score, "origin": highest_origin}
        answer.append(cur_result)
    logging.info("My result :{}".format(answer))
    return json.dumps(answer)
