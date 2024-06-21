## The Sum of Outcomes for Rolling an N-sided Dice K Times Through Convolution

<img src="https://github.com/dipuk0506/dice/blob/main/Dice_interval5.png" width="700">
The image is collected from our paper [1].

### Scripts

This repository presents functions in the Python programming language for computing probabilities of finding different numbers as the sum of outcomes for rolling an N-sided dice K times.

There are two functions. One is applicable for a fair dice with a uniform probability distribution. Another is applicable for both fair and unfair dice.

The following function takes the number of sides and the number of rolling as input and returns probabilities with the range of indexes.
#### def outcome_of_rolling_n_sided_dice_k_time(n_side: int, k_time: int) -> float:

The following function takes the probabilities of getting different sides and the number of rolling as input and returns probabilities with the range of indexes.
#### def outcome_of_rolling_unfair_dice_k_time(dist_prob_1: float, k_time: int) -> float:
This function requires an array as the first input. However, this function can compute probabilities for unfair dice. In an unfair dice, the probabilities of getting different sides are different.

I have also submitted a pull request to a repository to share the function with a larger audience.
The request: https://github.com/TheAlgorithms/Python/pull/11463


### Convolution:
We are applying the digital convolution equation [2].

If $x$ is an $N_x$ point signal and $h$ is an $N_h$ point signal, their convolution ($y$) is an $N_x+N_h-1$ point signal. 

If indexes of $x$ are $i_x$ to $j_x$ and indexes of $h$ are $i_h$ to $j_h$, indexes of convolution ($y$) becomes $i_x+i_h$ to $j_x+j_h$.

Value at $l$ index ($y[l]$) becomes the summation of $x[index] \times h[l-index]$ values. The equation is as follows:

$$y[l] = \sum\limits_{index=-\inf}^{\inf} x[index] . h[l-index] $$

In this equation, $x[index]$ is zero when $index$ is out of the range of $x$. Also, $h[l-index]$ is zero when $l-index$ is out of the range of $h$.

Shortly, $y[l]$ becomes the summation of multiplication values ($\sum x[] \times h[]$) where the summation of indexes ([]+[]) is equal to $l$.


### Relationship Between Dice Throwing and Convolution

#### Two dice:
Suppose we are rolling two N-sided dice simultaneously. The possible outcomes for one dice is 1 to N. Each of one to N outcomes has a probability of 1/N.

Write probabilities as an array: [1/N, 1/N, 1/N.......(N-elements)]

Indexes of probabilities:[1, 2, 3, ...........N]

The possible summation of outcomes can be 2 to 2N. The summation is 2 when the outcomes from both dice are 1. The summation is 2N when the outcomes from both dice are N. Therefore, the range follows the rule of convolution.


The summation of indexes is 2 when both dice receive 1. The (1,1) combination.

The probability of summation of 2 becomes the multiplication of two probabilities: (1/N) and (1/N). 

The summation becomes 3 for (1,2) and (2,1) combinations.

Probabilities: (1/N) $\times$ (1/N) for (1,2) and (1/N) $\times$ (1/N) for (2,1)

Total probability of getting three as summation: 2 $\times$ (1/N) $\times$ (1/N).

The summation becomes 4 for (1,3), (2,2), and (3,1) combinations; when N is greater than or equal to 3.

The probability: 3 $\times$ (1/N) $\times$ (1/N)

The summation becomes 7 for (1,6), (2,5), (3,4), (4,3), (5,2), and (6,1) combinations; when N is greater than or equal to 6.

The probability: 6 $\times$ (1/N) $\times$ (1/N)

If N is 4, the summation becomes 7 for (3,4), and (4,3) combinations.

The probability: 2 $\times$ (1/N) $\times$ (1/N)

The summation becomes 2 $\times$ N-1 for (N, N-1) and (N-1, N) combinations and the probability is 2 $\times$ (1/N) $\times$ (1/N).

The summation becomes 2 $\times$ N for the (N, N) combination, and the probability is (1/N) $\times$ (1/N).

Therefore, we can get the probability of getting a sum using the convolution for two dice throwing.


Let's write the probability distribution of getting different summations for two dice throwing as follows:

The array of probability: [p2, p3, p4, ... p2N]

Indexes of probabilities: [2, 3, ..........,2N]

#### Three dice:
Suppose we are rolling another N-sided dice simultaneously with the previous two dice.

The range of probable summations will be 3 to 3 $\times$ N

The summation becomes 3 for (1, 1, 1) combination. Which is equal to the probability of getting as sum 2 in the first two rolls and 1 in the third; the ($\bf{2}$,1) combination. As 2 is the outcome of the summation from the first two dice, it is in the boldface.

That probability is p2 $\times$ (1/N).

The summation becomes 4 for ($\bf{2}$,2) and ($\bf{3}$,1) combinations.

The probability becomes p2 $\times$ (1/N) + p3 $\times$ (1/N)

Similarly, for all probable summation values (S), we found the following pattern:

Array1[index] is multiplied by Array2[S-index]

All multiplications are added to compute the probability of getting S as the sum.

Similarly, we can continue convoluting to obtain summation probabilities for more dice rolling.

#### Third dice is unfair:
Let us assume the third dice has M number of sides with non-uniform probability.

Let us assume probabilities are [q1, q2, q3, .... qM]

Indexes of probabilities: [1, 2, 3, ...........,M]

The range of getting different summation values is 3 to 2N+M.

The probability of getting 3 as summation is p2 $\times$ q1

The probability of getting 4 as summation is p2 $\times$ q2 + p3 $\times$ q1

Therefore, when dice rolling is mixed with fair and unfair dice, the convolution works.

Similarly, the convolution works with a k-number of unfair dice rolling.

#### Note:
We used this approach to draw figures and write discussions in papers [1,3].


#### Reference:
[1] Kabir, HM Dipu, et al. "Uncertainty-aware decisions in cloud computing: Foundations and future directions." ACM Computing Surveys (CSUR) 54.4 (2021): 1-30.

[2] Smith, S. W. (1997). "Convolution," Chapter 6, The scientist and engineer's guide to digital signal processing.

[3] Kabir, HM Dipu, et al. "Partial adversarial training for neural network-based uncertainty quantification." IEEE Transactions on Emerging Topics in Computational Intelligence 5.4 (2019): 595-606.
