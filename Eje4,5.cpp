#include <iostream>
#include <cmath> // Para std::abs
using namespace std;

// Definición de la función original f(x)
double f(double x) {
    return 25 * pow(x, 3) - 6 * pow(x, 2) + 7 * x - 88;
}

// Definición de la primera derivada f'(x)
double f_prime(double x) {
    return 75 * pow(x, 2) - 12 * x + 7;
}

// Definición de la segunda derivada f''(x)
double f_double_prime(double x) {
    return 150 * x - 12;
}

// Definición de la tercera derivada f'''(x)
double f_triple_prime(double x) {
    return 150;
}

// Función para calcular la serie de Taylor hasta el tercer orden
double taylor_approximation(double x, double a) {
    double f_a = f(a);
    double f_prime_a = f_prime(a);
    double f_double_prime_a = f_double_prime(a);
    double f_triple_prime_a = f_triple_prime(a);

    double taylor_value = f_a 
                        + f_prime_a * (x - a) 
                        + (f_double_prime_a / 2.0) * pow(x - a, 2) 
                        + (f_triple_prime_a / 6.0) * pow(x - a, 3);

    return taylor_value;
}

// Función para calcular el error relativo porcentual
double relative_error(double true_value, double approx_value) {
    return abs((true_value - approx_value) / true_value) * 100.0;
}

int main() {
    double x_base = 1.0; // Punto base de la expansión de Taylor
    double x_target = 3.0; // Punto donde queremos predecir f(3)

    // Valor exacto de f(3)
    double true_value = f(x_target);

    // Cálculo de la aproximación de Taylor hasta tercer orden
    double taylor_value = taylor_approximation(x_target, x_base);

    // Cálculo del error relativo porcentual
    double error = relative_error(true_value, taylor_value);

    // Mostrar los resultados
    cout << "Valor exacto de f(3): " << true_value << endl;
    cout << "Aproximación con Taylor de tercer orden: " << taylor_value << endl;
    cout << "Error relativo porcentual: " << error << "%" << endl;

    return 0;
}
