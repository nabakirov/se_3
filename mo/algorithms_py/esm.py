
import sys
sys.stdout = open("./_gssm_max.txt", "w+")

def F(X):
	return round(-0.04 * X ** 3 + X ** 2 + X -1, 4)


def esm_min(H, X0, tollerance, max_k=7):
	k = 0
	YF0 = F(X0)
	X1 = round(X0 + H, 4) 
	YF1 = F(X1)

	while k < max_k:
		k += 1
		print(f"1) k = {k}\n")
		print(f"2) y(k) >= y(k-1) -> {YF1} >= {YF0}\n")

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
			print(f"3) y(k+1) = f(x(k+1)) = {YF1}\n")
			print(f"4) k < k_max -> {k} < {max_k}")
			print(f"\t{k < max_k}\n\n\n")
	print(f'x = {X1}\n')
	print(f'y = {YF1}')


def esm_max(H, X0, tollerance, file=None, max_k=7):
	if file:
		print = file.write
	k = 0
	YF0 = F(X0)
	X1 = round(X0 + H, 4) 
	YF1 = F(X1)
	print(f"\n\tH = {H}\n\tX0 = {X0}\n\tX1 = {X1}\n\tYF0 = {YF0}\n\tYF1 = {YF1}\n\n")

	while k < max_k:
		k += 1
		print(f"1) k = {k}\n")
		print(f"2) y(k) <= y(k-1) -> {YF1} <= {YF0}")

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
			print(f"3) y(k+1) = f(x(k+1)) = {YF1}\n")
			print(f"4) k < k_max -> {k} < {max_k}")
			print(f"\t{k < max_k}\n\n\n")
	print(f'x = {X1}\n')
	print(f'y = {YF1}')



if __name__ == '__main__':
	H = 0.2
	X0 = -3
	max_k = 6
	tollerance = 0.01
	esm_min(H, X0, tollerance, max_k)
		# esm_max(H, X0, tollerance, file, max_k)



