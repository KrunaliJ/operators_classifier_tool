
import re

# Operator groups
OPERATORS = {
    "Arithmetic": ["+", "-", "*", "/", "//", "%", "**"],
    "Assignment": ["=", "+=", "-=", "*=", "/=", "//=", "%=", "**=", "&=", "|=", "^=", ">>=", "<<="],
    "Comparison": ["==", "!=", ">", "<", ">=", "<="],
    "Logical": ["and", "or", "not"],
    "Identity": ["is", "is not"],
    "Membership": ["in", "not in"],
    "Bitwise": ["&", "|", "^", "~", "<<", ">>"]
}

# Flatten operator list and build a reverse lookup
operator_lookup = {}
for group, ops in OPERATORS.items():
    for op in ops:
        operator_lookup[op] = group

# Sort operators by length (to match multi-char first)
sorted_ops = sorted(operator_lookup.keys(), key=len, reverse=True)
pattern = r"|".join(map(re.escape, sorted_ops))

def classify_operators(code: str):
    matches = re.findall(pattern, code)
    classification = {group: [] for group in OPERATORS}
    
    for match in matches:
        group = operator_lookup.get(match)
        if group and match not in classification[group]:
            classification[group].append(match)
    
    return classification

# Example
if __name__ == "__main__":
    print("Operator Classifier Tool")
    code = input("Enter a Python expression: ")

    result = classify_operators(code)
    
    print("\nOperator Groups Found:")
    for group, ops in result.items():
        if ops:
            print(f"{group}: {', '.join(ops)}")
