def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]


if __name__ == "__main__":
    for text in ["level", "Hello", "racecar", "A man a plan a canal Panama"]:
        print(is_palindrome(text))
