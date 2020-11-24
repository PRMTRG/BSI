'''
Author: Tymoteusz Mirski

Excercise description:
Suppose that a component we wish to model has a constant failure rate with a
mean time between failures of ______ hours? Find:
(a) The reliability function.
(b) The reliability of the item at ______ hours.
'''

import math

def calculate_reliability(mtbf):
    reliability = 1/mtbf
    return reliability

def print_reliability_function(reliability):
    print(f'The reliability function: R(t) = e^(-({reliability} * t))')
    
def print_reliability_at_x_hours(reliability, hours):
    exponent = -1 * reliability * hours
    result = math.exp(exponent)
    print(f'The reliability of the item at {hours} hours is {result:.4f}.')

def print_problem_description():
    print("Suppose that a component we wish to model has a constant failure rate with a mean time between failures of ______ hours? Find:")
    print("(a) The reliability function.")
    print("(b) The reliability of the item at ______ hours.")
    
def run():
    print("Exercise 5 from file reliability.pdf:")
    print_problem_description()
    mtbf = float(input("Enter the mean time between failures (in hours): "))
    hours = float(input("Enter the number of hours: "))
    reliability = calculate_reliability(mtbf)
    print()
    print_reliability_function(reliability)
    print_reliability_at_x_hours(reliability, hours)
    print()
