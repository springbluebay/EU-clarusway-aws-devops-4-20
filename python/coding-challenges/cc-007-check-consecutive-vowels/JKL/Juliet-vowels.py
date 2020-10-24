def vowels(string):
    vowels_characters = ("a", "e", "o", "ö", "u", "ü", "i", "ı")
    string = string.lower()
    string_len = len(string)
    for i in range(0, string_len):
        if string_len > 1 and string[i] in vowels_characters and string[i + 1] in vowels_characters:
            print("Positive")
            return "Positive"
    print("Negative")
    return "Negative"

vowels("gasdph")
vowels("aiou")
vowels("taoum")
vowels("a")