# Q1. Creates a function that takes two numbers as arguments and return their sum.
def addition(a, b):
    add = a + b
    return add

print(addition(10, 20)) # 30
print(addition(30, 20)) # 50
print(addition(10, 90)) # 100

# Q2.Converts hours into seconds.
def howManySeconds(hours):
    hoursToSeconds = hours * 3600
    return hoursToSeconds

print(howManySeconds(12)) # 43200
print(howManySeconds(8)) # 28800
print(howManySeconds(3)) # 10800

# Q3. Converts minutes into seconds.
def convert(minutes):
    second = minutes * 60
    return second

print(convert(30)) # 1800
print(convert(10)) # 600
print(convert(20)) # 1200

# Q4.Calculates total points of a team from number of wins(3pts), draws(1pt), and losses(0pt).
def footballPoints(wins, draws, losses):
    points = wins * 3 + draws * 1 + losses * 0
    return points

print(footballPoints(4, 3, 1)) # 15
print(footballPoints(10, 5, 0)) # 35
print(footballPoints(11, 0, 9)) # 33

# Q5. Write functions to calculate the bitwise AND, bitwise OR and bitwise XOR of two numbers.
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

# Q6. Write Function to return first value of an array.
def getFirstValue(arr):
    return arr[0]

print(getFirstValue(["Saab", "Volvo", "BMW"])) # Saab
print(getFirstValue([3, 5, 1])) # 3
print(getFirstValue(['hello', 'world', 'welcome'])) # hello

# Q7.Create a function that takes a number as an argument, increments the number by +1 and returns the result.
def addition(num):
    numPlusOne = num + 1
    return(numPlusOne)

print(addition(5)) # 6
print(addition(100)) # 101
print(addition(99)) # 100