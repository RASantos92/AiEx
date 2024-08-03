from openai import OpenAI
import json
import env
client = OpenAI(api_key=env.myGptkey)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "write a haiku about ai"}
    ]
)


print(type(completion))

# Write the completion information to a JSON file
with open("completion_data.json", "w") as json_file:
    json.dump(completion, json_file, indent=4)

# Print confirmation
print("Completion data saved to completion_data.json")