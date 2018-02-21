using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static void Main(String[] args) {
        int t = Convert.ToInt32(Console.ReadLine());
        for(int a0 = 0; a0 < t; a0++) {
            string expression = Console.ReadLine();
            Console.WriteLine(validate(expression));
        }
    }
    static string validate(string s) {
        
        
        int length = s.Length; // Initial length.
        // Console.WriteLine("Old: " + s + " " + length); // DEBUG
        
        // While there is content, and even numbered content...
        while(length != 0 && length % 2 == 0) {
            // Find and replace ordered pairs.
            // Ideally, we end up with a blank str.
            s = s.Replace("()", "");
            s = s.Replace("[]", "");
            s = s.Replace("{}", "");
            
            // Has our length changed? If so, update.
            if(length > s.Length) length = s.Length;
            // Otherwise, we can't make any more changes.
            else length = 0;
        }
        // Console.WriteLine("New: " + s + " " + length); // DEBUG
        // Any leftover, unprocessed characters?
        if(s.Length != 0) return "NO";
        // No? Valid!
        return "YES";
    }
}
