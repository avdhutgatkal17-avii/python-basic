#Nearest Multiple of 10

def roundToNearest(s: str) -> int:
    last_digit = int(s[-1])

    if last_digit <= 5:
        result = s[:-1] + "0"
    else:
        digits = list(s[:-1])
        i = len(digits) - 1

        while i >= 0 and digits[i] == '9':
            digits[i] = '0'
            i -= 1

        if i < 0:
            result = '1' + ''.join(digits) + '0'
        else:
            digits[i] = str(int(digits[i]) + 1)
            result = ''.join(digits) + '0'

    result = result.lstrip('0') or '0'
    return int(result)
