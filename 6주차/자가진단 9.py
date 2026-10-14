password = input()

pattern = input()

repeated_pattern = pattern * 5

if password in repeated_pattern:
    print('YES')
else:
    print('NO')
