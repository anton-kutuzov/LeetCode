package leetcode.hashTable.easy.KeyboardRow;


import java.util.HashMap;

/*
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:

Given:
["Hello", "Alaska", "Dad", "Peace"]
Result:
["Alaska", "Dad"]
*/
public class Solution {
    private static final HashMap<Character, Integer> CHART_TO_LINE = getChartToLineMap();

    public String[] findWords(String[] words) {
        int[] indexesOfWord = new int[words.length];
        int n = 0;
        for (int i = 0; i < words.length; i++) {
            if (isChartsFromOneLine(words[i].toLowerCase())) {
                indexesOfWord[n++] = i;
            }
        }
        String[] result = new String[n];
        for (int i = 0; i < n; i++) {
            result[i] = words[indexesOfWord[i]];
        }
        return result;
    }

    private boolean isChartsFromOneLine(String word) {
        if (word.isEmpty()) {
            return false;
        }
        boolean isChartsFromOneLine = true;
        int firstLetterLine = CHART_TO_LINE.get(word.charAt(0));
        for (int i = 1; i < word.length(); i++) {
            if (firstLetterLine != CHART_TO_LINE.get(word.charAt(i))) {
                isChartsFromOneLine = false;
                break;
            }
        }
        return isChartsFromOneLine;
    }

    private static HashMap<Character, Integer> getChartToLineMap() {
        return new HashMap<Character, Integer>() {
            {
                put('q', 1);
                put('w', 1);
                put('e', 1);
                put('r', 1);
                put('t', 1);
                put('y', 1);
                put('u', 1);
                put('i', 1);
                put('o', 1);
                put('p', 1);

                put('a', 2);
                put('s', 2);
                put('d', 2);
                put('f', 2);
                put('g', 2);
                put('h', 2);
                put('j', 2);
                put('k', 2);
                put('l', 2);

                put('z', 3);
                put('x', 3);
                put('c', 3);
                put('v', 3);
                put('b', 3);
                put('n', 3);
                put('m', 3);
            }
        };
    }
}
