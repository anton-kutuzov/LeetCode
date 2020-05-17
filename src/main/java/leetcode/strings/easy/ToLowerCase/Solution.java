package leetcode.strings.easy.ToLowerCase;


/*
mplement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example:

Given:
"Hello"
Result:
"hello"
*/
public class Solution {
    public String toLowerCase(String str) {
        StringBuilder lowerCaseSrt = new StringBuilder();
        int codeA = 'A';
        int codeLowA = 'a';
        int codeZ = 'Z';
        int codeLowZ = 'z';
        int difBetweenCases = codeA - codeLowA;
        for (int i = 0; i < str.length(); i++) {
            int code = str.charAt(i);
            if (code >= codeLowA && code <= codeLowZ) {
                lowerCaseSrt.append(str.charAt(i));
            } else if(code >= codeA && code <= codeZ) {
                lowerCaseSrt.append(((char)(((int)str.charAt(i)) - difBetweenCases)));
            } else {
                lowerCaseSrt.append(str.charAt(i));
            }
        }
        return lowerCaseSrt.toString();
    }
}
