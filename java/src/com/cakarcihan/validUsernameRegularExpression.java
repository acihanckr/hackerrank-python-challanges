package com.cakarcihan;

import java.util.Scanner;
class UsernameValidator {
    // start
    public static final String regularExpression = "[A-Za-z]{1}[A-Za-z0-9_]{7,29}";
    // end
}


public class validUsernameRegularExpression {

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine());
        while (n-- != 0) {
            String userName = scan.nextLine();

            if (userName.matches(UsernameValidator.regularExpression)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }
        }
    }
}