import numpy as np


def outcome_of_rolling_unfair_dice_k_time(dist_prob_1: float, k_time: int) -> float:
    
    """
     The sum of outcomes for rolling an unfair dice K times.

     This function returns an array. The last two elements are the 
     range of probability distribution.
     The range is: 'k_time' to 'k_time*(number_of_sides)'

     Other elements contain probabilities for getting a summation 
     from 'k_time' to 'k_time*(number_of_sides)'.

    """
    
    if k_time != int(k_time):
        raise ValueError("The function only accepts integer values of k")
    if len(dist_prob_1) < 2:
        raise ValueError("The number of sides should be more than 1")
    if k_time < 1:
        raise ValueError("Roll count should be more than 0")
    if k_time > 100 or len(dist_prob_1) > 100:
        raise ValueError("Limited to 100 sides or rolling to avoid memory issues")
        
    prob_dist = 1
    iter1 = 0
    while iter1 < k_time:
        prob_dist = np.convolve(prob_dist, dist_prob_1)
        iter1 = iter1 + 1
        
    prob_index = np.concatenate((prob_dist, np.array([k_time, k_time*len(dist_prob_1)])))

    return prob_index
