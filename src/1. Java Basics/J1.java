/*
> Date Created: 14/04/2026
> Author: Ishaan Rastogi
> Purpose: Basics of Java, Variables, and Data Types
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

class J1 {
    public static void main(String[] args) {

        // println() prints the text and moves to the next line
        System.out.println("Hello, World!");

        // print() prints the text without moving to the next line
        System.out.print("Welcome to Java programming!");
        System.out.print(" Let's learn together.");

        System.out.println(); // This will move to the next line

        // ---------------------------------- VARIABLES
        // -----------------------------------

        // Create & Declare a variable
        int age;

        // Initialize a variable
        age = 20;
        System.out.println("Age: " + age);

        // Create, Declare & Initialize a variable in one line
        int totalMarks = 20;

        // Case sensitive
        int weight = 80;
        int Weight = 90; // This is a different variable from 'weight'

        /*
         * Variable name rules
         * 1. Can only contain letters, digits, underscores, and dollar signs
         * 2. Cannot start with a digit ( Compilation error)
         * 3. Cannot be a reserved keyword (Compilation error)
         * 4. Cannot contain spaces (Compilation error)
         * 
         * FUN FACT: Main is not a reserved keyword because it is a special method name
         * in Java
         */

        // Convention in every language is to use camelCase for variable names
        int myVariableName = 10;
        String firstName = "Ishaan";

    }
}