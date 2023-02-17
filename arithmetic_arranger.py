def arithmetic_arranger(problems: list, answers_display: bool = False) -> str:
    """
    Return a vertically arranged arithmetic problems (+ or -) with or without answer (depends on answer_display param).
    @param problems: list of arithmetic problems (ex. "["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]". Less than
    5 items in a list.
    @param answers_display: True - answers will be displayed, False - answers will not be displayed
    @return: str. Vertically arranged arithmetic problems
    """
    OFFSET_FOR_OPERATOR = 2
    SPACE_BETWEEN_VERTICAL_PROBLEMS = '    '
    PROBLEM_LINE_SYMBOL = '-'
    problems_by_rows = ['', '', '', '']
    amount_of_problems = len(problems)
    problems_columns_width = {}

    # TEST | Less than 5 problems
    if amount_of_problems > 5:
        return "Error: Too many problems."

    for problem_index in range(amount_of_problems):
        problems[problem_index] = problems[problem_index].split()
        first_operand = problems[problem_index][0]
        second_operand = problems[problem_index][2]
        operation = problems[problem_index][1]
        problems_columns_width[problem_index] = max(len(first_operand), len(second_operand))

        # TEST | Only addition and subtraction
        if operation != '+' and operation != '-':
            return "Error: Operator must be '+' or '-'."

        # TEST | Only digit allowed
        elif not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."

        # TEST | Number must be < 5 digits
        elif problems_columns_width[problem_index] > 4:
            return "Error: Numbers cannot be more than four digits."

        problems_by_rows[0] += (first_operand.rjust(problems_columns_width[problem_index] + OFFSET_FOR_OPERATOR)
                                + SPACE_BETWEEN_VERTICAL_PROBLEMS)

        problems_by_rows[1] += (operation.ljust(OFFSET_FOR_OPERATOR)
                                + second_operand.rjust(problems_columns_width[problem_index])
                                + SPACE_BETWEEN_VERTICAL_PROBLEMS)

        problems_by_rows[2] += (''.center(problems_columns_width[problem_index]
                                          + OFFSET_FOR_OPERATOR, PROBLEM_LINE_SYMBOL)
                                + SPACE_BETWEEN_VERTICAL_PROBLEMS)

        problems_by_rows[3] += str(eval(first_operand + operation + second_operand)).rjust(
            problems_columns_width[problem_index] + OFFSET_FOR_OPERATOR) + SPACE_BETWEEN_VERTICAL_PROBLEMS

    for row_number, row_value in enumerate(problems_by_rows):
        problems_by_rows[row_number] = problems_by_rows[row_number].rstrip()

    if not answers_display:
        arranged_problems = '\n'.join((problems_by_rows[0], problems_by_rows[1],
                                       problems_by_rows[2]))

    elif answers_display:
        arranged_problems = '\n'.join((problems_by_rows[0], problems_by_rows[1],
                                       problems_by_rows[2], problems_by_rows[3]))
    else:
        return "Error: answers_display param should be bool (True or False)"

    return arranged_problems
