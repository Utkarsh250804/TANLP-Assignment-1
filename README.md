# TANLP-Assignment-1

NLP-Assignment
HOW NLP is used for text to speech conversion and vice-versa

## ASSIGNEMNET-1 
nltk.download('punkt') and nltk.download('averaged_perceptron_tagger'): Downloads the necessary datasets for tokenization and POS tagging. nltk.word_tokenize(sentence): Tokenizes the input sentence into individual words. nltk.pos_tag(words): Tags each word in the list with its corresponding part of speech. The loop prints each word along with its POS tag.

Each word is followed by its POS tag, such as NNP for proper noun, VBZ for the verb, 3rd person singular present, DT for determiner, JJ for adjective, and NN for a noun.

## ASSIGNMENT-2

Predefined Responses: A dictionary predefined_responses is used to store possible questions (keys) and their corresponding answers (values). Input Processing: The chatbot converts the user input to lowercase and tokenizes it to handle different forms of input effectively. Keyword Matching: It checks if any of the predefined questions (or keywords) are present in the user input. If found, it returns the associated response. User Interaction: The chatbot runs in a loop, taking input from the user and responding until the user types "bye".

ChatBot: Hello! I'm a simple chatbot. Ask me anything or type 'bye' to exit. You: Hello ChatBot: Hi there! How can I help you today? You: What is your name? ChatBot: I am a chatbot created to assist you. You can call me ChatBot! You: How are you? ChatBot: I'm just a bot, but I'm doing great! How about you? You: What can you do? ChatBot: I can answer basic questions and have a simple conversation with you. Try asking me something! You: Bye ChatBot: Goodbye! Have a great day!
