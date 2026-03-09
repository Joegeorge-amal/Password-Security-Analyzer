from character_check import analyzecharacters
from entropy import calculate_entropy
from strength import estimatestrength
from breachcheck import checkbreach

def main():
    password = input ("Enter password: ")
    char_result= analyzecharacters(password)
    entropy = calculate_entropy(password)
    strength = estimatestrength(password)
    breach_count = checkbreach(password)

    print("\n----Password Analysis----")
    print("length: ",len(password))
    print("Entropy: ",entropy,"bits")

    print("\nCountains: ")
    for key,value in char_result.items():
        symbol = "✔" if value else "✖"
        print(symbol,key)
    print("\nStrength: ", strength)
    if breach_count:
        print(f"\n\t⚠ Found in breaches {breach_count} times")
    else:
        print("\n✔ Not found in known breaches")

main()
