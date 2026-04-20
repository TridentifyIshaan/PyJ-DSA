/*
> Date Created: 20-04-2026
> Author: Ishaan Rastogi
> Purpose: To print numbers from 1 to n and n to 1 respectively
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.*;

class J6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of numbers:");
        int n = sc.nextInt();

        System.out.println("Numbers from 1 to n:");
        for (int i = 1; i <= n; i++) {
            System.out.println(i);
        }

        System.out.println("Numbers from n to 1:");
        for (int j = n; j >= 1; j--) {
            System.out.println(j);
        }
    }
}
