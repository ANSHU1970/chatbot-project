import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "what is color of the sky"}])
print(completion.choices[0].message.content)