from functools import reduce

def linearGenerator(seed, m, a, c, n):
    # a: multiplicador
    # m: modulo
    # c: corrimiento
    # n: cantidad de numeros a generar

    randomNums = [0] * n
    randomNums[0] = seed

    for i in range(1, n):
        randomNums[i] = ((randomNums[i - 1] * a) + c) % m

    bits = ''.join(list(map(lambda x: '{0:08b}'.format(x), randomNums)))
    return bits

def wichmanGenerator(ss, n, m1 = 30269, m2 = 30307,m3 = 30323):
    s1 = ss[0]
    s2 = ss[1]
    s3 = ss[2]
    

    randomNums = []

    for i in range(1, n + 1):
        s1 = (171 * s1) % m1
        s2 = (172 * s2) % m2
        s3 = (170 * s3) % m3
        v = ((s1 / m1) + (s2 / m2) + (s3 / m3)) % 1
        randomNums.append(v)

    bits = ''.join(list(map(lambda x: '{0:08b}'.format(int(x*1000)), randomNums)))

    return bits

#Suponiendo que se alimenta el primero
def lfsr(seed,n,step = 1,positions = []):
    def nextStep(chain):
        step = chain[:-1]
        return str(reduce(lambda i, j: int(i)^int(j), [chain[n] for n in positions])) + step
    result = ''
    current = '{0:b}'.format(seed)
    for x in range(1,(1 + n*step)):
        current = nextStep(current)
        if (x%step) ==0:
            result += current[-1]
        
    return result