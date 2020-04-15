def collatz(number):
    """Collatz sequence function to have the input evaluate to 1"""
    if number > 1:
        steps = 0
        while number != 1:
            if number % 2 == 0:
                print(number // 2)
                number = number // 2
                steps += 1
            elif number % 2 == 1:
                print(3 * number + 1)
                number = 3 * number + 1
                steps += 1
        print("Collatz sequence completed in " + str(steps) + " iterations to achieve a final value of 1.")

try:
    n = input("Enter a number: \n")
    n = collatz(int(n))
except ValueError:
    print('You must enter an integer data type.')

