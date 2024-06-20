## The Sum of Outcomes for Rolling an N-sided Dice K Times Through Convolution

This repository presents functions in the Python programming language for computing probabilities of finding different numbers as the sum of outcomes for rolling an N-sided dice K times.

There are two functions. One is applicable for a fair dice with a uniform probability distribution. Another is applicable for both fair and unfair dice.

The following function takes the number of sides and the number of rolling as input and returns probabilities with the range of indexes.
#### def outcome_of_rolling_n_sided_dice_k_time(n_side: int, k_time: int) -> float:

The following function takes the probabilities of getting different sides and the number of rolling as input and returns probabilities with the range of indexes.
#### def outcome_of_rolling_unfair_dice_k_time(dist_prob_1: float, k_time: int) -> float:
This function requires an array as the first input. However, this function can compute probabilities for unfair dice. In an unfair dice, the probabilities of getting different sides are different.

I have also submitted a pull request to a repository to share the function with a larger audience.
The request: https://github.com/TheAlgorithms/Python/pull/11463


