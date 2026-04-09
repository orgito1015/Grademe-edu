#def vowel_count(s):
#    vowels = "aeiouAEIOU"
#    sum = 0
#    for c in s:
#        if c in vowels:
#            sum += 1
#    return sum


#def cryptic_sort(strings: list[str]) -> list:

#    return (sorted(strings, key=lambda s: (len(s), s.lower(), vowel_count(s))))
            
## Example usage:
#print(cryptic_sort(["A", "banana", "grape", "kiwi", "oArange"]))
#print(cryptic_sort(["a", "e", "b", "o", "u"]))
#print(cryptic_sort(["Arsen", "arsen", "ARSEN"]))


#def cryptic_sort(strings: list[str]) -> list[str]:
#    return sorted(strings, key=lambda s: (len(s), s.lower(), sum(char in "aeiouAEIOU" for char in s)))

## Example
#print(cryptic_sort(["A", "banana", "grape", "kiwi", "oArange"]))
#print(cryptic_sort(["a", "e", "b", "o", "u"]))
#print(cryptic_sort(["Arsen", "arsen", "ARSEN"]))
#print(cryptic_sort(["aaa", "AAA", "bbb", "BBB"]))


def cryptic_sort(strings: list[str]) -> list:
    return sorted(strings, key=lambda s: (len(s), s.lower(), sum(char in "aeuioAEUIO" for char in s)))