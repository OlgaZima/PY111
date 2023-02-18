def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    # TODO реализовать проверку скобочной группы

    if not isinstance(brackets_row, str):
        raise TypeError()

    stack_ = 0
    for i in range(len(brackets_row)):
        if brackets_row[0] == ")":
            return False
            break
        elif brackets_row[i] == "(":
            stack_ += 1
        elif brackets_row[i] == ")":
            stack_ -= 1
    if stack_ == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
