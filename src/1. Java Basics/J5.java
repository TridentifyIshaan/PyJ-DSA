/*
> Date Created: 18/04/2026
> Author: Ishaan Rastogi
> Purpose: To showcase loops in java
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

public class J5 {
    public static void main(String[] args) {
        // for
        for (int i = 1; i <= 5; i++) {
            System.out.println(i);
        }
        System.out.println();

        for (int a = 1; a <= 10; a += 2) {
            System.out.println(a);
        }
        System.out.println();

        // Nested for
        for (int x = 1; x <= 3; x++) {
            for (int y = 1; y <= 3; y++) {
                System.out.print("* ");
            }
            System.out.println(); // println - next line
        }
        System.out.println();

        // for-each -> for (Datatype variable : Collection) {}
        // Use- When you want to iterate over any collection.
        String[] cars = { "Volvo", "Maruti", "Hyundai", "Honda" };
        for (String car : cars) {
            System.out.println(car);
        }
        System.out.println();

        int[] numbers = { 1, 2, 3, 4, 5 };
        for (int i : numbers) {
            System.out.println(i);
        }
        System.out.println();

        // while
        int i = 1;
        while (i <= 5) {
            System.out.println(i);
            i++;
        }
        System.out.println();

        // do-while
        int j = 1;
        do {
            System.out.println(j);
            j++;
        } while (j <= 5);
    }
}