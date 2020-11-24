def problem_desc():
    print("Exercise 2:")
    print("If 300 of these chips are used in building a mainframe computer, how many failures of the computer can be expected per month?")
    print()

def getFrN(tested, time, failed):
    total_time = tested*time
    downtime = 0
    len = int(input("Select len of array: "))
    for i in range(0, len):
        x = int(input("Attempts: "))
        y = int(input("Time per attempt: "))
        downtime += x * (time - y)
    operating_time = total_time - downtime
    result = failed/operating_time
    return result

def convert(fN):
    return fN * 24 * 30

def run():
    failed = int(input("Enter failures: "))
    tested = int(input("Enter number tested: "))
    time = int(input("Enter time: "))
    failures_monthly = convert(getFrN(tested,time,failed))
    result3 = failures_monthly * tested
    problem_desc()
    print("----Results----")
    print("Failures per month: ", failures_monthly)
    print("FR(N): ", result3)
    print("----Results----")

# EXAMPLE USAGE:
# Enter failures: 6
# Enter number tested: 300
# Enter time: 500
# Select len of array: 4
# Attempts: 2
# Time per attempt: 50
# Attempts: 2
# Time per attempt: 100
# Attempts: 1
# Time per attempt: 300
# Attempts: 1
# Time per attempt: 400
# Exercise 2:
# If 300 of these chips are used in building a mainframe computer, how many failures of the computer can be expected per month?
#
# ----Results----
# Failures per month:  0.02918918918918919
# FR(N):  8.756756756756756
# ----Results----
