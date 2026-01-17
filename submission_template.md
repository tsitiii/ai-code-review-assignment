# AI Code Review Assignment (Python)

## Candidate
- Name:
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The denominator uses len(orders), which counts all orders including cancelled ones. This produces an incorrect average.
- ZeroDivisionError can occur if the list is empty or all orders are cancelled.
- the function assumes 'amount' and 'status' keys always exist, but this might create a KeyError if those keys doesn't exist.


### Edge cases & risks
- Empty orders list → division by zero.
- All orders cancelled → division by zero.
- Orders missing 'amount' or 'status' keys → KeyError.
- Orders with 'amount' as non-numeric(e.g if string is given as amount value) → will give TypeError on addition.


### Code quality / design issues
- Input/output types not specified, reducing readability.
- Denominator counting all orders is misleading.
- No docstring or type hints to clarify expected input/output.
- we could use .get() to safely access keys and provide default values to avoid KeyError on the 'amount' and 'status' part.


## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only non-cancelled orders in the denominator.
- Add check to return 0 if count is zero.
- Use order.get() to safely access keys.
- Add type hints (orders: list[dict] -> float) for better readablity.
- Status is normalized to lowercase to avoid missing cancelled orders with different casing.
- 


### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Orders with 'amount' as a string number → converted to float correctly.
- Orders with invalid 'amount' (non-numeric) → skipped without crashing.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.
### Issues in original explanation
- it says cancelled orders are excluded, but denominator still counts them.
- Does not mention potential division by zero or input assumptions.
- No clarity on expected input/output


### Rewritten explanation
-This function calculates the average order value for all non-cancelled orders.
It sums the 'amount' of each order whose 'status' is not 'cancelled', converting
each amount to a float. Orders with non-numeric amounts are skipped. The function
divides by the number of valid non-cancelled orders, returning 0 if none exist.
Input is expected to be a list of dictionaries with 'status' and 'amount'.


## 4) Final Judgment
- Decision: Request Changes (for original) / Approve (for corrected code)
- Justification: Original code divides by all orders, causing inaccurate averages and possible division by zero. Corrected code handles non-cancelled orders correctly, avoids errors, and documents input/output.
- Confidence & unknowns: High confidence given the input assumptions; behavior is predictable with correctly formatted order dictionaries.


---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Original code does not check type, so non-string inputs (None, numbers, lists) will raise TypeError.

- Original code counts any string with "@" — multiple "@", missing local/domain parts, or domains without dots are incorrectly counted.

### Edge cases & risks
- Emails with multiple "@" → incorrectly counted as valid.

- Empty strings → counted as valid incorrectly if they contain "@".

- Missing local part ("@domain.com") → counted incorrectly.

- Missing domain part ("user@") → counted incorrectly.

- Domain without . ("user@localhost" or "w@c") → may not be a realistic email.

- Mixed types in input list → original code crashes.

### Code quality / design issues
- No type hints

- No docstring to explain input/output

- Assumes all inputs are strings → not safe for real-world data

- Simple "@" check is insufficient to capture minimal realistic email validity

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added type check to ensure only strings are processed.

- Require exactly one "@".

- Check that local and domain parts are non-empty.

- Require that domain contains at least one . for realistic public emails.


### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty list → should return 0.(Ensures the function correctly returns 0 without crashing.)

- All invalid strings (numbers, None, missing "@") → should return 0.(to ignore obviously invalid emails.)

- Mixed valid/invalid emails → only valid ones counted.

- Emails with multiple "@" → skipped.

- Emails with missing local or domain part → skipped.

- Emails with domain missing a dot → skipped.

- Normal valid emails ("user@example.com") → counted.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Overstates correctness : the original code does not safely ignore invalid entries; it crashes on non-string inputs.

- Simplistic "@" check is not sufficient to determine valid emails.

- Ignores edge cases like missing local/domain parts or domain without a dot.

### Rewritten explanation
- This function counts the number of valid email addresses in a list using a practical validation approach. email is considered valid if it is a string containing exactly one “@” symbol, with a non-empty local part before the “@” and a non-empty domain part after it that includes at least one dot. The function ignores non-string items, emails with multiple “@” symbols, missing local or domain parts, or domains without a dot. It safely handles empty lists and lists containing mixed types, and returns an integer representing the total number of valid emails.

## 4) Final Judgment
- Decision: Request Changes / Approve with Improvements

- Justification: The original code does not safely handle non-strings, missing parts, multiple "@", or domains without a dot. Minimal improvements are needed to ensure correct counting.

- Confidence & unknowns: High confidence

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
