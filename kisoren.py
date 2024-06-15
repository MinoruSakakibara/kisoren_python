# 01. Creates a function that takes two numbers as arguments and return their sum.
def addition(a, b):
    add = a + b
    return add

print(addition(10, 20)) # 30
print(addition(30, 20)) # 50
print(addition(10, 90)) # 100

# 02.Converts hours into seconds.
def howManySeconds(hours):
    hoursToSeconds = hours * 3600
    return hoursToSeconds

print(howManySeconds(12)) # 43200
print(howManySeconds(8)) # 28800
print(howManySeconds(3)) # 10800

# 03. Converts minutes into seconds.
def convert(minutes):
    second = minutes * 60
    return second

print(convert(30)) # 1800
print(convert(10)) # 600
print(convert(20)) # 1200

# 04.Calculates total points of a team from number of wins(3pts), draws(1pt), and losses(0pt).
def footballPoints(wins, draws, losses):
    points = wins * 3 + draws * 1 + losses * 0
    return points

print(footballPoints(4, 3, 1)) # 15
print(footballPoints(10, 5, 0)) # 35
print(footballPoints(11, 0, 9)) # 33

# 05. Write functions to calculate the bitwise AND, bitwise OR and bitwise XOR of two numbers.
def bitwiseAND(n1, n2):
    answer = n1 & n2
    return answer

def bitwiseOR(n1, n2):
    answer = n1 | n2
    return answer

def bitwiseXOR(n1, n2):
    answer = n1 ^ n2
    return answer

print(bitwiseAND(10, 20)) # 0
print(bitwiseOR(10, 20)) # 30
print(bitwiseXOR(10, 20)) # 30

# 06. Write Function to return first value of an array.
def getFirstValue(arr):
    return arr[0]

print(getFirstValue(["Saab", "Volvo", "BMW"])) # Saab
print(getFirstValue([3, 5, 1])) # 3
print(getFirstValue(['hello', 'world', 'welcome'])) # hello

# 07.Create a function that takes a number as an argument, increments the number by +1 and returns the result.
def addition(num):
    numPlusOne = num + 1
    return(numPlusOne)

print(addition(5)) # 6
print(addition(100)) # 101
print(addition(99)) # 100

# 08. Given two numbers, return true if the sum of both numbers is less than 100. Otherwise return false.
def lessThan100(a, b):
    if (a + b < 100):
        return True
    else:
        return False
    
print(lessThan100(10, 20)) # True
print(lessThan100(50, 60)) # False
print(lessThan100(20, 50)) # True

# 09. Create a function that returns true when num1 is equal to num2; otherwise return false.
def isSameNum(num1, num2):
    if (num1 == num2):
        return True
    else:
        return False
    
print(isSameNum(30, 30)) # True
print(isSameNum(20, 40)) # False
print(isSameNum(50, 50)) # True

# 10. Create a function that takes a number (step) as an argument and returns the amount of matchsticks in that step.
def matchHouses(step):
    if (step > 1):
        matchSticks = ((step * 6) - (step - 1))
        return matchSticks
    elif (step == 1):
        matchSticks = step * 6
        return matchSticks
    else:
        matchSticks = 0
        return matchSticks

print(matchHouses(5)) # 26
print(matchHouses(0)) # 0
print(matchHouses(1)) # 6

# 11. Write function to return the square of a number.
def squared(a):
    return(a * a)

print(squared(6)) # 36
print(squared(9)) # 81
print(squared(4)) # 16

# 12.Write function to calculate Perimeter of Rectangles
def findPerimeter(height, width):
    primeter = (height + width) * 2
    return primeter

print(findPerimeter(20, 50)) # 140
print(findPerimeter(80, 30)) # 220
print(findPerimeter(10, 40)) # 100

# 13. Add up all the numbers from 1 to the number you passed to the function.
def addUp(num):
    i = 0
    sum = 0
    while i <= num:
        sum += i
        i += 1
    return sum
    
print(addUp(10)) # 55
print(addUp(40)) # 820
print(addUp(15)) # 120

# 13'. Add up all the numbers from 1 to the number you passed to the function.
def addUp(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum
    
print(addUp(10)) # 55
print(addUp(40)) # 820
print(addUp(15)) # 120