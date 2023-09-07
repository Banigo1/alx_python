#!/usr/bin/env python3
"""
Script that lists all strings that contain the letter 'a' from the given input list
"""

if __name__ == "__main__":
    # Input list of strings
    strings = [
        "PaDEBU", "Va667Q", "K83J6a", "Y48EHa", "a0SNW7", "CaSS85", "HSTaC4", "F9Va5K", "WaYIQ7",
        "aRSY3H", "KQPYVa", "ILZ1Ta", "6RL4Ga", "EZaL7Z", "aDRYXW", "a0UY7P", "MCWKaI8", "aSZYCX",
        "TYaVLB", "B1aEDS", "Ta0B54", "QTMa6O", "4KLDKa", "7FL9aZ", "JaOKHI", "a764FI", "6R7T2a",
        "aaR49M", "6aJ56U", "TaaYVY", "0G5a9Z", "EM3C7a", "FY1WaY", "F3aQaN", "KZXCZa", "75aIVI",
        "aaNUI4", "B37OZa", "aFZ9WB", "VaKRP3", "GXaGTE", "J78MXa", "aFOLIE", "CXGJa9", "Ja4OF0",
        "YT7aaF", "X61aSX", "a3EMX5", "VBKa7O", "TBa48U", "aGOPMI", "QaFHD8", "6329aL", "aN748Z",
        "JP9aK3", "C2FaM4", "6a7YQG", "4E5KaB", "2aNF9T", "63U9Sa", "9CJa9L", "1aCX06", "aR20aC",
        "09aKC0", "NVaaVX", "EaWGKO", "Q51aXK", "XC2BPa", "a4ECUI", "ZVNNGa", "PDEa54", "aLLSSL",
        "LCCaOF", "07aHIZ", "50MXaV", "1aBGKP", "TRX45a", "POaQ22", "89aP15", "XR6IaX", "MaJN4I",
        "Ha42KO", "TNVLa5", "FL4MaF", "QaXHDS", "EBP80a", "R5aLUL", "VLOaVM", "Ga9JSH", "9RLHa9",
        "E5Va0P", "JaV24U", "aY5BBB", "Xa4Ha"
    ]

    # Print the results in the expected format
    for index, string in enumerate(strings, start=1):
        print(f"{index}: {string}")

