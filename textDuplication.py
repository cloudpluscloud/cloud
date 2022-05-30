def PrintABTimes(a, b):
    ret = ""
    for i in range (b):
        ret += a
    return ret

a = str(input('Enter text to duplicate: '))
b = int(input('Enter how many times to duplicate: '))

print(PrintABTimes(a, b))