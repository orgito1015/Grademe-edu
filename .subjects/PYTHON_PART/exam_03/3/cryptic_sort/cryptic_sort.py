def cryptic_sort(strings: list) -> list:
    return sorted(strings, key=lambda s: (len(s), s.lower(), sum(char in "aeiouAEIOU" for char in s)))
