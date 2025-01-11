This repository demonstrates a common yet often overlooked error in recursive functions: the RecursionError. The `factorial` function, while seemingly simple, lacks a base case for negative numbers, leading to infinite recursion.  The solution implements appropriate error handling to gracefully manage invalid inputs.