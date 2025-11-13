import random
import sys

def generate_no() -> int:
    """Generates the secret number between 1 and 100."""
    return random.randint(1, 100)