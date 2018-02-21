using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution
{
    //-------------------------------------------------------------------------
    static int[] exactLeft(int[] a, int n, int d)
    {
        /* 
         * Slice the first k values because we know they will get shifted to the end.
         * Slice the remaining values.
         * Append those k values to the end of our remaining values.
         * Everything is in its final position.
         */

        // Account for error.
        if (a == null || d <= 0 || n <= 1) return a;

        // Slice off the first d elements because they would have ended up at the end.
        int[] newEnd = new int[d];      // Prep enough space for these d values.

        // Copy(Source Array, Source Start, Dest Array, Dest Start, # of Values)
        Array.Copy(a, 0, newEnd, 0, d);

        // The remaining values.
        //  - We already got the d values, so subtract them from n to measure what's left.
        int[] newStart = new int[n - d];
        Array.Copy(a, d, newStart, 0, n - d);

        // Append end values to the remaining values.
        int[] result = newStart.Concat(newEnd).ToArray();

        return result;
    }
    //-------------------------------------------------------------------------
    static void print(int[] a)
    {
        foreach (var i in a)
        {
            Console.Write(i + " ");
        }
    }
    //-------------------------------------------------------------------------
    static void Main(String[] args)
    {
        string[] tokens_n = Console.ReadLine().Split(' ');
        int n = Convert.ToInt32(tokens_n[0]); // n: size
        int k = Convert.ToInt32(tokens_n[1]); // k: shift
        string[] a_temp = Console.ReadLine().Split(' ');
        int[] a = Array.ConvertAll(a_temp, Int32.Parse); // Values

        a = exactLeft(a, n, k);
        // for(var i = 0; i < k; ++i) {
        //     a = simpleLeft(a, n);
        // }
        // foreach(var i in a) {
        //     Console.Write(i + " ");
        // }
        print(a);
    }
    //-------------------------------------------------------------------------
}