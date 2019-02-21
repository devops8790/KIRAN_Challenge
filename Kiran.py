import re
r = re.compile(r"^(?!.*?(\d)(?:\D?\1){4})[4-6]\d{3}(?:-?\d{4}){3}$")

card = input("Enter a card number")

check = r.search(card)
if check:
	print("Valid")
else:
	print("invalid")
    