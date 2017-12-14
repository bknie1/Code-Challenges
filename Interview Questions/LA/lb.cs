using System;
using System.Collections.Generic;
using System.Linq;

namespace Leaderboard
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var p = new Program(); // Resolving an error.
            Tests();
        }

        private static void Tests()
        {
            var l = new Leaderboard();

            // Add a bunch of users.
            l.PostData("Alok", 1000);
            l.PostData("Mike", 2000);
            l.PostData("Kevin", 3000);
            l.PostData("Jon", 4000);
            l.PostData("Matt", 5000);
            l.PostData("Ngoc", 6000);
            l.PostData("Brandon", 9966);

            // Alok really killed it today. Update his steps.
            l.PostData("Alok", 10000);

            l.ShowLeaderboard(5, "Mike"); // Outside top 5.
            l.ShowLeaderboard(5, "Brandon"); // Inside top 5.
        }
    }

    //------------------------------------------------------------------------------------------------------------------
    internal class Leaderboard
    {
        /*
          The leaderboard owns a ranked (by steps) list of participants. We can add or update users on the leaderboard
          or request a 'top n' participants relative to a user.
         */

        private List<Participant> _rankedParticipants = new List<Participant>();

        // public Leaderboard() {} // Default constructor is enough.
        //--------------------------------------------------------------------------------------------------------------
        public void PostData(string username, int steps)
        {
            /*
              @arg string username
              @arg int steps

              Given a username and steps, either add the user or update the user's data in our ranked participants list.

              Refactors:
                  - Reduced nesting by continuing if we don't have a match.
                  - What if we pass in a larger value?

                  - Complexity of PostData: n log(n)
                      - Try O(n)? Dictionary to keep an index of the list I have.
                      - Dictionary username, where the person is in the list.

                  - I didn't like that we called sort twice. Used a condition tree to determine whether or not we're
                  adding a new participant and, either way, we sort at the end.
            */
            var present = false;
            username = username.Trim(); // Sanitize. If user facing: Implement a counter-injection method.

            foreach(var member in _rankedParticipants)
            {
                if (!string.Equals(member.Username, username)) continue; // These users do not match.

                // Else: These users match, so this user already exists in our db.
                member.Steps += steps;
                present = true;
            }

            // No match found, so add the new user.
            if (!present) _rankedParticipants.Add(new Participant(username, steps));

            RankSort(); // We sort regardless.
        }
        //--------------------------------------------------------------------------------------------------------------
        public void ShowLeaderboard(int top, string username)
        {
            /*
            Prints a human readable copy of our leaderboard with a target 'top' n participants. Will also print the
            desired user in relation to those top participants if the user isn't already included in those results.

            Refactors:
                - If the user wasn't included in our top in: Inverted the condition to reduce nesting.
                - Acknowledging Mike's concern about reaching for a top n that doesn't exist.

            Ideas:
                - Could use a params object[] args if we want a method that can deliver either a report or a report and
                specific user data. Requre [0] (top), but make [1] (username) optional.
            */

            if (top > _rankedParticipants.Count)
            {
                var e = new ArgumentOutOfRangeException("", "Error: 'top' value exceeds current leaderboard.");
                Console.WriteLine(e);
                return;
            }

            username = username.Trim(); // Sanitize. If user facing: Implement a counter-injection method.

            var isPresent = false;

            for(var i = 0; i < top; i++) // Print 'top' list.
            {
                Console.Write((i + 1) + ".\t");
                Console.WriteLine(_rankedParticipants[i].ToString());
                if(string.Equals(_rankedParticipants[i].Username, username))
                {
                    isPresent = true;
                }
            }

            if(!isPresent) // User not printed, so add them.
            {
                for(var i = top + 1; i < _rankedParticipants.Count; i++)
                {
                    if (!string.Equals(_rankedParticipants[i].Username, username)) continue; // These users don't match.

                    // This is the user we want; they exist in the db. Print their data.
                    Console.Write((i + 1) + ".\t");
                    Console.WriteLine(_rankedParticipants[i].ToString() + "\n");
                    return;
                }
                Console.WriteLine("Error: User not found.");
            }
            Console.WriteLine();
        }
        //--------------------------------------------------------------------------------------------------------------
        private void RankSort()
        {
            _rankedParticipants = _rankedParticipants.OrderByDescending(o => o.Steps).ToList();
        }
        //--------------------------------------------------------------------------------------------------------------
    }
    //------------------------------------------------------------------------------------------------------------------
    internal class Participant
    {
        /*
          Each participant has their own unique ID that tracks their progress.
         */
        public readonly string Username;
        public int Steps = 0;
        //--------------------------------------------------------------------------------------------------------------
        public Participant(string username, int steps)
        {
            this.Username = username;
            this.Steps += steps;
        }
        //--------------------------------------------------------------------------------------------------------------
        public override string ToString()
        {
            // return $"{Username} {Steps}"; // Rider says this is an old C# 6.0 feature.
            return string.Concat(Username, "\t", Steps);
        }
        //--------------------------------------------------------------------------------------------------------------
    }
}
