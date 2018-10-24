#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

const double EPS = 1e-1;

double F(double X) {
	return -X * X * X - 6 * X * X + X + 6;
}

int main() {

	freopen("KopahovGSSM_MIN.txt", "w", stdout);

	double a = -4.76, b = -4.72; // left and right borders [a,b];

	printf("left border = %lf\nright border = %lf\n", a, b);

	double r = (pow(5.0, 0.5) - 1.0) / 2.0;
	printf("r = %lf\n", r);

	double X0 = a + (1.0 - r) * (b - a);
	printf("X0 = %lf\n", X0);
	double F0 = F(X0);
	printf("F0 = %lf\n", F0);
	double X1 = a + r * (b - a);
	printf("X1 = %lf\n", X1);
	double F1 = F(X1);
	printf("F1 = %lf\n\n", F(X1));

	int k = 0;

	while (true) {
		printf("Iteration no. %d:\n", k);
		printf("Step 1: Compute k = k + 1 -> %d + 1 = %d\n", k, k + 1);
		k += 1;
		printf("Step 2: Checking of F0 < F1 -> %lf < %lf\n", F0, F1);
		if (F0 < F1) {
			printf("Statement is true\n");
			printf("a := X0 - > %lf = %lf\n", a, X0);
			a = X0;
			printf("X0 := X1 -> %lf = %lf\n", X0, X1);
			X0 = X1;
			printf("F0 := F1 -> %lf = %lf\n", F0, F1);
			F0 = F1;
			printf("X1 := a + r * (b - a) -> %lf := %lf + %lf * (%lf - %lf)\n", X1, a, r, b, a);
			X1 = a + r * (b - a);
			printf("F1 := F(X1) -> %lf := %lf\n", F1, F(X1));
			F1 = F(X1);
		}
		else {
			printf("Statement is False\n");
			printf("b := X1 -> %lf := %lf\n", b, X1);
			b = X1;
			printf("X1 := X0 -> %lf := %lf\n", X1, X0);
			X1 = X0;
			printf("F1 := F0 -> %lf := %lf\n", F1, F0);
			F1 = F0;
			printf("X0 := a + (1 - r) * (b - a) - > %lf := %lf + (%lf - %lf) * (%lf - %lf)\n", X0, a, r, b, a);
			X0 = a + (1 - r) * (b - a);
			printf("F0 := F(X0), %lf := %lf\n");
			F0 = F(X0);
		}
		printf("\n");
		if (k == 6) {
			break;
		}
	}

	cout << "Final Result:" << endl;
	cout << "X1: " << X1 << endl;
	cout << "F1: " << F1 << endl;

	return 0;
}
