import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def processQuestions(questions, maxRating):
    from_ = []
    to_ = []
    for q in questions:
        for i in q:
            from_.append(i["from"])
            to_.append(i["to"])

    min_ = max(from_)
    max_ = min(min(to_), maxRating)

    count = max_ - min_ + 1
    return count


def processInterview(input):
    questions = input["questions"]
    maxRating = input["maxRating"]

    return processQuestions(questions, maxRating)

@app.route('/stig/perry', methods=['POST'])
def evaluate():
    input = request.get_json()
    logging.info("data sent for evaluation {}".format(input))
    result = []
    for i in range(len(input)):
        q = processInterview(input[i])
        obj = {
            "p": 1,
            "q": q
        }
        result.append(obj)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

