/*
> Date Created: 17/04/2026
> Author: Ishaan Rastogi
> Purpose: Types of Operators
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working

Notes:
 1. Arithmetic operators ( +, -, *, /, % )
 2. Relational operators ( <, >, <=, >=, ==, != )
 3. Logical operators ( &&, ||, ! )
 4. Assignment & Shorthand operators ( =, +=, -=, *=, /=, %= )
 5. Unary operators ( +, - )
 6. Increment/Decrement operators ( ++, -- )
 7. Bitwise operators ( &, |, ^, ~, <<, >> )
 8. Ternary operator ( ? : )
 9. Special operators ( sizeof, instanceof )
 10. Typecasting
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

        // Assignment & Shorthand operators
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

        // Unary operators
        a = 10;
        int e = +a;
        System.out.println(e); // 10
        int f = -a;
        System.out.println(f); // -10
        System.out.println("");

        // Increment/Decrement operators
        a = 1;
        System.out.println("Pre");
        System.out.println(++a); // add 1 to a and then print a
        System.out.println(--a); // subtract 1 from a and then print a
        System.out.println("Post");
        System.out.println(a++); // print a and then add 1 to a
        System.out.println(a--); // print a and then subtract 1 from a
        System.out.println("Final Value of a: " + a); // 1
        System.out.println("");

        // Soln - 2 1 1 2 1

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
        System.out.println(c + (int) d); // 30
        System.out.println("");
    }
}