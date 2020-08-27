target = int(input('Select a number: '))
epsilon = 0.01
step = epsilon**2
answer = 0.0

while abs(answer**2 - target) >= epsilon and answer <= target:
    print(abs(answer**2 - target), answer)
    answer += step

if abs(answer**2 - target) >= epsilon:
    print(f'Not found the square root of {target}')
else:
    print(f'The square root of {target} is {answer}')