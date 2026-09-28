from config import client, MODEL


question = "What is 15% of 18000?"


response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": question
        }
    ],
    temperature=0
)


answer = response.choices[0].message.content


print("=== NO TOOL RUN ===")
print("Question:", question)
print("Answer:", answer)
