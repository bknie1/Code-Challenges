using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    static void Main(String[] args) {
        string a = Console.ReadLine();
        string b = Console.ReadLine();

        Console.WriteLine(tally(a, b));
    }
    
    static int tally(string a, string b) {
        a = a.ToLower();
        b = b.ToLower();
        
        int[] letters = new int[26]; // a-z slots
        int deletions = 0;

        if(a.Length <= 0 || b.Length <= 0) return deletions;
        
        // Count against each other.
        // Add all letter instances from 'a'.
        foreach(var c in a) {
            ++letters[c - 'a']; // ASCII offset.
        }
        
        // Cancel out a's tally with b's results.
        // Subtract all letter instances from 'b' to find our difference from 'a'.
        foreach(var c in b) {
            --letters[c - 'a']; // ASCII offset.
        }
        
        // Add values.
        // They simply exist, so we only need the abs.
        foreach(var i in letters) {
            deletions += Math.Abs(i);
        }
        
        // print(letters, length, pairs, deletions);
        return deletions;
   }
    
    static void print(int[] letters, int length, int pairs, int deletions) {
        foreach(var i in letters) {
            Console.WriteLine(i);
        }
        Console.WriteLine("Length: " + length); // DEBUG
        Console.WriteLine("Pairs: " + pairs); // DEBUG
        Console.WriteLine("Deletions: " + deletions); // DEBUG
    }
}
