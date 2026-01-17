# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
def count_valid_emails(emails: list) -> int:
    """
    email is considered valid if:
    - it is a string
    - contains exactly one '@'
    - local part (string before '@') is not empty
    - domain part (string after '@') is not empty and contains at least one '.'

    """
    count = 0

    for email in emails:
        if isinstance(email, str) and email.count("@") == 1:
            local, domain = email.split("@")
            if local and domain and "." in domain:
                count += 1

    return count

