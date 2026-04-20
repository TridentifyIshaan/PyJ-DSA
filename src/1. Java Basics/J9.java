/*
> Date Created: 20-04-2026
> Author: Ishaan Rastogi
> Purpose: To print all the numbers divisible by 7 within the range of 50 to 100
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
*/

class J9 {
    public static void main(String[] args) {

        for (int i = 50; i <= 100; i++) {
            if (i % 7 == 0) {
                System.out.println(i);
            }
        }
    }
}
