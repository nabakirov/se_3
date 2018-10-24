

def F(X):
	return round(-0.04 * X ** 3 + X ** 2 + X -1, 4)


def esm_min(H, X0, tollerance, file=None, max_k=7):
	if file:
		print = file.write
	k = 0
	YF0 = F(X0)
	X1 = round(X0 + H, 4) 
	YF1 = F(X1)

	while k < max_k:
		k += 1
		print(f"Step 1. k = {k}\n")
		print(f"Step 2. y(k) >= y(k-1) -> {YF1} >= {YF0}\n")

		if YF1 >= YF0:
			print("\tTrue\n")
			X1 = X0
			YF1 = YF0
		else:
			print("\tFalse\n")
			print(f"\tx(k+1) = {X1} + {H} = {round(X1 + H, 4)}\n")
			X0 = X1
			YF0 = YF1
			X1 = round(X1 + H, 4)
			YF1 = F(X1)
			print(f"Step 3. y(k+1) = {YF1}\n")
			print(f"Step 4. abs(x(k) - x(k+1)) = |{X0} - {X1}| = {round(abs(X0 - X1), 4)}\n")
			print(f"Step 5. {round(abs(X0 - X1), 4)} >= {tollerance}\n")
			print(f"\t{abs(X0 - X1) >= tollerance}\n\n\n")
	print(f'x = {X1}\n')
	print(f'y = {YF1}')


def esm_max(H, X0, tollerance, file=None, max_k=7):
	if file:
		print = file.write
	k = 0
	YF0 = F(X0)
	X1 = round(X0 + H, 4) 
	YF1 = F(X1)

	while k < max_k:
		k += 1
		print(f"Step 1. k = {k}\n")
		print(f"Step 2. y(k) <= y(k-1) -> {YF1} >= {YF0}\n")

		if YF1 <= YF0:
			print("\tTrue\n")
			X1 = X0
			YF1 = YF0
		else:
			print("\tFalse\n")
			print(f"\tx(k+1) = {X1} + {H} = {round(X1 + H, 4)}\n")
			X0 = X1
			YF0 = YF1
			X1 = round(X1 + H, 4)
			YF1 = F(X1)
			print(f"Step 3. y(k+1) = {YF1}\n")
			print(f"Step 4. abs(x(k) - x(k+1)) = |{X0} - {X1}| = {round(abs(X0 - X1), 4)}\n")
			print(f"Step 5. {round(abs(X0 - X1), 4)} >= {tollerance}\n")
			print(f"\t{abs(X0 - X1) >= tollerance}\n\n\n")
	print(f'x = {X1}\n')
	print(f'y = {YF1}')



if __name__ == '__main__':
	H = 0.2
	X0 = -3
	max_k = 6
	tollerance = 0.01
	filename = './abakirov_esm_max.txt'
	with open(filename, 'w+') as file:
		# esm_min(H, X0, tollerance, file, max_k)
		esm_max(H, X0, tollerance, file, max_k)



