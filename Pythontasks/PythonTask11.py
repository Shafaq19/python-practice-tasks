import re


def remove_parenthesis(words):
    words_without_braces = [re.sub(r"\(|\)", "", word) for word in words]
    return words_without_braces


if __name__ == '__main__':
    words = ["example (.com))", "w3resource", "github (.com)", "stackoverflow (.com)"]
    print("\n".join(remove_parenthesis(words)))
