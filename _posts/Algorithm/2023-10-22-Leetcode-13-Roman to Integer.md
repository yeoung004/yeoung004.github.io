# Converting Roman Numerals to Integers in Python

> Roman numerals have been used since ancient times and have a unique representation using specific characters. Today, I will explore an algorithm to convert a string representation of a Roman numeral into its integer form in Python.

### Mapping Roman Numerals:

The key to this algorithm lies in the mapping of Roman numerals to their respective integer values:

```
roman = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}
```
This dictionary provides a straightforward way to look up the integer value of a given Roman numeral.

### The Algorithm:

I've created a Solution class that houses the function romanToInt. The idea is to traverse the Roman numeral string and continuously add the respective integer values to our result:

```
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            try:
                result += roman[s[i: i + 2]]
                i += 1
            except KeyError:
                result += roman[s[i]]
            i += 1

        return result
```

The logic is as follows:

1. Initialize result to 0, which will hold our final integer value.
2. Use a while loop to traverse through the string.
3. Attempt to match two characters of the string with our dictionary. If 
4. it's a match (like "CM", "XC", etc.), add its corresponding integer value to the result.
5. If there's a KeyError (meaning the two characters are not in our dictionary), then we match only the single character and add its integer value.
6. Move the index accordingly to continue the traversal.

### Excute Code:

```
if __name__ == '__main__':
    print(Solution().romanToInt("LVIII"))
```

This will output 58, as "L" represents 50, "V" represents 5, and "III" represents 3, summing up to 58.

### Conclusion:

> This Python-based solution efficiently converts Roman numerals to integers. By leveraging dictionary lookups and some careful string traversal, we can handle both the standard Roman numeral characters and the special two-character cases.