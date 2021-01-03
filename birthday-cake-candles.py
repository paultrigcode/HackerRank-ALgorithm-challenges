def birthdayCakeCandles(candles):
    # Write your code here
    maxi = 0
    counter = 0
    for i in candles:
        if i>maxi :
            maxi = i
            counter = 1
        elif i == maxi :
           counter += 1
    return counter

print(birthdayCakeCandles([3,3,4,2,1,4,2,4]))
