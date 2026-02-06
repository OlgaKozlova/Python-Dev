from data.numbers import NUMBERS
from services.math_utils import multiply
from services.formatter import format_numbers
from config import DEBUG

result = multiply(NUMBERS)

if DEBUG:
    print("DEBUG:", result)

print(format_numbers(result))