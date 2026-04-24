/*
> Date Created: 24/04/2026
> Author: Ishaan Rastogi
> Purpose: To print a solid diamond pattern (pyramid + inverse pyramid)
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.*;

class J8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows in the pyramid: ");
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n - i; j++) {
                System.out.print("  ");
            }
            for (int k = 1; k <= 2 * i - 1; k++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        // Inverted pyramid has 1 row less than the above rows => n - 1
        for (int i = 1; i <= n - 1; i++) { // n - 1 = n - 1
            for (int j = 1; j <= i; j++) { // + 1
                System.out.print("  ");
            }
            // we are -1 twice because for start and end of the loop
            for (int k = 1; k <= 2 * (n - i) - 1; k++) { // 2 * (n - i) + 1 - 1 - 1 = 2 * (n - i) - 1
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}