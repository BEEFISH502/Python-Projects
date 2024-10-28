import openai


##Set Open AI key here##
openai.api_key = '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'

def get_code_snippet(prompt):
	"""This function sends a request to the OpenAI API with a prompt to generate code and returns the response"""
	try:
	 	response = openai.ChatCompletion.create(
	 		model="get-3.5-turbo", 
	 		messages=[
	 		{"role": "system", "content": "Yes, Senpai."}, 
	 		{"role": "user", "content": prompt}
	 		],
	 		max_tokens=150,
	 		temperature=0.5,
	 	)
	 	return response['choices'][0]['message']['content'].strip()
	except Exception as e:
	 	return f"Error: {str(e)}"
	 			
	 			###This function will send a request to the OpenAI API with a prompt to explain code and returns the explanation###

def get_code_explanation(prompt):
	explanation_prompt = f"Explain the folowing code in detail:\n\n{prompt}"
	try: 
		response = openai.ChatCompletion.create(
			engine="get-3.5-turbo",
			messages=[
			{"role": "system", "content": "Yes, Senpai"},
			{"role": "user", "content": explanation_prompt}
			],
			max_tokens=200,
			temperature=0.7,
		)
		return response.choices[0].text.strip()
	except Exception as e:
		return f"Error:[str(e)]"

def main():
	print("Welcome to C.O.D.E Lyoko")
	while True:
		user_input = input ("What are we coding today, senpai?")


		if user_input.lower() in ['quit', 'exit']:
			print("Goodbye")
			break

##Now we generate code based on user input##
		code = get_code_snippet(user_input)
		print("\nGenerated Code:\n", code)

##Now Explain, ONE TIME ;)##
		explanation = get_code_explanation(code)
		print("\nExplanation\n", explanation)

if __name__ == '__main__':
	main()

