"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania", "SA": "South Australia"}

state_name = input("Enter short state: ").upper()
while state_name != "":
    if state_name in CODE_TO_NAME:
        print(state_name, "is", CODE_TO_NAME[state_name])
    else:
        print("Invalid short state")
    state_name = input("Enter short state: ").upper()