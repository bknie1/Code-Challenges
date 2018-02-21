using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    
    public static int fib(int n) {
        // fib(n) = fib(n - 1) + fib(n - 2)
        if(n > 1) {
            return fib(n - 1) + fib(n - 2);
        }
        return n; // Can't fib any more!
    }

    static void Main(String[] args) {
        /* Given n in the fib sequence, complete the fibonacci function so it returns fib(n).
            fib(0) = 0
            fib(1) = 1
            fib(2) = 0 + 1 = 1
            fib(3) = 1 + 1 = 2
            fib(4) = 1 + 2 = 3
            fib(5) = 2 + 3 = 5
        */
        int n = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(fib(n));
    }
}
