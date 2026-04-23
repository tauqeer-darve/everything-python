while True:
    user_input: str = input('You: ')

    if user_input == 'Hello':
        print('Bot: Hello!')
    elif user_input == 'How are you?':
        print('Bot: Good, what about you')
    elif user_input == 'Bye':
        print('Bot: Goodbye!')
    else:
        print('Bot: Sorry, I did not understand that.')