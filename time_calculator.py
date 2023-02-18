def add_time(start: str, duration: str, day_of_the_week: str = 'No') -> str:
    """
    Add the duration time to the start time and return the result.
    :param start: a start time in the 12-hour clock format (ex. "3:00 PM")
    :param duration: a duration time that indicates the number of hours and minutes (ex. "2:32")
    :param day_of_the_week: (optional) a starting day of the week, case-insensitive
    :return: the result of addition (ex. Returns: "12:03 PM", ex.2 "12:03 AM, Thursday (2 days later)")
    """

    DAYS_OF_THE_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    WEEK_LENGTH = 7
    TWELVE_FORMAT_MAX_H = 12
    TWENTY_FOR_FORMAT_MAX_H = 24
    MINUTES_IN_H = 60

    # Prepare the time data
    start_time = start.split()
    start_time[0] = start_time[0].split(':')
    addition_time_list = duration.split(':')

    start_h = int(start_time[0][0])
    start_m = int(start_time[0][1])
    meridiem = start_time[1]

    h_to_add = int(addition_time_list[0])
    m_to_add = int(addition_time_list[1])

    # Argument validation
    if meridiem != 'AM' and meridiem != 'PM':
        return 'Invalid meridiem'
    elif start_h > TWELVE_FORMAT_MAX_H or start_m > MINUTES_IN_H:
        return 'Invalid start timme'
    elif m_to_add > MINUTES_IN_H:
        return 'Invalid duration'

    # Time calculation
    if meridiem == 'AM':
        twenty_four_format_start_time_h = start_h
    else:
        twenty_four_format_start_time_h = start_h + TWELVE_FORMAT_MAX_H

    twenty_four_time_h_total = twenty_four_format_start_time_h + h_to_add + ((start_m + m_to_add) // MINUTES_IN_H)
    h_at_the_last_day = twenty_four_time_h_total % TWENTY_FOR_FORMAT_MAX_H
    new_h = h_at_the_last_day % TWELVE_FORMAT_MAX_H

    # Time normalization
    if new_h == 0:
        new_h = TWELVE_FORMAT_MAX_H
    new_m = (start_m + m_to_add) % MINUTES_IN_H

    if h_at_the_last_day < TWELVE_FORMAT_MAX_H:
        new_meridiem = 'AM'
    else:
        new_meridiem = 'PM'

    # Days calculation
    amount_of_passed_days = twenty_four_time_h_total // TWENTY_FOR_FORMAT_MAX_H
    days_passed_string = ''

    if amount_of_passed_days == 1:
        days_passed_string = ' (next day)'
    if amount_of_passed_days > 1:
        days_passed_string = f' ({amount_of_passed_days} days later)'

    if day_of_the_week != 'No':
        try:
            start_day_normalized = day_of_the_week.lower().capitalize()
            start_day_index = DAYS_OF_THE_WEEK.index(start_day_normalized)
        except ValueError:
            return 'Invalid Day of The Week'

        new_day_index = (start_day_index + amount_of_passed_days) % WEEK_LENGTH

        new_time = f'{new_h}:{new_m:02} {new_meridiem}, {DAYS_OF_THE_WEEK[new_day_index]}{days_passed_string}'

        return new_time

    else:
        new_time = f'{new_h}:{new_m:02} {new_meridiem}{days_passed_string}'
        return new_time
