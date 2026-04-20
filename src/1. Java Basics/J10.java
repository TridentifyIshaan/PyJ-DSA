/*
> Date Created: 20-04-2026
> Author: Ishaan Rastogi
> Purpose: To print the prime numbers in range 1 to 100
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

class J10 {
    public static void main(String[] args) {
        for (int i = 2; i <= 100; i++) {
            boolean flag = true;

            for (int j = 2; j <= i / 2; j++) {
                if (i % j == 0) {
                    flag = false;
                    break;
                }
            }

            if (flag) { // if flag is true then the number is prime
                System.out.println(i);
            }
        }
    }
}
