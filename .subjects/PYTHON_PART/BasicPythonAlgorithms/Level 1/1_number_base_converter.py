#Write a function that converts a number from one base to another.Supported bases from 2 to 36 in clusive, using digits 0-9 and letters A-Z for values 10-35.Return  "ERROR" for invalid inputs(base,digits)
#def number_base_converter(number: str, from_base: int, to_base: int) -> str:

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    try:
        num = int(number, from_base)
    except:
        return "ERROR"

    if num == 0:
        return "0"

    result = ""
    while num > 0:
        result = digits[num % to_base] + result
        num //= to_base

    return result

print(number_base_converter("1010", 2, 10))  # Output: "10"
print(number_base_converter("1A", 16, 10))    # Output: "26"
print(number_base_converter("Z", 36, 10))     # Output: "35"
print(number_base_converter("123", 10, 2))    # Output: "1111011"
print(number_base_converter("123", 10, 37))   # Output: "ERROR"
print(number_base_converter("1G", 16, 10))    # Output: "ERROR"
print(number_base_converter("1A", 10, 16))    # Output: "ERROR"
