def calculator(expression):
    allowed_signs = '+-/*'
    if not any(sign in expression for sign in allowed_signs):
        raise ValueError('Must contain at least one of the allowed signs')
    for sign in allowed_signs:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left,right)
            except (ValueError, TypeError):
                raise ValueError('The expression must contain two integers and one sign')


if __name__ == '__main__':
    print(calculator('6/2'))
