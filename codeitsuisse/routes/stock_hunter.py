import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/square', methods=['POST'])
def evaluate_stock_hunter():

    def derive_map(entry_point, vertical_stepper, horizontal_spacer, target_point, gridDepth, gridKey):

        entry_x = entry_point['EntryX']
        entry_y = entry_point['EntryY']
        target_x = target_point['TargetX']
        target_y = target_point['TargetY']
        rows = max(entry_x, target_x) + 1
        cols = max(entry_y, target_y) + 1

        def calc_risk_level(risk_level, rows, cols):

            for i in range(rows):
                for j in range(cols):
                    if i == 0 and j == 0:
                        risk_index_value = 0
                    elif i == target_x and j == target_y:
                        risk_index_value = 0
                    elif i == 0:
                        risk_index_value = vertical_stepper * j
                    elif j == 0:
                        risk_index_value = horizontal_spacer * i
                    else:
                        risk_index_value = risk_level[i - 1][j] * risk_level[i][j - 1]
                    risk_level[i][j] = (risk_index_value + gridDepth) % gridKey

            return risk_level

        risk_index_initialize = [[0 for y in range(cols)] for x in range(rows)]
        risk_level_value = calc_risk_level(risk_index_initialize, rows, cols)
        risk_map = [["Z" for x in range(cols)] for y in range(rows)]

        risk_cost = [[0 for y in range(cols)] for x in range(rows)]
        for i in range(len(risk_level_value)):
            for j in range(len(risk_level_value[i])):
                if (risk_level_value[i][j] % 3 == 0):
                    risk_cost[i][j] = 3
                    risk_map[i][j] = "L"
                if (risk_level_value[i][j] % 3 == 1):
                    risk_cost[i][j] = 2
                    risk_map[i][j] = "M"
                if (risk_level_value[i][j] % 3 == 2):
                    risk_cost[i][j] = 1
                    risk_map[i][j] = "S"
        return risk_cost, risk_map

    def find_minimum_cost(arr):
        if (len(arr), len(arr[0])) == (0, 0):
            return 0
        row = len(arr)
        col = len(arr[0])

        cache = [[0 for y in range(col)] for x in range(row)]
        cache[0][0] = arr[0][0]

        for i in range(1, col):
            cache[0][i] = cache[0][i - 1] + arr[0][i]

        for j in range(1, row):
            cache[j][0] = cache[j - 1][0] + arr[j][0]

        for i in range(1, row):
            for j in range(1, col):
                if cache[i - 1][j] > cache[i][j - 1]:
                    cache[i][j] = cache[i][j - 1] + arr[i][j]
                else:
                    cache[i][j] = cache[i - 1][j] + arr[i][j]
        return cache[row - 1][col - 1]

    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    output_list = []
    for test_case in data:
        output_dict = {}
        entry_point = test_case["entryPoint"]
        target_point = test_case["targetPoint"]
        gridDepth = test_case["gridDepth"]
        gridkey = test_case["gridKey"]
        horizontal_spacer = test_case["horizontalStepper"]
        vertical_stepper = test_case["verticalStepper"]
        risk_cost, risk_map = derive_map(entry_point, vertical_stepper, horizontal_spacer, target_point, gridDepth, gridkey)
        risk_cost = [list(x) for x in zip(*risk_cost)]
        risk_map = [list(x) for x in zip(*risk_map)]

        minimum_cost = find_minimum_cost(risk_cost) - risk_cost[0][0]
        output_dict['gridMap'] = risk_map
        output_dict['minimumCost'] = minimum_cost
        output_list.append(output_dict)

    logging.info("My result :{}".format(output_list))
    return json.dumps(output_list)

