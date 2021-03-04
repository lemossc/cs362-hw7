FIRST_LEAP_YEAR = 1582  # First year leap year rules were introduced by the Gregorian Calendar


def is_leap_year(year):
    # Validate input
    if not isinstance(year, int) or year < FIRST_LEAP_YEAR:
        return None
    # Determine whether year is a leap year -- assume common
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True

    return False
