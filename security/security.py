

LIBRARY_LETTER = dict()
LIBRARY_DIGIT = dict()

import string

bank = string.ascii_lowercase + string.digits + '.'
for i, k in enumerate(bank):
    LIBRARY_LETTER[k] = i
    LIBRARY_DIGIT[i] = k

n = len(bank)


import click


@click.group()
def cli():
    pass


def nod(a, b):
    c = max(a, b)
    r = 0
    for i in range(1, c):
        if a % i == 0 and b % i == 0:
            r = i
    return r


def multiplication_key(key, n):
    for i in range(1, n):
        if key * i % n == 1:
            return i
    return None

def addition_key(key, n=n):
    return n - key % n 


@click.command()
def affine_encode():
    print(bank)

    print("n =", n)
    rawstring = input("text to decode: ")
    key1 = int(input("multiplication key: "))
    if nod(key1, n) != 1:
        print("multiplication key must be coprime")
        return
    key2 = int(input("addition key: "))
    if not (0 < key2 < n):
        print("addition key must be 0 < key < {}".format(n))
        return
    m_key = multiplication_key(key1, n)
    a_key = addition_key(key2, n)
    raw_array = rawstring.lower()
    encrypted = []
    for letter in raw_array:
        w = key1 * LIBRARY_LETTER[letter] + key2
        w = w if w < n else w % n
        encrypted.append(LIBRARY_DIGIT[w])
    print()
    print("encoded:\t", ''.join([k for k in encrypted]))
    print('reverse multiplication key:\t', m_key)
    print('reverse addition key:\t', a_key)
    print()


@click.command()
def affine_decode():
    rawstring = input("text to decode: ")
    key1 = int(input("multiplication key: "))
    key2 = int(input("addition key: "))
    raw_array = rawstring.lower()
    encrypted = []
    for letter in raw_array:
        w = key1 * (LIBRARY_LETTER[letter] + key2)
        w = w if w < n else w % n
        encrypted.append(LIBRARY_DIGIT[w])
    print(''.join([k for k in encrypted]))


def visioner(rawstring, key):
    encoded = ''
    ki = 0
    for i, letter in enumerate(rawstring):
        if i % len(key) == 0:
            ki = 0
        w = LIBRARY_LETTER[key[ki]] + LIBRARY_LETTER[letter]
        w = w if w < n else w % n
        encoded += LIBRARY_DIGIT[w]
    return encoded


@click.command()
def visioner_encode():
    print(bank)

    print("n =", n)
    rawstring = input("text to decode: ").lower()

    key = input("key: ").lower()

    
    reverse_key = ''.join([LIBRARY_DIGIT[addition_key(LIBRARY_LETTER[l])] for l in key])
    encoded = visioner(rawstring, key)
    print("encoded\t", encoded)
    print("reverse_key\t", reverse_key)


@click.command()
def visioner_decode():
    rawstring = input("text to decode: ").lower()

    key = input("key: ").lower()

    encoded = visioner(rawstring, key)
    print("decoded\t", encoded)




def additivity(rawstring, key: int):
    if key >= n:
        raise ValueError('key must be lower than n')
    raw_array = rawstring.lower()
    encrypted = []
    for letter in raw_array:
        w = LIBRARY_LETTER[letter] + key
        w = w if w < n else w % n
        encrypted.append(LIBRARY_DIGIT[w])
    return ''.join([k for k in encrypted])

import math, sys

class Matrix:
    def __init__(self, array, n):
        if math.sqrt(len(array)) != n:
            raise AttributeError('array square root must be n')
        self.array = array
        self.n = n
        self.len = len(array)
    def __call__(self, x, y):
        return self.array[y * self.n + x]
    def d(self, i):
        return i % self.n, i // self.n


@click.command()
def hill():
    alpha = tuple(string.ascii_lowercase)
    n = len(string.ascii_lowercase)
    print(string.ascii_lowercase)
    print(n)
    from re import findall
    matrixLength = 2
    MatrixKey = [[15,4],[11,3]]
    det = MatrixKey[0][0]*MatrixKey[1][1] - MatrixKey[0][1]*MatrixKey[1][0]
    print(det)
    if det != 1:
        print("Error: determinant != 1"); raise SystemExit
    iMatrixKey = [
        [MatrixKey[1][1],-MatrixKey[0][1]],
        [-MatrixKey[1][0],MatrixKey[0][0]]
    ]
    cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
    if cryptMode not in ['E','D']:
            print("Error: mode is not Found!"); raise SystemExit
    startMessage = input("Write the message: ").lower()
    while len(startMessage) % matrixLength != 0: startMessage += 'z'
    def regular(text):
        template = r"[a-z]{"+str(matrixLength)+"}"
        return findall(template, text)
    def encryptDecrypt(message, matrix, summ = 0, final = ""):
        for double in range(len(message)):
            for string in range(matrixLength):
                for column in range(matrixLength):
                    summ += matrix[string][column] * alpha.index(message[double][column])
                final += alpha[(summ)%n]; summ = 0
        return final
    if cryptMode == 'E': finalMessage = encryptDecrypt(regular(startMessage), MatrixKey)
    else: finalMessage = encryptDecrypt(regular(startMessage), iMatrixKey)
    print("Final message:",finalMessage)
    

# createprocedureakcia
# 01234
# 30412 - 


# aoriceeatcearpdkeruc
# 13402



def shift_encode(rawstring: str, key: str):
    v_key = []
    for i in key:
        i = int(i)
        if i in v_key:
            print(f"key must contain column indexes, found second {i}")
            sys.exit(0)
        v_key.append(i)
    v_key = sorted(v_key)
    for i in range(len(key)):
        if i != v_key[i]:
            print(f"missing column {i}")
            sys.exit(0)
    reverse_key = ''
    for i, o in enumerate(key):
        for j, k in enumerate(key):
            if i == int(k):
                reverse_key += str(j)
    print(f"reverse key: {reverse_key}")
    key_l = len(key)
    while len(rawstring) % key_l != 0: rawstring += '.'
    matrix = {}
    for i, letter in enumerate(rawstring):
        column = i % key_l
        if column not in matrix:
            matrix[column] = ''
        matrix[column] += letter
    text = ''
    for index in key:
        text += matrix[int(index)]
    return text

def shift_decode(rawstring: str, key: str):
    key_l = len(rawstring) / len(key)
    matrix = [[] for i in range(len(key))]
    column = 0
    for i, letter in enumerate(rawstring):
        if i != 0 and i % key_l == 0:
            column += 1
        matrix[column].append(letter)
    text = ''
    new_matrix = []
    for index in key:
        index = int(index)
        new_matrix.append(matrix[index])
    for i, k in enumerate(key):
        for column in new_matrix:
            text += column[i]
    return text


@click.command()
def shift():
    crypt_mode = input("[E]ncrypt|[D]ecrypt: ").lower()
    message = input("Write the message: ").lower()
    key = input("key: ").lower()
    response = {
        'e': shift_encode,
        'd': shift_decode
    }
    print(response[crypt_mode](message, key))


cli.add_command(affine_decode)
cli.add_command(affine_encode)
cli.add_command(visioner_encode)
cli.add_command(visioner_decode)
cli.add_command(hill)
cli.add_command(shift)


if __name__ == '__main__':
    cli()
