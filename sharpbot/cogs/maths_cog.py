import tags
import math


@tags.tag('maths')
def fibi(self, total):
    """
    Gives the first n terms of the fibonacci sequence.
    """

    total = int(total)
    if total > 200:
        total = 200
    numbers = [1, 1]
    for i in range(1, total):
        numbers.append(numbers[-2] + numbers[-1])
        i += 1
    self.message(str(numbers[:-1]))


@tags.tag('maths')
def primes(self, total=10):
    """
    Get the first n prime numbers.
    """

    total = int(total)
    primesC = []
    check = [2]
    for item in range(1, total):
        if item == 2:
            primesC.append(item)
        if item > 1:
            if any(item % x for x in (2, 3, 5, 7, 11, 13)):
                for x in check:
                    if item % x == 0:
                        break
                else:
                    check.append(item)
                    primesC.append(item)

    self.message(primesC)


@tags.tag('maths')
def fizzbuzz(self, total=0, number1=3, number2=5):
    """
    Get the first n numbers of the Fizzbuzz problem.
    """

    total = int(total)
    if total < 0 or total > 100:
        total = 50
    number1 = int(number1)
    number2 = int(number2)
    buzzes = []
    for item in range(0, total):
        if item % number1 == 0 and item % number2 == 0:
            buzzes.append('Fizzbuzz')
        elif item % number1 == 0:
            buzzes.append('Fizz')
        elif item % number2 == 0:
            buzzes.append('Buzz')
        else:
            buzzes.append(item)

    self.message(str(buzzes))


@tags.tag('maths')
def area(self, shape, *args):
    """
    Find the area of a shape.
    """

    if shape.lower() == "rectangle":
        answer = int(args[0]) * int(args[1])
        self.message(answer)
        return

    if shape.lower() == "triangle":
        answer = 0.5 * int(args[0]) * int(args[1])
        self.message(answer)
        return

    if shape.lower() == "trapezoid":
        answer = (int(args[0]) + int(args[1])) / 2 * int(args[2])
        self.message(answer)
        return

    if shape.lower() == "circle":
        answer = math.sqrt(int(args[0])) * math.pi
        self.message(answer)
        return

    else:
        self.message(
            "Possible shapes are: Rectangle, Triangle, Trapezoid and Circle.")


@tags.tag('maths')
def log(self, base, total):
    """
    Get the log of a base to its solution.
    """

    answer = math.log(int(total), int(base))
    self.message(answer)


@tags.tag('maths')
def linear(self, *args):
    """
    Give this 2 cordinates and it give's the linear equation.
    """
    cord1x, cord1y = args[0].strip('()').split(',')
    cord2x, cord2y = args[1].strip('()').split(',')
    cord1x, cord1y, cord2x, cord2y = map(int, (cord1x, cord1y, cord2x, cord2y))

    gradient = (cord2y - cord1y) / (cord2x - cord1x)

    final = "y = {}x + {}"

    self.message(final.format(gradient, (gradient * cord1x) + cord1y))
