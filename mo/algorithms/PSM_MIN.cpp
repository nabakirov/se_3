/* POCKET SEARCH METHOD (MIN point)*/

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

const double EPS = 1e-1;

double F(double X) {
	return -X * X * X - 6 * X * X + X + 6;
}

int main() {

	freopen("Talantbek_uulu_PSM_MIN.txt", "w", stdout);

	int k = 0;
	double H0 = 0.01, X0 = -4.13, R = 10;
	double H1 = H0, X1;

	cout << F(X0) << endl;

	double YF0 = F(X0);

	X1 = X0 + H0;

	double YF1 = F(X1);

	while(k < 7) {
		cout << "Iteration no." << k << ":" << endl << endl;
		cout << "Step 1: " << "Compute the current number of iteration: " << "k = k + 1 = "
			<< k << " + 1 = " << k + 1 << endl;
		k = k + 1;
		cout << "Step 2: " << "Checking of the logical condition YF1 >= YF0 -> " << YF1 << " >= " << YF0 << endl;
		if (YF1 >= YF0) {
			cout << "We can conclude that it is True.\nWe must compute the branch then of the logical statement if - then - else:\n";
			
			if (abs(H0) < EPS / R) {
				H1 = H0;
				X1 = X0;
				YF1 = YF0;
			}
			else {
				H1 = -H0 / R;
				H0 = H1;
				X0 = X1;
				YF0 = YF1;
				X1 = X0 + H1;
				YF1 = F(X1);
			}
		}
		else {
			cout << "We can conclude that it is False.\nWe must compute the branch else of the logical statement if - then - else:\n";
			
			cout << "H1 := H0 = " << H1 << " = " << H0 << endl;
			H1 = H0;

			X0 = X1;

			cout << "YF0 := YF1 = " << YF0 << " = " << YF1 << endl;
			YF0 = YF1;

			X1 = X0 + H1;

			cout << "YF1 := F(X1) = " << YF1 << " := " << F(X1) << endl;
			YF1 = F(X1);
		}
		cout << endl << endl;
	}

	cout << "Final result" << endl;
	cout << "X1: " << X1 << endl;
	cout << "YF1: " << YF1 << endl;
}
