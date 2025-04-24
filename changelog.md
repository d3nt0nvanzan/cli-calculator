# Changelog

## [0.0.1] - 2025-04-24 

### Fixed
- **Alphabetic Input Handling bug**:
  -Fixed issue where alphabetic input (e.g., "abc") for 'firstNumber' or 'secondNumber' caused the program to exit or reset operation.
  - Updated 'main.py' input loops to:
    - Capture input as 'user_input' (string).
    - Checkfor alphabetic characters with 'if any(c.isalpha() for c in user_input)'.
    - Convert to 'Decimal' only if valid.
  - New approach applies input validation on the string first, ensuring robust re-prompting without disrupting operaiton.
