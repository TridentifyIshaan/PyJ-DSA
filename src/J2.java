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
        System.out.println(a / b); // 0 - Floor Division means it will truncate the decimal part
        System.out.println(a % b); // 10 - Remainder
        System.out.println(""); // New Line

        // Relational operators
        System.out.println(a < b); // T
        System.out.println(a > b); // F
        System.out.println(a <= b); // T
        System.out.println(a >= b); // F
        System.out.println(a == b); // F
        System.out.println(a != b); // T
        System.out.println("");

        // Logical operators (In Java, these require boolean operands)
        boolean x = true;
        boolean y = false;
        System.out.println(x && y); // F
        System.out.println(x || y); // T
        System.out.println(!x); // F
        System.out.println("");

        // Assignment operators
        a = b; 
        System.out.println(a); // 20
        a += b;
        System.out.println(a); // 40
        a -= b;
        System.out.println(a); // 20
        a *= b;
        System.out.println(a); // 400
        a /= b;
        System.out.println(a); // 20
        a %= b;
        System.out.println(a); // 0
        System.out.println("");

        // Increment/Decrement operators - Shorthand
        a++;
        System.out.println(a); // 1
        a--;
        System.out.println(a); // 0
        System.out.println("");

        // Bitwise operators
        a = 10;
        b = 20;
        System.out.println(a & b); // 0 - AND
        System.out.println(a | b); // 30 - OR
        System.out.println(a ^ b); // 30 - XOR
        System.out.println(~a); // -11 - NOT
        System.out.println(a << b); // 10485760 = ((2^20) * 10) - Left Shift
        System.out.println(a >> b); // 0 - Right Shift
        System.out.println("");

        // Ternary operator (condition must be a boolean expression)
        System.out.println((a > b) ? a : b); // Meaning - If (a > b) is true then print a else print b - 20
        System.out.println("");

        // Special operators
        // Note: Java doesn't have sizeof operator. Primitive sizes are fixed.
        System.out.println("Size of int: " + Integer.BYTES + " bytes"); // 4
        System.out.println("");

        // instanceof is used for checking object types, not primitives.
        String str = "Hello";
        System.out.println(str instanceof String); // T
        System.out.println("");

        // Typecasting
        int c = 10;
        double d = 20.5;
        System.out.println(c + d); // 30.5
        System.out.println(c + (int)d); // 30
        System.out.println("");
    }
}