X = int(input('Aチームの得点:'))
Y = int(input('Bチームの得点:'))

X_a = X + 5
Y_b = Y + 5

if X > Y and X < Y_b:
    print('Yes')
elif X < Y and X_a > Y:
    print('Yes')
else:
    print('No')
    