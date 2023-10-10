import re
import long_res as lr  # Importing  module 'long_res' for long responses


# Function to calculate the response probability based on recognized words and keywords
def response_probability(user_res, recogised_words, single_res=False, keywords=[]):
    temprature = 0  # Variable to count recognized words
    has_keywords = True  # Flag to check if user message contains all keywords

    # Loop through each word in the user's response
    for word in user_res:
        if word in recogised_words:
            temprature += 1  # Increment the count if the word is recognized
    
    # Calculating the accuracy of recognized words in a user message
    accuracy = float(temprature) / float(len(recogised_words))

    # Loop through the provided keywords to check if they all exist in the user's response
    for word in keywords:
        if word not in user_res:
            has_keywords = False
            break

    # If user message contains all keywords or single_res flag is True, return accuracy as an integer percentage
    if has_keywords or single_res:
        return int(accuracy * 100)
    else:
        return 0

# Function to check and select the best response based on probabilities
def check_Response(text):
    highest_prob_list = {}  # Dictionary to store response probabilities

    # Nested function to calculate response probability and store it in highest_prob_list
    def response(bot_res, list_of_words, single_res=False, keywords=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_res] = response_probability(text, list_of_words, single_res, keywords)

    # Define responses and their associated recognized words and keywords
    response('Hello!', ['hello', 'hi', 'wassup', 'ssup', 'sup', 'hey', 'heyo', 'heya'], single_res=True)
    response('I\'m doing great! How about you?', ['how', 'are', 'you', 'u', 'r'], keywords=['how'])
    response('Thank You!', ['you', 'u', 'r', 'are', 'amazing', 'good', 'best'], keywords=['you', 'amazing'])
    response(lr.eat, ['What', 'you', 'eat'], keywords=['you', 'eat'])
    response('Glad to hear that!', ['i', 'im', 'i\'m', 'am', 'great', 'fine', 'good'], keywords=['fine'])
    response(lr.facts, ['tell', 'me', 'something'], keywords=['something'])

    # Find the response with the highest probability
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    # Return the response with the highest probability, or 'unknown' if the probability is less than 1%
    return lr.unknown() if highest_prob_list[best_match] < 1 else best_match

# Function to split and check user input and get the best response
def getResponse(res):
    split_text = re.split(r'\s+|[,;?!.-]\s*', res.lower())  # Split user input into words
    response = check_Response(split_text)  # Get the best response based on the input
    return response

# Main loop for continuous interaction with the user
while True:
    print('Bot: ' + getResponse(input("User: ")))  # Print the bot's response based on user input
