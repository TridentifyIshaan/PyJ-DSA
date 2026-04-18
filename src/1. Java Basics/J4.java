/*
> Date Created: 18/04/2026
> Author: Ishaan Rastogi
> Purpose: To showcase conditionals in Java
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.*;

public class J4 {
    public static void main(String[] args) {

        // If
        int a = 10;
        if (a > 5) {
            System.out.println("a is greater than 5");
        }
        // If-Else
        if (a < 0) {
            System.out.println("a is negative");
        } else {
            System.out.println("a is positive");
        }
        // If-Else-If
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your age");
        int age = sc.nextInt();
        if (age >= 18) {
            System.out.println("Adult");
        } else if (age < 18 && age > 0) {
            System.out.println("Not Adult");
        } else {
            System.out.println("Invalid Age");
        }

        // Nested If-Else
        System.out.println("Do you have LeetCode Premium?");
        boolean hasLCpremium = sc.nextBoolean();
        System.out.println("Enter the number of problems you have solved");
        int solvedProblems = sc.nextInt();
        if (hasLCpremium) {
            if (solvedProblems >= 200) {
                System.out.println("Unlock Advanced Sheet");
            } else {
                System.out.println((200 - solvedProblems) + " more problems to go to unlock Advanced Sheet");
            }
        } else {
            System.out.println("Upgrade to Premium");
        }

        // Ternary Operator - (Condition) ? what to return when true: what to return
        // when false
        System.out.println("Enter the no. of streak days");
        int streakDays = sc.nextInt();
        String status = (streakDays >= 21) ? "Consistent" : "Irregular";
        System.out.println("Your status is: " + status);

        // Switch
        System.out.println("Enter the day number of the week");
        int n = sc.nextInt();
        switch (n) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Invalid Day");
        }
        // continue - will skip the current and move on

        // Advanced Switch
        System.out.println("Enter the day number of the week");
        int x = sc.nextInt();
        switch (x) {
            case 1 -> System.out.println("Monday");
            case 2 -> System.out.println("Tuesday");
            case 3 -> System.out.println("Wednesday");
            case 4 -> System.out.println("Thursday");
            case 5 -> System.out.println("Friday");
            case 6 -> System.out.println("Saturday");
            case 7 -> System.out.println("Sunday");
            default -> System.out.println("Invalid Day");
        }

    }
}
