# operators_classifier_tool

 Line-by-Line Explanation of code

*import re
We import Python’s regular expressions module, re, to help us search for operators inside a string.

*OPERATORS = { ... }
This dictionary holds all the operators grouped into categories:

"Arithmetic" includes basic math operators.

"Assignment" includes all types of assignment (like +=, *=,-=,/=).

"Comparison" includes things like ==, !=, <, etc.

"Logical" includes and, or, not.

"Identity" includes is, is not.

"Membership" includes in, not in.

"Bitwise" includes &, |, ~, <<, etc.

We’ll use this structure to match operators and figure out what group they belong to.

*operator_lookup = {}
We create a new dictionary to map each individual operator (e.g., '+') back to its group (e.g., 'Arithmetic').

*for group, ops in OPERATORS.items():
Loop through every group and its list of operators.

*operator_lookup[op] = group
Each operator string gets stored as a key in operator_lookup, and its value is the name of the group it belongs to.
This makes it easy to look up the group of any operator in one step later.

*sorted_ops = sorted(operator_lookup.keys(), key=len, reverse=True)
To correctly match operators, we sort them by length in descending order. Why?

 So **= is matched before *, and is not is matched before is.

Otherwise, a longer operator might be misinterpreted as multiple shorter ones.

*pattern = r"|".join(map(re.escape, sorted_ops))
We build a regular expression pattern that will match any operator.

re.escape() escapes any special characters in operators (like *, |, etc.).

join(..., "|") joins them with |, which means “or” in regex.

*def classify_operators(code: str):
This function takes a string of Python code and returns a dictionary showing which operators were found in which group.

*matches = re.findall(pattern, code)
We use re.findall to extract all operators from the input code based on our pattern.

*classification = {group: [] for group in OPERATORS}
We make a results dictionary to hold our final answer. Each group (Arithmetic, Logical, etc.) starts with an empty list of matched operators.

*for match in matches:
Loop through every matched operator found in the code.

 group = operator_lookup.get(match)
Look up what group that operator belongs to.

if group and match not in classification[group]:
If we found a valid group, and we haven’t already added this operator to the result for that group...

 classification[group].append(match)
...add it to the list.

*return classification
Once all operators are processed, return the final grouped result.

*if __name__ == "__main__":
This ensures the below code only runs when we directly execute this script.

*print("Operator Classifier Tool")
Friendly message when the program starts.

*code = input("Enter a Python expression: ")
Take input from the user (a line of Python code).

*result = classify_operators(code)
Analyze the input to classify all operators using the function we defined.

*Print results
python
Copy
Edit
for group, ops in result.items():
    if ops:
        print(f"{group}: {', '.join(ops)}")
For every group that had matches, print the group and the list of operators found in it.
