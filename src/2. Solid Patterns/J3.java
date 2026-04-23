/*
> Date Created: 23/04/2026 
> Author: Ishaan Rastogi
> Purpose: To print a right equilateral triangle pattern
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.Scanner;

class J3 {
    public static void main(String[] stringArray) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the length of the right equilateral triangle: ");
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
