/*
> Date Created: 20-04-2026
> Author: Ishaan Rastogi
> Purpose: To print the 10 multiples of n
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.*;

class J7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of numbers:");
        int n = sc.nextInt();

        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " * " + i + " = " + n * i);
        }
    }
}
