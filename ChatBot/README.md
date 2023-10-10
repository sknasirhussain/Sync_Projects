# Chat Bot with Response Probability

This Python code implements a simple chat bot that responds to user input based on the probability of recognizing words and keywords in the user's message. The bot selects the best response from a predefined set of responses.

## How it works

The code consists of several functions:

### `response_probability(user_res, recognized_words, single_res=False, keywords=[])`

This function calculates the response probability based on recognized words and keywords in the user's message. It counts how many recognized words are present in the user's response and checks if all provided keywords are present.

- `user_res`: List of words in the user's message.
- `recognized_words`: List of words that the bot recognizes.
- `single_res`: Flag indicating if a single response is required.
- `keywords`: List of keywords to check in the user's response.

### `check_Response(text)`

This function selects the best response based on probabilities. It iterates through a predefined set of responses and calculates the probability of each response using `response_probability`. The response with the highest probability is selected.

- `text`: List of words in the user's message.

### `getResponse(res)`

This function splits the user's input into words and calls `check_Response` to get the best response based on the input.

- `res`: User's input as a string.

### Main Loop

The code includes an infinite loop that continuously interacts with the user. It takes user input, processes it using `getResponse`, and prints the bot's response.

## Usage

1. Ensure you have Python installed on your system.

2. Run the script in a Python environment.

```bash
python chat_bot.py
```

3. The bot will continuously prompt for user input and provide responses based on the recognition probabilities.

## Responses

The code includes predefined responses and associated recognized words and keywords. You can customize these responses and recognition criteria to fit your chat bot's purpose.

## Requirements

- Python 3.x
- `re` module (Python's built-in regular expression module)

## Author

SK Nasir Hussain

