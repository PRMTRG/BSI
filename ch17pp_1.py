def problem_desc():
    print("Exercise 1:")
    print('California Instruments, Inc., produces 3,000 computer chips per day.')
    print('Three hundred are tested for a period of 500 operating hours each.')
    print('During the test, six failed: two after 50 hours, two at 100 hours, one at 300 hours, and one at 400 hours.')
    print('Find FR(%) and FR(N).')


# FR(%) = failures per number tested
def getFrPercent(fails,tested):
    return fails/tested


# FR(N) = failures per operating time:
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

def run():
    problem_desc()
    failed = int(input("Enter failures: "))
    tested = int(input("Enter number tested: "))
    time = int(input("Enter time: "))
    result1 = getFrPercent(failed, tested)
    result2 = getFrN(tested, time, failed)
    print("----Results----")
    print("Failures per number tested: ", result1)
    print("failures per operating time: ", result2)

# EXAMPLE RUN:
# Exercise 1:
# California Instruments, Inc., produces 3,000 computer chips per day.
# Three hundred are tested for a period of 500 operating hours each.
# During the test, six failed: two after 50 hours, two at 100 hours, one at 300 hours, and one at 400 hours.
# Find FR(%) and FR(N).
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
# ----Results----
# Failures per number tested:  0.02
# failures per operating time:  4.054054054054054e-05