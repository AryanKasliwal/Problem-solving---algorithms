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
            astroids = {}

            if i == len(test) or i == 0:
                if highest_score < 1:
                    highest_score = 1
                    highest_origin = i
                continue

            current_score = 1
            lowest_origin, highest_origin = i - 1, i + 1

            while highest_origin < len(test) and lowest_origin >= 0:
                looping = False
                while lowest_origin >= 0 and test[lowest_origin] == test[highest_origin]:
                    try:
                        astroids[test[lowest_origin]] += 1
                    except:
                        astroids[test[lowest_origin]] = 1
                    lowest_origin -= 1
                    looping = True
                if looping:
                    lowest_origin += 1

                while highest_origin < len(test) and test[lowest_origin] == test[highest_origin]:
                    astroids[test[lowest_origin]] += 1
                    highest_origin += 1
                if looping:
                    lowest_origin -= 1

                if test[lowest_origin + 1] in astroids.keys():
                    num = astroids[test[lowest_origin + 1]]
                    if num < 7:
                        current_score += num
                    elif 8 < num < 11:
                        current_score += (num * 1.5)
                    else:
                        current_score += (num * 2)
                    astroids[test[lowest_origin + 1]] = 0

                if lowest_origin >= 0 and highest_origin < len(test) and test[lowest_origin] != test[highest_origin]:
                    break

            if current_score > highest_score:
                highest_score = current_score
                highest_origin = i

        cur_result = {"input": test, "score": highest_score, "origin": highest_origin}
        answer.append(cur_result)

    logging.info("My result :{}".format(answer))
    return json.dumps(answer)
