def multi_bracket_validation(input):
    curly = 0
    square = 0
    parens = 0
    lst1 = []
    lst1[:0] = input
    for i in lst1:
        if i == "{":
            curly += 1
        if i == "}":
            curly -= 1
            if curly < 0:
                return False
        if i == "[":
            square += 1
        if i == "]":
            square -= 1
            if square < 0:
                return False
        if i == "(":
            parens += 1
        if i == ")":
            parens -= 1
            if parens < 0:
                return False
    if curly or parens or square != 0:
        return False
    else:
        return True
