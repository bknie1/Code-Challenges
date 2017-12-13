/*
  Create a ranked leaderboard that allows you to add participants and update
  their steps.


*/

using System;

class Solution
{
    static void Main(string[] args)
    {
        Leaderboard l = new Leaderboard();
        l.PostData("Brandon", 1000);
        l.PostData("Alok", 2000);
        l.PostData("Mike", 3000);
    }
}

class Leaderboard
{
  /*
    The leaderboard owns a ranked (by steps) list of participants.
    We can post new data (users) to the leaderboard or request
  */
    private List<Participant> rankedParticipants = new List<Participant>();

    Leaderboard()
    {
      // Placeholder.
    }

    void PostData(string username, int steps)
    {
      /*
        @arg string username
        @arg int steps

        Given a username and steps, either add the user or update the user's
        data in our ranked participants list.

        Considerations:
          What if we pass in a larger value?

        Complexity of PostData: n log(n)
        Try O(n)? Dictionary to keep an index of the list I have.
        Dictionary username, where the person is in the list.
      */
        foreach(var member in rankedParticipant)
        {
            if(string.Equals(member.username, username))
            {
                member.steps += steps;
                rank_sort();
                return;
            }
        }
        rankedParticipants.add(new Participant(username, steps));
        rank_sort();
    }

    void ShowLeaderboard(int top, string username)
    {
      /*
      Prints a human readable copy of our leaderboard with a target 'top' n
      participants. Will also print the desired user in relation to those top
      participants if the user isn't already included in those results.

      Example
        ShowLeaderboard(3,"alok");
          Jon 1 9000
          Mike 2 8000
          Brandon 3 7000
          Alok   10 1000
      */
        bool is_present = false;

        for(var i = 0; i <= top; i++) // Print 'top' list.
        {
            Console.Write((i + 1) + " ");
            rankedParticipant[i].toString();
            if(string.Equals(rankedParticipant[i].username, username))
            {
                is_present = true;
            }
        }

        if(!is_present) // User not printed, so add them.
        {
            for(var i = top + 1; i < rankedParticipants.length; i++)
            {
                if(string.Equals(rankedParticipants[i].username, username))
                {
                    Console.Write((i + 1) + " ");
                    rankedParticipant[i].toString();
                    return;
                }
            }
        }
        Console.WriteLine("Error: User not found.");
    }
}
class Participant
{
  /*
    Each participant has their own unique ID that tracks their progress.
  */
    public readonly string username; // UID
    public int steps = 0; // The number of steps the user has walked in total.

    Participant(string username, int steps)
    {
        this.username = username;
        this.steps = steps;
    }

    public override string ToString()
    {
        return $"{username} {steps}";
    }
}
