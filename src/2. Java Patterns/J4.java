/*
> Date Created: 22/04/2026 
> Author: Ishaan Rastogi
> Purpose: Java Pattern 4
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.Scanner;

class J4 {
    public static void main(String[] stringArray) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of rows: ");
        int n = scanner.nextInt();
        for (int i = 0; i < n; ++i) {
            int n2;
            for (n2 = 0; n2 < n - i; ++n2) {
                System.out.print(" ");
            }
            for (n2 = 0; n2 <= i; ++n2) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
