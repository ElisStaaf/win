#include <stdio.h>
#include <float.h>
#include <math.h>

double simpleCalc(double num1, double num2, char op) {
    double res;

    switch (op) {
    case '+':
        res = num1 + num2;
        break;
    case '-':
        res = num1 - num2;
        break;
    case '*':
        res = num1 * num2;
        break;
    case '/':
        res = num1 / num2;
        break;
    case '^':
        res = pow(num1, num2);
        break;
    default:
        printf("ERROR: Invalid operator.\n");
        return -DBL_MAX;
    }
    return res;
}

int main() {
    char op;
    double num1, num2, res;

    // Read the operator
    printf("op>");
    scanf("%c", &op);

    // Read the two numbers
    printf("num>");
    scanf("%lf %lf", &num1, &num2);

    res = simpleCalc(num1, num2, op);

    // Print the result
    if (res != -DBL_MAX)
        printf("Result: %.2lf\n", res);
    
    return 0;
}
