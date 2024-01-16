import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "essay about a panda"}])
print(completion.choices[0].message.content)