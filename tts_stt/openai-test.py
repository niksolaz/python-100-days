import os
import openai

client = openai.OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

try:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    print(completion.choices[0].message)
except openai.RateLimitError:
    print("You have exceeded your API rate limit.")
    