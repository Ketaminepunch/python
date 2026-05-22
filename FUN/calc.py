
from decimal import Decimal
import requests

EURO = [
    (Decimal("500"),  "500€",  "Bills"),
    (Decimal("200"),  "200€",  "Bills"),
    (Decimal("100"),  "100€",  "Bills"),
    (Decimal("50"),   "50€",   "Bills"),
    (Decimal("20"),   "20€",   "Bills"),
    (Decimal("10"),   "10€",   "Bills"),
    (Decimal("5"),    "5€",    "Bills"),
    (Decimal("2"),    "2€",    "Coins"),
    (Decimal("1"),    "1€",    "Coins"),
    (Decimal("0.50"), "50c",   "Cents"),
    (Decimal("0.20"), "20c",   "Cents"),
    (Decimal("0.10"), "10c",   "Cents"),
    (Decimal("0.05"), "5c",    "Cents"),
    (Decimal("0.02"), "2c",    "Cents"),
    (Decimal("0.01"), "1c",    "Cents"),
]

DOLLAR = [
    (Decimal("100"),  "100$",  "Bills"),
    (Decimal("50"),   "50$",   "Bills"),
    (Decimal("20"),   "20$",   "Bills"),
    (Decimal("10"),   "10$",   "Bills"),
    (Decimal("5"),    "5$",    "Bills"),
    (Decimal("2"),    "2$",    "Bills"),
    (Decimal("1"),    "1$",    "Bills"),
    (Decimal("0.25"), "25c",   "Cents"),
    (Decimal("0.10"), "10c",   "Cents"),
    (Decimal("0.05"), "5c",    "Cents"),
    (Decimal("0.01"), "1c",    "Cents"),
]
def getdenom(den:str):

    if den == "€" or den == "euro".casefold():
        return EURO
    elif den == "$" or den == "dollar".casefold():
        return DOLLAR
    
def CalcNotes(rest: Decimal,den: list[tuple[Decimal, str, str]]):
    sections: dict[str,list[str]] = {}
    for amount,label,section in den:
        n = int(rest // amount)
        if n>0:
            rest-=amount*n
            sections.setdefault(section, []).append(f"{n}x{label}")
    return sections
   
    

if __name__ == "__main__":
    denom = getdenom(input("Enter denomination Dollar or Euro: "))
    price = Decimal(input("Enter price: "))
    given = Decimal(input("Enter given: "))
    
    
    sections = CalcNotes((given - price),denom)
    
    for section, items in sections.items():
        print(f"{section}: {', '.join(items)}")
