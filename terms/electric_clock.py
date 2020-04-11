# n - number of minutes from the start of the day
# return electric clock result
print('n - minutes')
print("m - hours")
n = int(input())
m = int(input())
print(str(n // 60) + ':' + (n % 60))
