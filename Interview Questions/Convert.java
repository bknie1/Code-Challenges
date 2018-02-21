/*
Requirements:

Given some amount of money, we want to compute a representation of that amount using the fewest number of bills & coins.

Currency values to use:
$0.01
$0.05
$0.10
$0.25
$1.00
$5.00
$10.00
$20.00
$50.00
$100.00

For example, given $12.27 in US Currency,
the result would be: 1 cent + 1 cent + 1 quarter + 1 dollar + 1 dollar + 10 dollar

*/
// -------------------------------------------------------------------------------------------------------------------------------------------
/*
 * Given an amount of money, return a string result of the currency that represents that amount using the fewest currency values.
 */
public class CashConversion {

    private final Map<Float, String> currencyMap; // Our modifiable list of denominations. Final after initialization.
    private float amount; // Stores the argument we're currently processing in the appropriate format.

    // ----------------------------------------------------------------------------------------------------------------------------------------
    /**
     * Takes CLI args and prints the the amount using the fewest amount of denominations.
     * @args Our string amount representation.
    */
    public static void main(String[] args) {
        populateCurrencyMap();

        // Given any number of CLI args, do work on them; as long as they are valid.
        foreach(String arg : args) {
            amount = float(arg); // String Arg --> Convertable Float
            String result = "";

            // If our amount is valid, do work.
            if(amount) {
                // Iterate through from greatest to least denomination:
                foreach(float denomination : currencyMap) {
                    int remainder = convert(amount, denomination); // Calculate
                        // Is there a remainder?
                        if (remainder) {
                            amount -= remainder; // Update our current amount so that we can continue working on it.
                            finalResult = appendDenomination(money, denomination.get() ) + finalResult; // Reverse order (as originally desired).
                        }
                    // No? We're all done! Print and move on to the next amount.
                    else { System.out.println(finalResult); }
                }
            }
            else { System.out.println("Error: Invalid amount."); }// Could also be wrapped in a try block.
    }
    // ----------------------------------------------------------------------------------------------------------------------------------------
    /**
    * Creates our denomination map. Modifiable. Allows us to adjust to accommodate a variety
    * of currencies.
    */
    private void populateCurrencyMap() {
        // Populate greatest --> least so we iterate through in the correct order.
        currencyMap.put(100.00f, "100 dollar");
        currencyMap.put(50.00f, "50 dollar");
        currencyMap.put(20.00f, "20 dollar");
        currencyMap.put(10.00f, "10 dollar");
        currencyMap.put(5.00f, "5 dollar");
        currencyMap.put(1.00f, "dollar");
        // currencyMap.put(0.50f, "Half Dollar"); // Maybe? Hah.
        currencyMap.put(0.25f, "quarter");
        currencyMap.put(0.10f, "dime");
        currencyMap.put(0.01f, "cent");
    }
    // ----------------------------------------------------------------------------------------------------------------------------------------
    /**
     * Given our remaining amount and a certain denomination, do the conversion.
     * @arg amount The amount of money to be converted.
     * @arg denomination The dollar/coin value we want to use in our conversion.
     * @return How many times our denomination is expressed in our remaining cash amount.
    */
    private int convert(float amount, float denomination) {
        return currency = value % money;
    }
    // ----------------------------------------------------------------------------------------------------------------------------------------
    /**
    * @arg remainder The denomination amount calculated.
    * @ denomination The specific coin/dollar value used for the last calculation.
    * @ return The human readable, string result of our calculation.
    */
    private String appendDenomination(int remainder, String denomination) {
      for(int i = 0; i < remainder; ++i) {
        currency += "1 " + denomination;
      }
    }
    // ----------------------------------------------------------------------------------------------------------------------------------------
}
// --------------------------------------------------------------------------------------------------------------------------------------------
