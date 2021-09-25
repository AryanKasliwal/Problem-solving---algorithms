import logging
import json
from math import gcd

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


def fraction(p, q):
    d = gcd(p, q)

    p = p // d
    q = q // d

    return p, q


def processQuestions(questions, maxRating):
    output_list = []
    for q in questions:
        for i in q:
            output_list.extend([x for x in range(i['from'], i['to'] + 1)])

    output_list = filter(lambda number: number <= maxRating, output_list)
    output_list = filter(lambda number: number >= 1, output_list)
    count = len(set(output_list))

    return count


def processInterview(input):
    questions = input["questions"]
    maxRating = input["maxRating"]

    return processQuestions(questions, maxRating)


@app.route('/stig/perry', methods=['POST'])
def evaluate_perry():
    input = request.get_json()
    logging.info("data sent for evaluation {}".format(input))
    result = []
    for i in range(len(input)):
        p = processInterview(input[i])
        q = input[i]["maxRating"]
        p, q = fraction(p, q)
        obj = {
            "p": p,
            "q": q
        }
        result.append(obj)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

