import copy
import random


class Hat:

    def __init__(self, **kwargs):
        self.balls_in_hat_current = balls_dict_to_list_convert(kwargs)
        self.balls_in_hat_at_start = copy.copy(self.balls_in_hat_current)

    def draw(self, number_of_balls_to_draw: int) -> list:
        self.balls_in_hat_current = copy.copy(self.balls_in_hat_at_start)
        chosen_balls = []

        if number_of_balls_to_draw > len(self.balls_in_hat_current):
            return self.balls_in_hat_current

        for i in range(number_of_balls_to_draw):
            draw_ball_index = random.randrange(0, len(self.balls_in_hat_current))
            chosen_balls.append(self.balls_in_hat_current[draw_ball_index])
            self.balls_in_hat_current.pop(draw_ball_index)

        return chosen_balls


def balls_dict_to_list_convert(balls_count_dictionary: dict) -> list:
    balls_list = []

    for ball_color, number_of_balls in balls_count_dictionary.items():
        for i in range(number_of_balls):
            balls_list.append(ball_color)

    return balls_list


def is_experiment_successful(expected_balls: list, drawed_balls: list) -> bool:
    for i in expected_balls:
        try:
            drawed_balls.pop(drawed_balls.index(i))
        except ValueError:
            return False

    return True


def experiment(hat: object, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    positive_result_counter = 0
    expected_balls_list = balls_dict_to_list_convert(expected_balls)

    for i in range(num_experiments):
        chosen_balls_list = hat.draw(num_balls_drawn)

        if is_experiment_successful(expected_balls_list, chosen_balls_list):
            positive_result_counter += 1

    probability = positive_result_counter / num_experiments

    return probability
