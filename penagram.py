def is_pangram(sentence):  
    # Define the set of all letters in the English alphabet  
    alphabet = set("abcdefghijklmnopqrstuvwxyz")  
    
    # Convert the input sentence to lowercase and create a set of characters  
    sentence_set = set(sentence.lower())  
    
    # Check if all letters of the alphabet are in the sentence  
    return alphabet.issubset(sentence_set)  

# User input  
user_input = input("Enter a sentence: ")  

# Check and display result  
if is_pangram(user_input):  
    print("The sentence is a pangram.")  
else:  
    print("The sentence is not a pangram.")
