

# Complete the solve function below.
def solve(s):
    words = re.split(r'(\s+)', s)
    words_list = [word.capitalize() if word.isalpha() else word for word in words]
    finalStr = ''.join(words_list)
    return finalStr


