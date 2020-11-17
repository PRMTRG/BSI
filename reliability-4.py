import numpy as np

def calculate_highest_failure_rate(reliability, hours):
    log = np.log(reliability)
    result = log / hours * -1
    return result

def print_problem_description():
    print("What is the highest failure rate for a product if it is to have a reliability (or probability of survival) of ______ percent at ______ hours?  Assume that the time to failure follows an exponential distribution.")

def run():
    print("Exercise 4 from file reliability.pdf:")
    print_problem_description()
    reliability = float(input("Enter the reliability: "))
    hours = float(input("Enter the number of hours: "))
    highest_failure_rate = calculate_highest_failure_rate(reliability, hours)
    print()
    print(f'The failure rate must be no higher than {highest_failure_rate:.8f} (failures per hour).')

run()
