def decimal_to_binary(decimal):
    value = ''
    while decimal != 0:
        modulo = decimal % 2
        value = str(modulo) + value
        decimal //= 2
    return int(value)
