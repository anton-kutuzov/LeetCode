package leetcode.strings.easy.UniqueMorseCodeWords;


import java.util.HashSet;

/*
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.
Return the number of different transformations among all words we have.
Example:
Given:
words = ["gin", "zen", "gig", "msg"]
Result:
2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
*/
public class Solution {
    private static final String[] CODE = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
            ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};

    public int uniqueMorseRepresentations(String[] words) {
        int shift = 'a';
        HashSet<String> morses = new HashSet<>(words.length);
        for (String word: words) {
            StringBuilder morse = new StringBuilder();
            for (int codeChar: word.toCharArray()) {
                morse.append(CODE[codeChar - shift]);
            }
            morses.add(morse.toString());
        }
        return morses.size();
    }
}
