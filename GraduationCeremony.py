'''
In a university, your attendance determines whether you will be allowed
to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
'''


def graduation(n):
    """
    Main function which contains solution to the above problem.
    """
    count = 0
    missed_graduation = 0

    # Generate all combinations of attendance for N days.
    distribution = generate_binary_numbers(n)

    for x in distribution:
        print(x)
        # Check if student is not absent for 4 days consecutively.
        if "0000" not in x:
            count += 1
            # Check if student is absent on last day (graduation day).
            if x[-1] == '0':
                missed_graduation += 1

    return count, (missed_graduation/count)


def generate_binary_numbers(n):
    """
    Generate all the binary numbers of lenght N.
    """

    max_int = '0b' + '1' * n

    for i in range(0, int(max_int, 2)+1, 1):
        yield str(format(i, 'b').zfill(n))


ans1, ans2 = graduation(4)

print("The number of ways to attend classes over N days is {}".format(ans1))
print("The probability that you will miss your graduation ceremony is {}".
      format(ans2))
