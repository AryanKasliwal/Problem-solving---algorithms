import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


class Room:
    def __init__(self, id, arrangement, interested_individuals):
        self.id = id
        self.positioning = arrangement
        self.interested_individuals = interested_individuals
        self.traversal_distances = [[0 for x in range(len(self.positioning[0]))] for y in range(len(self.positioning))]
        for i in range(len(arrangement)):
            for j in range(len(arrangement[i])):
                if arrangement[i][j] == 3:
                    self.infected_row = i
                    self.infected_column = j
                elif self.positioning[i][j] == 0 or self.positioning[i][j] == 2:

        while len(self.interested_people) != 0:
            self.interested_people.pop(0)
        for person in interested_individuals:
            person_x = int(person.split(",")[0])
            person_y = int(person.split(",")[1])
            self.interested_people.append((person_x, person_y))

    infected_row, infected_column = (0, 0)
    interested_people = []
    traversal_positioning = []

    def diagonal_time_taken(self, array):
        output = dict()
        self.traversal_distances = [[0 for x in range(len(self.positioning[0]))] for y in range(len(self.positioning))]
        for index, person in enumerate(array):
            flag = False
            if self.positioning[int(person[0])][int(person[1])] == 2 or self.positioning[person[0]][person[1]] == 0:
                output[array[index]] = -1
            else:
                visited = [[0 for x in range(len(self.positioning[0]))] for y in range(len(self.positioning))]
                for i in range(len(visited)):
                    for j in range(len(visited[i])):
                        if self.positioning[i][j] == 0 or self.positioning[i][j] == 2:
                            visited[i][j] = 1
                        else:
                            visited[i][j] = 0
                queue = [(self.infected_row, self.infected_column)]
                visited[self.infected_row][self.infected_column] = 1
                while len(queue) != 0:
                    p = queue[0]
                    queue.pop(0)
                    if p == person:
                        output[array[index]] = self.traversal_distances[p[0]][p[1]]
                        flag = True

                    if p[0] - 1 >= 0 and visited[p[0] - 1][p[1]] == 0:
                        if self.positioning[p[0] - 1][p[1]] == 1 or self.positioning[p[0] - 1][p[1]] == 3:
                            self.traversal_distances[p[0] - 1][p[1]] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0] - 1, p[1]))
                            visited[p[0] - 1][p[1]] = 1

                    if p[0] + 1 < len(self.positioning) and visited[p[0] + 1][p[1]] == 0:
                        if self.positioning[p[0] + 1][p[1]] == 1 or self.positioning[p[0] + 1][p[1]] == 3:
                            self.traversal_distances[p[0] + 1][p[1]] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0] + 1, p[1]))
                            visited[p[0] + 1][p[1]] = 1

                    if p[1] - 1 >= 0 and visited[p[0]][p[1] - 1] == 0:
                        if self.positioning[p[0]][p[1] - 1] == 1 or self.positioning[p[0]][p[1] - 1] == 3:
                            self.traversal_distances[p[0]][p[1] - 1] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0], p[1] - 1))
                            visited[p[0]][p[1] - 1] = 1

                    if p[1] + 1 < len(self.positioning[0]) and visited[p[0]][p[1] + 1] == 0:
                        if self.positioning[p[0]][p[1] + 1] == 1 or self.positioning[p[0]][p[1] + 1] == 3:
                            self.traversal_distances[p[0]][p[1] + 1] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0], p[1] + 1))
                            visited[p[0]][p[1] + 1] = 1

                    if p[0] - 1 >= 0 and p[1] - 1 >= 0 and visited[p[0] - 1][p[1] - 1] == 0:
                        if self.positioning[p[0] - 1][p[1] - 1] == 1 or self.positioning[p[0] - 1][p[1] - 1] == 3:
                            self.traversal_distances[p[0] - 1][
                                p[1] - 1] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0] - 1, p[1] - 1))
                            visited[p[0] - 1][p[1] - 1] = 1

                    if p[0] - 1 >= 0 and p[1] + 1 < len(self.positioning[0]) and visited[p[0] - 1][p[1] + 1] == 0:
                        if self.positioning[p[0] - 1][p[1] + 1] == 1 or self.positioning[p[0] - 1][p[1] + 1] == 3:
                            self.traversal_distances[p[0] - 1][
                                p[1] + 1] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0] - 1, p[1] + 1))
                            visited[p[0] - 1][p[1] + 1] = 1

                    if p[0] + 1 < len(self.positioning) and p[1] - 1 >= 0 and visited[p[0] + 1][p[1] - 1] == 0:
                        if self.positioning[p[0] + 1][p[1] - 1] == 1 or self.positioning[p[0] + 1][p[1] - 1] == 3:
                            self.traversal_distances[p[0]][p[1] - 1] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0] + 1, p[1] - 1))
                            visited[p[0] + 1][p[1] - 1] = 1

                    if p[0] + 1 < len(self.positioning) and p[1] + 1 < len(self.positioning[0]) and visited[p[0] + 1][
                        p[1] + 1] == 0:
                        if self.positioning[p[0] + 1][p[1] + 1] == 1 or self.positioning[p[0] + 1][p[1] + 1] == 3:
                            self.traversal_distances[p[0] + 1][
                                p[1] + 1] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0] + 1, p[1] + 1))
                            visited[p[0] + 1][p[1] + 1] = 1
                if not flag:
                    output[array[index]] = -1
        return output

    def horizontal_time_taken(self, array):
        output = dict()
        self.traversal_distances = [[0 for x in range(len(self.positioning[0]))] for y in range(len(self.positioning))]
        for index, person in enumerate(array):
            flag = False
            if self.positioning[int(person[0])][int(person[1])] == 2 or self.positioning[person[0]][person[1]] == 0:
                output[array[index]] = -1
            else:
                visited = [[0 for x in range(len(self.positioning[0]))] for y in range(len(self.positioning))]
                for i in range(len(self.positioning)):
                    for j in range(len(self.positioning[i])):
                        if self.positioning[i][j] == 0 or self.positioning[i][j] == 2:
                            visited[i][j] = 1
                        else:
                            visited[i][j] = 0
                queue = [(self.infected_row, self.infected_column)]
                visited[self.infected_row][self.infected_column] = 1
                while len(queue) != 0:
                    p = queue[0]
                    queue.pop(0)
                    if p == person:
                        output[array[index]] = self.traversal_distances[p[0]][p[1]]
                        flag = True

                    if p[0] - 1 >= 0 and visited[p[0] - 1][p[1]] == 0:
                        if self.positioning[p[0] - 1][p[1]] == 1 or self.positioning[p[0] - 1][p[1]] == 3:
                            self.traversal_distances[p[0] - 1][p[1]] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0] - 1, p[1]))
                            visited[p[0] - 1][p[1]] = 1

                    if p[0] + 1 < len(self.positioning) and visited[p[0] + 1][p[1]] == 0:
                        if self.positioning[p[0] + 1][p[1]] == 1 or self.positioning[p[0] + 1][p[1]] == 3:
                            self.traversal_distances[p[0] + 1][p[1]] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0] + 1, p[1]))
                            visited[p[0] + 1][p[1]] = 1

                    if p[1] - 1 >= 0 and visited[p[0]][p[1] - 1] == 0:
                        if self.positioning[p[0]][p[1] - 1] == 1 or self.positioning[p[0]][p[1] - 1] == 3:
                            self.traversal_distances[p[0]][p[1] - 1] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0], p[1] - 1))
                            visited[p[0]][p[1] - 1] = 1

                    if (p[1] + 1) < len(self.positioning[0]) and visited[p[0]][p[1] + 1] == 0:
                        if self.positioning[p[0]][p[1] + 1] == 1 or self.positioning[p[0]][p[1] + 1] == 3:
                            self.traversal_distances[p[0]][p[1] + 1] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0], p[1] + 1))
                            visited[p[0]][p[1] + 1] = 1
                if not flag:
                    output[array[index]] = -1
        return output

    def horizontal_time_taken_forX(self, array):
        output = dict()
        self.traversal_distances = [[0 for x in range(len(self.positioning[0]))] for y in range(len(self.positioning))]
        for index, person in enumerate(array):
            flag = False
            if self.positioning[int(person[0])][int(person[1])] == 2 or self.positioning[person[0]][person[1]] == 0:
                output[array[index]] = -1
            else:
                visited = [[0 for x in range(len(self.positioning[0]))] for y in range(len(self.positioning))]
                queue = [(self.infected_row, self.infected_column)]
                visited[self.infected_row][self.infected_column] = 1
                while len(queue) != 0:
                    p = queue[0]
                    queue.pop(0)
                    if p == person:
                        output[array[index]] = self.traversal_distances[p[0]][p[1]]
                        flag = True

                    if p[0] - 1 >= 0 and visited[p[0] - 1][p[1]] == 0:
                        if self.positioning[p[0] - 1][p[1]] == 1 or self.positioning[p[0] - 1][p[1]] == 3:
                            self.traversal_distances[p[0] - 1][p[1]] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0] - 1, p[1]))
                            visited[p[0] - 1][p[1]] = 1

                    if p[0] + 1 < len(self.positioning) and visited[p[0] + 1][p[1]] == 0:
                        if self.positioning[p[0] + 1][p[1]] == 1 or self.positioning[p[0] + 1][p[1]] == 3:
                            self.traversal_distances[p[0] + 1][p[1]] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0] + 1, p[1]))
                            visited[p[0] + 1][p[1]] = 1

                    if p[1] - 1 >= 0 and visited[p[0]][p[1] - 1] == 0:
                        if self.positioning[p[0]][p[1] - 1] == 1 or self.positioning[p[0]][p[1] - 1] == 3:
                            self.traversal_distances[p[0]][p[1] - 1] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0], p[1] - 1))
                            visited[p[0]][p[1] - 1] = 1

                    if p[1] + 1 < len(self.positioning[0]) and visited[p[0]][p[1] + 1] == 0:
                        if self.positioning[p[0]][p[1] + 1] == 1 or self.positioning[p[0]][p[1] + 1] == 3:
                            self.traversal_distances[p[0]][p[1] + 1] += 1  # self.traversal_distances[p[0]][p[1]] + 1
                            queue.append((p[0], p[1] + 1))
                            visited[p[0]][p[1] + 1] = 1
                if not flag:
                    output[array[index]] = -1
        return output

    def healthy_people(self):
        people = []
        for i in range(len(self.positioning)):
            for j in range(len(self.positioning[i])):
                if self.positioning[i][j] == 1:
                    people.append((i, j))
        return people

    def p1(self):
        return self.horizontal_time_taken(self.interested_people)

    def p2(self):
        people = self.healthy_people()
        ans = self.horizontal_time_taken(people)
        return ans

    def p3(self):
        people = self.healthy_people()
        max_value = 0
        ans = self.diagonal_time_taken(people)
        for value in ans.values():
            if value == -1:
                return -1
            if value > max_value:
                max_value = value
        return max_value

    def distance_between_points(self, p1, p2):
        return (((p1[0] - p2[0]) * (p1[0] - p2[0])) + ((p1[1] - p2[1]) * (p1[1] - p2[1])))

    def calculate_energy(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) - 1

    def get_nearest_points(self, p2_result):
        negative_values = []
        positive_values = []
        closest_points_dict = dict()
        for (x, y), value in p2_result.items():
            if value == -1:
                negative_values.append((x, y))
                closest_points_dict[(x, y)] = (0, 0)
            else:
                positive_values.append((x, y))
        for i in negative_values:
            closest_distance = 1000000000000
            for j in positive_values:
                cur_distance = self.distance_between_points(i, j)
                if (cur_distance < closest_distance):
                    closest_points_dict[i] = j
                    closest_distance = cur_distance
        return closest_points_dict

    def p4(self, p2_result, ans1):
        if ans1 != -1:
            return 0
        else:
            closest_points_dict = self.get_nearest_points(p2_result)
            answer = 0
            for (p11, p12), (p21, p22) in closest_points_dict.items():
                answer += self.calculate_energy((p11, p12), (p21, p22))
            return answer


@app.route('/parasite', methods=['POST'])
def evaluate_parasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    rooms = []
    output_list = []
    for data_point in data:
        output_dict = {}
        room = Room(data_point["room"], data_point["grid"], data_point["interestedIndividuals"])
        output_dict["room"] = data_point["room"]
        rooms.append(room)
        ans = room.p1()
        output_p1 = {}
        index = 0
        for key in data_point['interestedIndividuals']:
            output_p1[key] = list(ans.values())[index]
            index += 1
        output_dict['p1'] = output_p1
        ans1 = 0
        answer = room.p2()
        for value in answer.values():
            if value == -1:
                ans1 = -1
                break
            if value > ans1:
                ans1 = value

        output_dict['p2'] = ans1

        ans2 = room.p3()
        output_dict['p3'] = ans2

        ans3 = room.p4(answer, ans1)
        output_dict['p4'] = ans3

        output_list.append(output_dict)
        logging.info("data sent for evaluation {}".format(output_list))
    return json.dumps(output_list)
