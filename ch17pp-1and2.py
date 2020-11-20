def problem_desc():
    print("Exercise 1:")
    print('California Instruments, Inc., produces 3,000 computer chips per day.')
    print('Three hundred are tested for a period of 500 operating hours each.')
    print('During the test, six failed: two after 50 hours, two at 100 hours, one at 300 hours, and one at 400 hours.')
    print('Find FR(%) and FR(N).')
    print()
    print("Exercise 2:")
    print("If 300 of these chips are used in building a mainframe computer, how many failures of the computer can be expected per month?")
    print()


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


def convert(fN):
    return fN * 24 * 30

#Exercise 1:
problem_desc()
failed = int(input("Enter failures: "))
tested = int(input("Enter number tested: "))
time = int(input("Enter time: "))
result1 = getFrPercent(failed, tested)
result2 = getFrN(tested, time, failed)

# Exercise 2:
failures_monthly = convert(result2)
result3 = failures_monthly * tested

print("----Results----")
print("Exercise 1:")
print("Failures per number tested: ",result1)
print("failures per operating time: ",result2)
print("Exercise 2:")
print("Failures per month: ", failures_monthly)
print("FR(N): ", result3)
print("----Results----")

#Example Usage:
# Exercise 1:
# California Instruments, Inc., produces 3,000 computer chips per day.
# Three hundred are tested for a period of 500 operating hours each.
# During the test, six failed: two after 50 hours, two at 100 hours, one at 300 hours, and one at 400 hours.
# Find FR(%) and FR(N).
#
# Exercise 2:
# If 300 of these chips are used in building a mainframe computer, how many failures of the computer can be expected per month?
#
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
# Exercise 1:
# Failures per number tested:  0.02
# failures per operating time:  4.054054054054054e-05
# Exercise 2:
# Failures per month:  0.02918918918918919
# FR(N):  8.756756756756756
# ----Results----
