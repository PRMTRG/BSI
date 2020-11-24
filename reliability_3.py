'''
Author: Tymoteusz Mirski

Excercise description:
An industrial machine compresses natural gas into an interstate gas pipeline. 
The compressor is on line 24 hours a day. (If the machine is down, a gas field
has to be shut down until the natural gas can be compressed, so down time is
very expensive.) The vendor knows that the compressor has a constant failure
rate of ______ failures/hr. What is the operational reliability after ______
hours of continuous service?
'''

import math

def calculate_operational_reliability(failure_rate, hours_of_service):
    exponent = -1 * failure_rate * hours_of_service
    result = math.exp(exponent)
    return result

def print_problem_description():
    print("An industrial machine compresses natural gas into an interstate gas pipeline. The compressor is on line 24 hours a day. (If the machine is down, a gas field has to be shut down until the natural gas can be compressed, so down time is very expensive.) The vendor knows that the compressor has a constant failure rate of ______ failures/hr. What is the operational reliability after ______ hours of continuous service?")

def run():
    print("Exercise 3 from file reliability.pdf:")
    print_problem_description()
    failure_rate = float(input("Enter the failure rate per hour: "))
    hours_of_service = float(input("Enter the number of hours of service: "))
    reliability = calculate_operational_reliability(failure_rate, hours_of_service)
    print()
    print(f'The calculated reliability is equal to {reliability:.4f} or {(reliability*100):.2f}%.')
    print()
