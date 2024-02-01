import openai

def chat_with_gpt(prompt, session_history, model, api_key):
	openai.api_key = api_key

	full_prompt = session_history + "\nHuman: " + prompt + "\nAI:"
	response = openai.Completion.create(
		model=model,
		prompt=full_prompt,
		max_tokens=150,
		temperature=0.7,
		stop=["\nHuman:", "\n"]
	)
	answer = response.choices[0].text.strip()
	new_history = session_history + "\nHuman: " + prompt + "\nAI: " + answer
	return answer, new_history

if __name__ == '__main__':
	session_history = ""
	while True:
		user_input = input("You: ")
		gpt_response, session_history = chat_with_gpt(user_input, session_history, api_key=api_key)
		print("GPT-3.5-turbo:", gpt_response)
