# Gender Input Validator

A beginner-friendly Python project that validates user input by accepting only predefined gender options. The program continues prompting the user until a valid choice is entered.

## Features

- Accepts gender input from the user
- Removes extra spaces automatically
- Converts input to uppercase
- Reads only the first character entered
- Validates the input using a loop
- Prevents invalid values from being accepted

## Technologies Used

- Python 3

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/gender-input-validator.git
```

2. Navigate to the project folder:

```bash
cd gender-input-validator
```

3. Run the script:

```bash
python main.py
```

## Example

### Input

```text
What is your gender?

[M] Male
[F] Female

x
```

### Output

```text
Invalid input. Please try again:
```

### Valid Input

```text
M
```

### Output

```text
Male gender successfully registered!
```

## Learning Objectives

This project demonstrates:

- User input handling
- String manipulation
- Input validation
- `while` loops
- Membership operators (`in` and `not in`)
- Data sanitization

## Key Concepts

### Removing Spaces

```python
gender.strip()
```

Removes spaces from the beginning and end of the input.

### Converting to Uppercase

```python
gender.upper()
```

Makes input validation easier.

### Reading Only the First Character

```python
gender[0]
```

Allows inputs such as:

```text
Male
M
male
m
```

to be treated the same way.

### Input Validation

```python
while gender not in 'MF':
```

Keeps asking until a valid option is entered.
