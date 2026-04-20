/*
> Date Created: 20-04-2026
> Author: Ishaan Rastogi
> Purpose: To print the sum of first n natural numbers
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

import java.util.*;

class J8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of numbers:");
        int n = sc.nextInt();
        int sum = 0;

        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        System.out.println("The sum is: " + sum);
    }
}
