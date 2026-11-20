def average(numbers):
    """Return the average of numbers, or 0 if empty."""
    return sum(numbers) / len(numbers) if numbers else 0


def first_word(text):
    """Return the first word, or empty string if none."""
    return text.split()[0] if text.strip() else ""


def percent(part, total):
    """Return percentage, or 0 if total is zero."""
    return part / total * 100 if total != 0 else 0
