import re
from typing import Tuple

from cv2 import sort

PRICE_REGEX = "[0-9]*\.[0-9]{2}"
NAME_REGEX = "[a-zA-Z/]+(?:[a-zA-Z/]+\s)*[a-zA-Z/]+"
SKIP_REGEX = "@"
END_REGEX = "BALANCE|SUBTOTAL|TOTAL"
TAX_REGEX = "TAX\s[0-9]*\.[0-9]{2}"


def validate_line(line: str) -> str:
    has_price: bool = re.search(PRICE_REGEX, line)
    has_name : bool = re.search(NAME_REGEX, line)
    has_skip : bool = re.search(SKIP_REGEX, line)
    
    has_end : bool = re.search(END_REGEX, line)
    names: list = re.findall(NAME_REGEX, line)
    if len(names) > 0 and max(names, key=lambda s: len(s)) == "TAX":
        has_end = True

    if len(names) > 0 and len(max(names, key=lambda s: len(s))) < 5:
        has_skip = True
    

    valid: bool = has_price and has_name and not has_skip and not has_end

    if valid:
        return "valid"
    elif has_end:
        return "end"
    else:
        return "skip"

def parse_line(line: str) -> Tuple[str, int]:
    name:str = max(re.findall(NAME_REGEX, line), key=lambda s: len(s))
    price_str:str = re.search(PRICE_REGEX, line).group(0)
    price:int = parse_price(price_str)
    

    return (name, price)

def parse_price(price_str: str) -> int:
    print(price_str)
    dollar, cent = tuple( [int(num) for num in ("0" + price_str).split(".")] )
    return dollar * 100 + cent

def parse_tax(text: str) -> int:
    
    match:re.Match = re.search(TAX_REGEX, text)
    if match:
        price_str:str = match.group(0).split(" ")[1]
        return parse_price(price_str)
    else:
        return 0

def parse_text(text: str) -> list[Tuple[str, int]]:
    lines : list[str] = text.split("\n")
    outputs : list[Tuple[str, int]]= []
    
    for line in lines:
        validation:str = validate_line(line)

        if validation == "valid":
            outputs.append(parse_line(line))
        elif validation == "end":
            break

    return outputs

def parse_receipt(text: str) -> Tuple[list[Tuple[str, int]], int]:
    return parse_text(text), parse_tax(text)