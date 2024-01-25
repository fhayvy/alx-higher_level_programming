#!/usr/bin/python3
def weight_average(my_list=[]):
    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return (0)
    else:
        weighted_mean = total_score / total_weight
        return (weighted_mean)
