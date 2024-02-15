i1 = "\u200B"
i2 = "\u200C"
i_delimiter = "\u200D"

import base64

def int_to_invisible_string(i: int) -> str:
    # Convert integer to binary reprsentation
    binary = bin(i)[2:]
    # Convert binary to invisible string
    result = ""
    for bit in binary:
        if bit == "0":
            result += i1
        else:
            result += i2
    return result

def int_from_invisible_string(s: str) -> int:
    # Convert invisible string to binary
    binary = ""
    for char in s:
        if char == i1:
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
        result += i_delimiter

    return result

def make_string_visible(s: str) -> str:
    result = ""
    s = [x for x in s.split(i_delimiter) if x != '']
    for byte in s:
        result += chr(int_from_invisible_string(byte))
    result = base64.b64decode(result).decode()
    return result

def extract_important_symbols(s: str) -> str:
    result = ""
    for char in s:
        if char == i1 or char == i2 or char == i_delimiter:
            result += char
    return result



