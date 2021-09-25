import logging
import json
import math
from math import gcd

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


def fraction(p, q):
    d = gcd(p, q)

    p = p // d
    q = q // d

    return p, q


def fact(n):
    if (n <= 1):
        return 1
    return n * fact(n - 1)


def nPr(n, r):
    return math.floor(fact(n) / fact(n - r))

def processQuestions(questions, maxRating):
    # output_list = []
    # for q in questions:
    #     for i in q:
    #         output_list.extend([x for x in range(i['from'], i['to'] + 1) if x >= maxRating])
    #

    #count = len(set(output_list))

    return nPr(len(questions), 2)


def processInterview(input):
    questions = input["questions"]
    maxRating = input["maxRating"]

    return processQuestions(questions, maxRating)


@app.route('/stig/perry', methods=['POST'])
def evaluate_perry():
    input = request.get_json()
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

