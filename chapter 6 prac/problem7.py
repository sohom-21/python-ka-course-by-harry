# 7. Write a program to find out whether a given post is talking about "Harry" or not.
search_word1 = 'harry'
search_word2 = 'codewithharry'

user_post = input("Enter or type the post you want to talk about: ").lower()

if (search_word1 in user_post) or (search_word2 in user_post):
    print("The post is talking about Harry.")
else:
    print("The post is not talking about Harry.")