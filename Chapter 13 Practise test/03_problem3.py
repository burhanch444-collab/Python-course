def divisibel5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 45, 63, 7863, 7364, 45]

f = list(filter(divisibel5, a))
print(f)
