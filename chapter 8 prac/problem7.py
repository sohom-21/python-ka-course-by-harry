# Write a python function to remove a given word from a list ad strip it at the same time.
def word_remove(wordlist, wordsearch):
    """
    Remove a word from a list and strip whitespace from all remaining words.
    Returns the modified list.
    """
    # Strip whitespace from all words first
    wordlist = [word.strip() for word in wordlist]

    # Try to remove the word
    try:
        wordlist.remove(wordsearch)
        print(f"Word '{wordsearch}' removed successfully.")
    except ValueError:
        print(f"The search value '{wordsearch}' is not in the list.")

    return wordlist


def main():
    # Get input and immediately split and strip
    user_input = input('Enter words separated by commas: ')
    wordlist = [word.strip() for word in user_input.split(',')]

    wordsearch = input('Enter the word you want to remove: ').strip()

    # Call the function and store the result
    result = word_remove(wordlist, wordsearch)
    print("Final list:", result)


if __name__ == "__main__":
    main()

# This is a common Python pattern that makes the script run the main() function when executed directly
# If this file is imported by another script, main() won't automatically run