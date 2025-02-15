name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# Use f-string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,036!
print(f"{year} {name} for about {cost:,.0f}!")

# Using a for loop with the range function and f-string formatting,
# produce the following right-aligned output (DO NOT use a list):

for integer in range(1,11):
    number = 2 ** integer
    print(f"2 ^{integer:>2} is {number:>4}")