def phpneLetter(digits):
    if not digits:
        return []
    keyboard = {
       "2":'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
    a = []
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return keyboard[digits]
    restult = phpneLetter(digits[1:])
    for i in restult:
        for j in keyboard[digits[0]]:
            a.append((j+i))

    return a

print(phpneLetter('22'))