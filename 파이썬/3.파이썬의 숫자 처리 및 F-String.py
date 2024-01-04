print(round(8 / 3, 2)) # round(숫자, 소수점 자리수) = 소수점 자리수까지 반올림

print(8 // 3) # // = 몫만 출력

result = 4 / 2
result /= 2 # /= = result = result / 2

print(int(result))

score = 0

# User scores a point
score += 1 # += = score = score + 1

print(score)

# f-String
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}") # f-String = {}안에 변수를 넣어서 출력