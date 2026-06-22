gender = input(
    'What is your gender?\n'
    ' [M] Male\n'
    ' [F] Female\n'
).strip().upper()[0]

while gender not in 'MF':
    gender = input(
        'Invalid input. Please try again:\n'
    ).strip().upper()[0]

if gender == 'M':
    print('Male gender successfully registered!')
elif gender == 'F':
    print('Female gender successfully registered!')
