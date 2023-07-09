import openai

openai.api_key = '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'

def query(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def main():
    while True:
        user_query = input("Enter your query (or 'exit' to quit): ")
        
        if user_query.lower() == 'exit':
            break
        
        response = query(user_query)
        print("Response:", response)

if __name__ == '__main__':
    main()
