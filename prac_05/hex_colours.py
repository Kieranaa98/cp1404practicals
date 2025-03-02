COLOUR_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a",
                "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
                "Amaranth": "#e52b50", "Amber": "#ffbf00",
                "Amethyst": "#9966cca", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc" }

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    if colour_name in COLOUR_CODE:
        print(colour_name, "is", COLOUR_CODE[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()