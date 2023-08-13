# import openai

# Set your OpenAI API key
# openai.api_key = 'YOUR_API_KEY'


# 1.
# # Define your prompt
# prompt = "Once upon a time"

# # Generate a completion
# response = openai.Completion.create(
#     engine="text-davinci-003",  # GPT-3.5 engine
#     prompt=prompt,
#     max_tokens=50  # Maximum length of the response
# )

# # Get the generated completion
# completion = response.choices[0].text.strip()
# print(completion)




#2. role-based Completion api
# # Define the prompt with role-based content
# prompt = """
# Question: What are the capital cities of the following countries?
# Country: France
# Country: Germany
# Country: Italy

# Answer:
# """

# # Generate a completion
# response = openai.Completion.create(
#     engine="text-davinci-003",
#     prompt=prompt,
#     max_tokens=100
# )

# # Get the generated completion
# completion = response.choices[0].text.strip()
# print(completion)





#3. ChatCompletion api
# Create a list of messages for the conversation
# messages = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
# ]

# # Generate a completion with the chat conversation
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=messages
# )

# # Get the generated reply from the assistant
# reply = response.choices[0].message['content']
# print(reply)





# #4. Search api
# # Define the documents to search
# documents = [
#     "White House",
#     "hospital",
#     "school"
# ]

# # Define the query
# query = "The president"

# # Search the documents with the query
# response = openai.Engine("davinci").search(
#     documents=documents,
#     query=query
# )

# # Print the result
# print(response)
#





# #5. Answer api
# # Define the question
# question = "What is human life expectancy in the United States?"

# # Define the context
# context = """
# Life expectancy in the United States is 78 years.
# According to the U.S. Centers for Disease Control and Prevention,
# in 2017 the average life expectancy in the United States was 78.6 years.
# """

# # Generate an answer to the question
# response = openai.Answer.create(
#     search_model="ada",
#     model="curie",
#     question=question,
#     documents=[context],
#     examples_context="In 2017, U.S. life expectancy was 78.6 years.",
#     examples=[["What is human life expectancy in the United States?", "78 years."]],
#     max_tokens=5,
#     stop=["\n", "
# "]
# )

# # Print the result
# print(response)
#





# #6. Classification api
# # Define the documents to classify
# documents = [
#     "White House",
#     "hospital",
#     "school"
# ]

# # Define the query
# query = "The president"

# # Classify the documents with the query
# response = openai.Classification.create(
#     search_model="ada",
#     model="curie",
#     query=query,
#     labels=["politics", "public health", "education"],
#     documents=documents
# )

# # Print the result
# print(response)
#






# #7. File api
# # Define the file
# file = open("file.txt", "r")

# # Create the file
# response = openai.File.create(
#     file=file,
#     purpose="search"
# )

# # Print the result
# print(response)
#

# #8. FineTune api
# # Define the training data
# training_data = [
#     ["White House", "politics"],
#     ["hospital", "public health"],
#     ["school", "education"]
# ]

# # Fine-tune the model on the training data
# response = openai.FineTune.create(
#     training_data=training_data,
#     validation_data=training_data,
#     # model="curie",
#     # model="davinci",
#     model="ada",
#     epochs=3
# )

# # Print the result
# print(response)
#


