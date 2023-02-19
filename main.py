# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)

# Run unit tests automatically
main(module='test_module', exit=False)
