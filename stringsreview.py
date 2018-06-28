'''# Ask the user for their first and last
# names.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
# Print the user's full name below...

print(first_name, last_name)

def replace_at_index(word, index):
    word = list(word)
    word[index] = "-"
    word = ''.join(word)
    print(word)

replace_at_index("eggplant", 5)
'''
def reverse(word):
    result = ""
    for i in range(0, len(word) + 1):
        if i == 0:
            continue
        else:
            #print(word[0-i])
            result = result + word[0-i]
    print(result)        
reverse("Hello")
