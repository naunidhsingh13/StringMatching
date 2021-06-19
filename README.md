# StringMatching
Collection of String Matching Algorithms

### Problem Statement :- 
For a given string *text* of length *n* *(n>0)* and a given string *pattern* find the all the occurrences of *pattern* of length *m (m>0)* in *text*.
Return the all the starting indices.

### Approach :-

 * Naive Approach: Iterate over each index from 0 to *n-m* and compare each substring of length *m*
 * RabinKarp : Use a Rolling hash function for each substring and first compare the value of the rolling hash function.
 * KMP : Create a Pi table Maintaining the length of prefix which is also a suffix for the *pattern* string. And move steps using this pi table instead of back tracking entire length *m*.
