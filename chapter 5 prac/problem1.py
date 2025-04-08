#1. Write a program to create a dictionary of Hindi words with values as their
# English translation. Provide user with an option to look it up!

hindi_dictionary = {
    "madad":"Help",
    "kursi":"chair",
    "billi":"cat"
}
user_word = hindi_dictionary.get(input("Enter the hindi word to see the english translation: "))
if user_word:
    print(user_word)
else:
    print("abhi translation nahi hai uska")
