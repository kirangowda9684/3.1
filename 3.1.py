def prefixstrng(strings, prefix):
     return [s for s in strings if s.startswith(prefix)]
strings =  ['cat', 'car', 'fear', 'center']
prefix = "ca"
print("Given string:")
print(strings)
print("prefix of the string:", prefix)
print("the strings that starts with", prefix)
print(prefixstrng(strings, prefix))
strings =  ['cat', 'dog', 'shatter', 'donut', 'at', 'todo']
prefix = "do"
print("\nGiven string:")
print(strings)
print("prefix of the string:", prefix)
print("the strings that starts with", prefix)
print(prefixstrng(strings, prefix))