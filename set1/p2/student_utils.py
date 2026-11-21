
# Full Name: Jessie B. Maralit
# Section: IV-BSIT A
# Activity: P2 - Custom Module
# Date: November 21, 2026


def average(grades):
    return sum(grades) / len(grades)


def status(grades):
    if average(grades) >= 75:
        return "PASSED"
    return "FAILED"


def highest(grades):
    return max(grades)


def lowest(grades):
    return min(grades)