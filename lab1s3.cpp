#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Bikvadratnoe {
public:
    double koef_a, koef_b, koef_c;

    double vvesti_chislo(string imya) {
        double znachenieп++;
        while (true) {
            cout << "Enter " << imya << ": ";
            if (cin >> znachenie) {
                return znachenie;
            }
            cout << "This is not a number, enter a number" << endl;
            cin.clear();
            cin.ignore(10000, '\n');
        }
    }

    void vvod() {
        koef_a = vvesti_chislo("A");
        koef_b = vvesti_chislo("B");
        koef_c = vvesti_chislo("C");
    }

    void reshenie() {
        if (koef_a == 0) {
            reshenie_kvadratnogo();
            return;
        }

        double D = koef_b * koef_b - 4 * koef_a * koef_c;
        cout << "D = " << D << endl;

        if (D < 0) {
            cout << "No roots" << endl;
            return;
        }

        if (D == 0) {
            double zamena = -koef_b / (2 * koef_a);
            vyvesti_korni(zamena);
            return;
        }

        double zamena1 = (-koef_b + sqrt(D)) / (2 * koef_a);
        double zamena2 = (-koef_b - sqrt(D)) / (2 * koef_a);
        vyvesti_korni(zamena1);
        vyvesti_korni(zamena2);
    }

    void reshenie_kvadratnogo() {
        cout << "A = 0, solving B*x^2 + C = 0" << endl;

        if (koef_b == 0) {
            if (koef_c == 0)
                cout << "Equation 0 = 0, any x is a solution" << endl;
            else
                cout << "Equation has no solutions" << endl;
            return;
        }

        double zamena = -koef_c / koef_b;
        vyvesti_korni(zamena);
    }

    void vyvesti_korni(double zamena) {
        if (zamena < 0) return;
        if (zamena == 0) {
            cout << "x = 0" << endl;
        } else {
            cout << "x = " << sqrt(zamena) << endl;
            cout << "x = " << -sqrt(zamena) << endl;
        }
    }
};

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");
    Bikvadratnoe uravnenie;
    uravnenie.vvod();
    uravnenie.reshenie();
    return 0;
}