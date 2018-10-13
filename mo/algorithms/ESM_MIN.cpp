
/* EVEN SEARCH METHOD */

#include <bits/stdc++.h>

#define eps 0.1

using namespace std;

double F(double X){
    return -0.04 * X * X * X + X * X + X -1;
}

int main(){

    // freopen("Talantbek_uuluESM.txt", "w", stdout);

    int k = 0;
    double H = 0.2, X0 = -3, X1;

    //cout << F(X0) << endl;

    double YF0 = F(X0);

    X1 = X0 + H;

    double YF1 = F(X1);

    for(;k != 7;){
        cout << "Iteration no." << k << ":" << endl << endl;
        cout << "Step 1: " << "Compute the current number of iteration: " << "k = k + 1 = "
             << k << " + 1 = " << k + 1 << endl;
        k = k + 1;
        cout << "Step 2: " << "Checking of the logical condition YF1 >= YF0 -> " << YF1 << " >= " << YF0 << endl;
        if(YF1 >= YF0){
            cout << "We can conclude that it is True.\n. We must compute the branch then of the logical statement if - then - else:\n";

            cout << "X1 := X0 = " << X1 << " := " << X0 << endl;
            X1 = X0;

            cout << "YF1 := YF0 = " << YF1 << " := " << YF0 << endl;
            YF1 = YF0;
        } else {
            cout << "We can conclude that it is False.\nWe must compute the branch else of the logical statement if - then - else:\n";
            cout << "X0 := X1 = " << X1 << endl;
            X0 = X1;

            cout << "YF0 := YF1 = " << YF0 << " = " << YF1 << endl;
            YF0 = YF1;

            cout << "X1 := X1 + H = " << X1 <<" + " << H << endl;
            X1 = X1 + H;

            cout << "YF1 := F(X1) = " << YF1 << " := " << F(X1) << endl;
            YF1 = F(X1);
        }
        cout << endl << endl;
    }

    cout << "Final result" << endl;
    cout << "X1: " << X1 << endl;
    cout << "YF1: " << YF1 << endl;
}
