from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a weatherman, local to the area provided by the weather information you will recieve. Give a weather report based on this information, addinf some local flair."}
    ]
)

print(completion.choices[0].message)