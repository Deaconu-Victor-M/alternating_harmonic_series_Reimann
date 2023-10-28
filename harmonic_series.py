import math
from colorama import Fore, Back, Style, just_fix_windows_console
from texttable import Texttable

just_fix_windows_console()

# Function to compute the sum of the series
def series_of_sum_numerically(n):
    sum = 0
    for i in range(1, n+1):
        sum += ((-1)**(i+1))/i
    return sum

# Function to compute the rearranged sum
def rearranging_sum(p, q, left_off_positive, left_off_negative):

    sum_p_positive = 0
    # print(Fore.BLUE + "Positive terms: ")
    for i in range(left_off_positive, left_off_positive + 2*p - 1, 2):
        sum_p_positive += ((-1)**(i+1))/i
        # print(Fore.BLUE + f"-1^{i+1}/{i}", end= " " + Fore.WHITE)
    left_off_positive += 2*p
    # print("")


    sum_q_negative = 0
    # print(Fore.RED + "Negative terms: ")
    for i in range(left_off_negative, left_off_negative+ 2*q - 1, 2):
        sum_q_negative += ((-1)**(i+1))/i
        # print(Fore.RED + f"-1^{i+1}/{i}", end= " " + Fore.WHITE)
    left_off_negative += 2*q
    # print("")
    return sum_p_positive + sum_q_negative, left_off_positive, left_off_negative


def rearranged_sum(n, p, q):
    left_off_positive = 1
    left_off_negative = 2
    total_sum = 0
    while left_off_negative <= n and left_off_positive <= n:
        partial_sum = 0
        partial_sum, pos_temp, neg_temp = rearranging_sum(p, q, left_off_positive, left_off_negative)
        total_sum += partial_sum
        # print(pos_temp, neg_temp)
        left_off_positive = pos_temp
        left_off_negative = neg_temp

    return total_sum

def main():
    n = int(input("Please enter the number of terms: "))
    p = int(input("Please no of p positive terms: "))
    q = int(input("Please enter no of q negative terms: "))

    table = Texttable()
    table.add_rows([["n", "Sum of the series", "ln 2", "Rearranged sum"], [n, f"~{series_of_sum_numerically(n)}", f"~{math.log(2)}", f"~{rearranged_sum(n, p, q)}"]])
    print(table.draw())

main()

