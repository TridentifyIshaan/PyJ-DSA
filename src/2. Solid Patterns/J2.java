/*
> Date Created: 22/04/2026 
> Author: Ishaan Rastogi
> Purpose: Java Pattern 2
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.Scanner;

class J2 {
    public static void main(String[] stringArray) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of rows: ");
        int n = scanner.nextInt();
        System.out.println("Enter the number of columns: ");
        int n2 = scanner.nextInt();
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n2; ++j) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
