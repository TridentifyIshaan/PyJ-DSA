/*
> Date Created: 24/04/2026
> Author: Ishaan Rastogi
> Purpose: To print hollow square pattern
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.*;

public class J1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the length of the square:");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == 1 || i == n || j == 1 || j == n) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
}
