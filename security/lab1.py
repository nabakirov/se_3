LIBRARY_LETTER = dict(
a=0,
b=1,
c=2,
d=3,
e=4,
f=5,
g=6,
h=7,
i=8,
j=9,
k=10,
l=11,
m=12,
n=13,
o=14,
p=15,
q=16,
r=17,
s=18,
t=19,
u=20,
v=21,
w=22,
x=23,
y=24,
z=25
)
LIBRARY_DIGIT = {
0: 'a',
1: 'b',
2: 'c',
3: 'd',
4: 'e',
5: 'f',
6: 'g',
7: 'h',
8: 'i',
9: 'j',
10: 'k',
11: 'l',
12: 'm',
13: 'n',
14: 'o',
15: 'p',
16: 'q',
17: 'r',
18: 's',
19: 't',
20: 'u',
21: 'v',
22: 'w',
23: 'x',
24: 'y',
25: 'z'
}
n = len(LIBRARY_DIGIT)


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

def addition_key(key, n):
	return n - key % n 


@click.command()
def affine_encode():
	print("text to decode")
	rawstring = input()
	print("multiplication key")
	key1 = int(input())
	if nod(key1, n) != 1:
		print("multiplication key must be coprime")
		return
	print("addition key")
	key2 = int(input())
	if not (0 < key2 <= n):
		print("addition key must be 0 < key <= {}".format(n))
		return
	m_key = multiplication_key(key1, n)
	a_key = addition_key(key2, n)
	raw_array = rawstring.lower()
	encrypted = []
	for letter in raw_array:
		w = key1 * LIBRARY_LETTER[letter] + key2
		w = w if w <= n else w % n
		encrypted.append(LIBRARY_DIGIT[w])
	print()
	print("encoded: ", ''.join([k for k in encrypted]))
	print('reverse multiplication key: ', m_key)
	print('reverse addition key: ', a_key)
	print()


@click.command()
def affine_decode():
	print("text to decode")
	rawstring = input()
	print("multiplication key")
	key1 = int(input())
	print("addition key")
	key2 = int(input())
	raw_array = rawstring.lower()
	encrypted = []
	for letter in raw_array:
		w = key1 * (LIBRARY_LETTER[letter] + key2)
		w = w if w <= n else w % n
		encrypted.append(LIBRARY_DIGIT[w])
	print(''.join([k for k in encrypted]))




def additivity(rawstring, key: int):
	if key >= n:
		raise ValueError('key must be lower than n')
	raw_array = rawstring.lower()
	encrypted = []
	for letter in raw_array:
		w = LIBRARY_LETTER[letter] + key
		w = w if w <= n else w % n
		encrypted.append(LIBRARY_DIGIT[w])
	return ''.join([k for k in encrypted])


cli.add_command(affine_decode)
cli.add_command(affine_encode)


if __name__ == '__main__':
	cli()
