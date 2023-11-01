import math
from texttable import Texttable


# Function to compute the sum of the series
def series_of_sum_numerically(n):
    """
    This function computes the sum of the series numerically in its original form

    Args:
        n (int): The number of terms to be considered

    Returns:
        float: The sum of the series
    """
    sum = 0
    for i in range(1, n+1):
        sum += ((-1)**(i+1))/i
    return sum


# Function to compute the rearranged sum
def sum_segment(p, q, left_off_positive, left_off_negative):
    """
    This function computes the sum of the series in the rearranged form

    Args:
        p (int): The number of positive terms for each iteration
        q (int): The number of negative terms for each iteration
        left_off_positive (int): Shows Where the sum was left off for the positive terms
        left_off_negative (int): Shows Where the sum was left off for the negative terms

    Returns:
        float, int, int: The sum of the series in the rearranged order, The last positive term and the last negative term considered in the sum
    """

    sum_p_positive = 0
    for i in range(left_off_positive, left_off_positive + 2*p - 1, 2):
        sum_p_positive += ((-1)**(i+1))/i
    left_off_positive += 2*p


    sum_q_negative = 0
    for i in range(left_off_negative, left_off_negative+ 2*q - 1, 2):
        sum_q_negative += ((-1)**(i+1))/i
    left_off_negative += 2*q
    return sum_p_positive + sum_q_negative, left_off_positive, left_off_negative


def rearranged_sum(n, p, q):
    left_off_positive = 1
    left_off_negative = 2
    total_sum = 0
    while left_off_negative <= n and left_off_positive <= n:
        partial_sum = 0
        partial_sum, pos_temp, neg_temp = sum_segment(p, q, left_off_positive, left_off_negative)
        total_sum += partial_sum
        left_off_positive = pos_temp
        left_off_negative = neg_temp

    return total_sum

def main():
    n = int(input("Please enter the number of terms: "))
    p = int(input("Please no of p positive terms: "))
    q = int(input("Please enter no of q negative terms: "))

    table = Texttable()
    table.add_rows([["n", "ln 2", "Sum of the series", "Rearranged sum"], [n, f"~{math.log(2)}", f"~{series_of_sum_numerically(n)}", f"~{rearranged_sum(n, p, q)}"]])
    print(table.draw())

main()

