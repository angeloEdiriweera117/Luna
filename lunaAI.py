import google.generativeai as ai

# API KEY
API_KEY = 'AIzaSyBqvyI1lX62jvA5G5FE3mvE05z_U7hXT-Q'

# Configure the API
ai.configure(api_key = API_KEY)

# Create a new model
model = ai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat()

# Start a conversation
while True:
    message = input('You: ')
    if message.lower() == 'bye':
        print('Luna: Goodbye!')
        break
    response = chat.send_message(message)
    print('Luna: ', response.text)