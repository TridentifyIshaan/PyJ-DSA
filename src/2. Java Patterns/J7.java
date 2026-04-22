/*
> Date Created: 22/04/2026 
> Author: Ishaan Rastogi
> Purpose: Java Pattern 7
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.Scanner;

class J7 {
    public static void main(String[] stringArray) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of rows in the pyramid: ");
        int n = scanner.nextInt();
        for (int i = 1; i <= n; ++i) {
            int n2;
            for (n2 = 1; n2 <= i - 1; ++n2) {
                System.out.print("  ");
            }
            for (n2 = 1; n2 <= 2 * (n - i) + 1; ++n2) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
