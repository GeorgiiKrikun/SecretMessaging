
i_0 = "\u200C"
i_1 = "\u200D"

import base64

def int_to_invisible_string(i: int) -> str:
    # Convert integer to binary reprsentation
    binary = bin(i)[2:]
    # Append 0s to make the length a multiple of 8
    while len(binary) % 8 != 0:
        binary = "0" + binary
    # Convert binary to invisible string
    result = ""

    for bit in binary:
        if bit == "0":
            result += i_0
        else:
            result += i_1
    return result

def int_from_invisible_string(s: str) -> int:
    # Convert invisible string to binary
    binary = ""
    for char in s:
        if char == i_0:
            binary += "0"
        else:
            binary += "1"
    # Convert binary to integer
    return int(binary, 2)

def make_string_invisible(s: str) -> str:
    result = ""
    s_b64 = base64.b64encode(s.encode()).decode()
    s_enc = s_b64.encode()
    for byte in s_enc:
        result += int_to_invisible_string(byte)

    return result

def make_string_visible(s: str) -> str:
    result = ""
    for i in range(0, len(s), 8):
        byte = s[i:i+8]
        result += chr(int_from_invisible_string(byte))
    result = base64.b64decode(result).decode()
    return result

def extract_important_symbols(s: str) -> str:
    result = ""
    for char in s:
        if char == i_0 or char == i_1:
            result += char
    return result



