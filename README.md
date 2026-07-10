# Rent Calculator

A simple Python command-line program that calculates how much **each person** needs to pay when sharing rent, food, and electricity expenses in a hostel or flat.

## Features

- Takes total rent, food bill, and electricity bill as input.
- Splits the total expense equally among all persons sharing the flat/hostel.
- Displays the final amount each person needs to pay.

## Inputs Required

| Input | Description |
|---|---|
| `persons` | Number of people sharing the flat/hostel |
| `rent` | Total hostel/flat rent |
| `food` | Total food bill |
| `electricity` | Total electricity bill |
| `charge_per_unit` | Electricity charge per unit |

## Output

- **Total amount to be paid by each person**, calculated by splitting the combined expenses equally.

## How It Works

```python
total = rent + food + electricity + charge_per_unit
total_per_person = total / persons
```

1. All expenses (rent, food, electricity, charge per unit) are added together to get the `total`.
2. The `total` is divided by the number of `persons` to get each person's share.
3. The result is printed as the final amount to be paid.

## How to Run

1. Make sure Python 3 is installed.
2. Save the code as `rent_calculator.py`.
3. Run it from the terminal:

```bash
python rent_calculator.py
```

4. Enter the number of persons, rent, food bill, electricity bill, and charge per unit when prompted.

## Requirements

- Python 3.x
- No external libraries needed

## Example Usage

```
Enter the number of persons = 4
Enter your hostel/flat rent = 8000
Enter your food bill = 4000
Enter your electricity bill = 1200
Enter the charge per unit = 8
Total amount to be paid by each person is: 3302.0
```

## Known Limitation

Currently, `charge_per_unit` is directly added into the total along with the electricity bill, rather than being used to *calculate* the electricity bill (e.g. `units_consumed * charge_per_unit`). If you want the calculator to compute the electricity cost from units consumed, this logic can be updated — let me know if you'd like that fixed.

## Possible Future Improvements

- Calculate electricity bill as `units_consumed * charge_per_unit` instead of adding both directly.
- Allow unequal splitting (e.g. some persons pay more/less based on room type).
- Add option to save each month's split to a history file.
- Round the final amount to 2 decimal places for cleaner output.
- Add input validation (e.g. reject negative numbers or zero persons).

## Author

Built as a beginner Python project to practice input handling, basic arithmetic, and real-life expense-splitting logic.
