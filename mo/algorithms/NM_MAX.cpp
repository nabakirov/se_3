#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

const double EPS = 1e-3;

double F(double X) {
	return -X * X * X - 8 * X * X + X + 8;
}

double DF(double X) {
	return -3 * X * X - 16 * X + 1;
}

double DDF(double X) {
	return -6 * X - 16;
}

int SIGN(double X) {
	return X >= 0 ? 1 : -1;
}


int main() {

	freopen("Bolotbek_uulu_NM_MAX.txt", "w", stdout);

	double X0 = 0.0, X1, R = 10, DP0, DP, DFX1, FX1;
	
	int COND = 0;

	double FX0 = F(X0),
		DFX0 = DF(X0),
		DDFX0 = DDF(X0);
	
	int k = 0;

	printf("FX0 := %lf\n", FX0);
	printf("DFX0 := %lf\n", DFX0);
	printf("DDFX0 := %lf\n", DDFX0);
	printf("COND := %d\n", COND);

	while (true) {
		printf("\nIteration no. %d:\n", k);
		printf("Step 1: Compute k = k + 1 -> %d + 1 = %d\n", k, k + 1);
		k += 1;
		printf("Checking of abs(DDFX0) <= EPS -> %lf < %lf\n", abs(DDFX0), EPS);
		if (abs(DDFX0) <= EPS) {
			printf("Statement is True.\n");
			printf("COND := 1\n");
			COND = 1;
		}
		else {
			printf("Statement is False\n");
			printf("DP := DFX0 / DDFX0 -> DP := %lf\n", DFX0 / DDFX0);
			DP = DFX0 / DDFX0;
		}
		printf("Checking of k = 1 -> %d = 1\n", k);
		if (k == 1) {
			printf("Statement is true.\n");
			DP0 = DP;
			printf("DP0 := DP -> DP0 := %lf\n", DP);
		}
		else {
			printf("Statement is false.\n");
		}
		printf("Checking of SIGN(DP0) = SIGN(DP) -> %d = %d\n", SIGN(DP0), SIGN(DP));
		if (SIGN(DP0) == SIGN(DP)) {
			printf("Statement is true\n");
			printf("X1 := X0 - DP -> X1 = %lf - %lf\n", X0, DP);
			X1 = X0 - DP;
		}
		else {
			printf("Statement is false\n");
			printf("X1 := X0 - DP / R  -> X1 = %lf - %lf\n", X0, DP / R);
			X1 = X0 - DP / R;
		}
		printf("DP0 := DP -> DP0 := %lf\n", DP);
		DP0 = DP;

		FX1 = F(X1);
		printf("FX1 := F(X1) -> FX1 := %lf\n", F(X1));
		
		DFX1 = DF(X1);
		printf("DFX1 := DF(X1) -> DFX1 := %lf\n", DF(X1));

		double REL_ERROR = 2 * abs(DP) / (abs(X1) + EPS);

		printf("REL_ERROR := 2 * abs(DP) / (abs(X1) + EPS) -> REL_ERROR := 2 * %lf\n", abs(DP) / (abs(X1 + EPS)));

		printf("Checking of REL_ERROR < EPS && COND != 1 -> %lf < %lf && %d != 1\n", REL_ERROR, EPS, COND);
		if (REL_ERROR < EPS && COND != 1) {
			printf("Statement is True.\n");
			printf("Cond := 2\n");
			COND = 2;
		}
		printf("X0 := X1 -> X0 := %lf\n", X1);
		X0 = X1;
		printf("DFX0 := DFX1 -> DFX0 := %lf\n", DFX1);
		DFX0 = DFX1;
		if (k == 6 || COND != 0) {
			break;
		}
	}

	cout << "Final result:\n";
	cout << "K: " << k << endl;
	cout << "X1: " << X1 << endl;
	cout << "EPS: " << EPS << endl;
	cout << "FX1: " << FX1 << endl;
	cout << "DFX1: " << DFX1 << endl;
	cout << "COND: " << COND << endl;

	return 0;
}
