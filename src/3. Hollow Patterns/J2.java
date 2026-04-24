/*
> Date Created: 24/04/2026
> Author: Ishaan Rastogi
> Purpose: To print a rectangle hollow pattern
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.*;

public class J2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows in the rectangle:");
        int r = sc.nextInt();
        System.out.println("Enter the number of columns in the rectangle:");
        int c = sc.nextInt();

        for (int i = 1; i <= r; i++) {
            for (int j = 1; j <= c; j++) {
                if (i == 1 || i == r || j == 1 || j == c) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }
    }
}
