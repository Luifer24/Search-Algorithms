target = int(input('Put you number: '))
epsilon = 0.01
down = 0.0
up = max(1.0, target)
answer = (down + up ) / 2 

while abs(answer**2 - target) >= epsilon:
    print(f'down={down}, up={up}, answer={answer}')
    if answer**2 < target:
        down = answer
    else:
        up = answer

    answer = (down + up) / 2

print(f'The square root of {target} is {answer}')
