/*

    Author: Ishaan Rastogi
    Date: 17-04-2026
    Purpose: Types of Operators
    Notes:
    1. Arithmetic operators ( +, -, *, /, % )
    2. Relational operators ( <, >, <=, >=, ==, != )
    3. Logical operators ( &&, ||, ! )
    4. Assignment operators ( - =, +=, -=, *=, /=, %= )
    5. Increment/Decrement operators ( ++, -- )
    6. Bitwise operators ( &, |, ^, ~, <<, >> )
    7. Ternary operator ( ? : )
    8. Special operators ( sizeof, instanceof )

*/

class J2 {
    public static void main(String[] args) {

        // Arithmetic operators
        int a = 10;
        int b = 20;
        System.out.println(a + b); // 30
        System.out.println(a - b); // -10
        System.out.println(a * b); // 200
        System.out.println(a / b); // 0.5
        System.out.println(a % b); // 0.5

        // Relational operators
        System.out.println(a < b); // true
        System.out.println(a > b); // false
        System.out.println(a <= b); // true
        System.out.println(a >= b);
        System.out.println(a == b);
        System.out.println(a != b);

        // Logical operators
        System.out.println(a && b);
        System.out.println(a || b);
        System.out.println(!a);

        // Assignment operators
        a = b;
        System.out.println(a);
        a += b;
        System.out.println(a);
        a -= b;
        System.out.println(a);
        a *= b;
        System.out.println(a);
        a /= b;
        System.out.println(a);
        a %= b;
        System.out.println(a);

        // Increment/Decrement operators
        a++;
        System.out.println(a);
        a--;
        System.out.println(a);

        // Bitwise operators
        System.out.println(a & b);
        System.out.println(a | b);
        System.out.println(a ^ b);
        System.out.println(~a);
        System.out.println(a << b);
        System.out.println(a >> b);

        // Ternary operator
        System.out.println(a ? b : c);

        // Special operators
        System.out.println(sizeof(a));
        System.out.println(instanceof(a));
    }
}