import math

def main(n, m, b, y):

    x = 0
    z = 0

    for k in range(1, m+1):
        for j in range(1, n+1):
            x = x + (pow(72 * pow(j, 3) - k - 46, 4))
    for i in range(1, n+1):
        for c in range(1, b+1):
            z = z + (66 * c + pow(math.sin(i), 4) + pow(1 + pow(y, 2), 7))
    answ = x + z
    return answ

if __name__ == '__main__':
    print(main(6, 4, 8, 0.68))
