import os
import openai

# Set your OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Define the system message for the assistant
system_message = "You are a funny, witty and sarcastic assistant."

# Define the conversation history with the system message
conversation = [
	{"role": "system", "content": system_message}
]

# Function to generate a response using the OpenAI ChatCompletion API
def generate_response(user_message):
	# Add user message to the conversation
	conversation.append({"role": "user", "content": user_message})

	# Generate a completion using the conversation history
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=conversation,
		max_tokens=30
	)

	# Get the system's response from the completion
	system_response = response.choices[0].message['content']

	# Add system response to the conversation
	conversation.append({"role": "system", "content": system_response})

	return system_response
