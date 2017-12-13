using System;

class Solution
{
    static void Main(string[] args)
    {
        for (var i = 0; i < 5; i++)
        {
            Console.WriteLine("Hello, World");
        }
    }
    
    public class UndoStack
    {
        string[] undoData;
        int currentLength = 0; // How much we have in it.
        int next = 0; // Where the next will go.

         public UndoStack(int capacity)
         {
             undoData = new string[capacity];
         }

        public void push(string currentData)
        {
            undoData[next] = currentData;
            next = (next + 1) % undoData.Length;
            if (currentLength < undoData.Length)
            {
                currentLength++;
            }
        }
        public string pop()
        {
            if(currentLength > 0)
            {
                currentLength -= 1;
                next -= 1;
                if(next < 0) next = undoData.Length;
                return undoData[next];
            }
            throw new Exception("Could not UNDO.");
        }
    }
}
