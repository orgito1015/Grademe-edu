def string_sculptor(text : str) -> str:
    result = ""
    index_leter = 0

    for i, char in enumerate(text):
        if char.isalpha():
            if index_leter % 2 == 0:
                result += char.lower()
            else:
                result += char.upper()
            index_leter += 1
        else:
            result += char

    return result

a = string_sculptor("Heello/123 World")

print(a)