"""
Functionality to calculate day of week.
"""
import re

DATE_REG_EXP = '^([0-9]{4}[-/]?((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00)[-/]?02[-/]?29)$'
MONTH_CUM_SUM_DAYS = {
    1: 0,
    2: 31,
    3: 59,
    4: 90,
    5: 120,
    6: 151,
    7: 181,
    8: 212,
    9: 243,
    10: 273,
    11: 304,
    12: 334,
}
WEEKDAYS = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}


def calc_weekday(date_str):
    """
    Calculate day of week based on provided date string.

    Arguments:
        date_str (str): provided date in "YYYY-mm-dd" format.

    Returns:
        week day name as a string.
    """
    _validate(date_str=date_str)

    year = int(date_str[:4])
    month = int(date_str[5:7])
    day = int(date_str[8:])

    num_years_before = year - 1
    num_leap_years_days = calc_num_leap_years_before(year=year, month=month)
    current_year_days = MONTH_CUM_SUM_DAYS.get(month) + (day - 1)

    prev_days = num_years_before + + num_leap_years_days + current_year_days

    weekday = WEEKDAYS.get(prev_days % 7)

    return weekday


class InvalidArgumentError(Exception):
    """
    Invalid argument error implementation.
    """

    def __init__(self):
        """
        Construct the object.
        """
        self.message = 'The provided arguments do not comply restrictions. Value should be in format "YYYY-mm-dd".'

    def __str__(self):
        """
        Define string representation.

        Returns:
            Error message as a string
        """
        return self.message


def _validate(date_str):
    """
    Validate input date string.

    Arguments:
        date_str (str): provided date.

    Raises:
        InvalidArgumentError: when provided string is not a real date or do not comply format restrictions.
    """
    if not re.match(DATE_REG_EXP, date_str):
        raise InvalidArgumentError()


def _is_leap_year(year):
    """
    Check whether provided year is leap or not.

    Arguments:
        year (int): specified year.

    Returns:
        boolean identifier whether provided year is leap or not.
    """
    if (year % 4) > 0:
        return False

    if (year % 100) > 0:
        return True

    if (year % 400) == 0:
        return True

    else:
        return False


def calc_num_leap_years_before(year, month):
    """
    Calculate number of 29th February dates happened before specified date.

    Arguments:
        year (int): specified year.
        month (int): specified month.

    Returns:
        number of 29th February dates happened before specified date as an integer.
    """
    num_leap_years = year // 4 - year // 100 + year // 400

    if _is_leap_year(year):
        if month < 3:
            num_leap_years = num_leap_years - 1  # 29th of February not happened on provided leap year.

    return num_leap_years
