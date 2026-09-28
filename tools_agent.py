from config import client, MODEL
from tools import calculator


question = "What is 15% of 18000?"

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to calculate."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": question
        }
    ],
    tools=tools,
    temperature=0
)


message = response.choices[0].message


print("=== TOOL ENABLED RUN ===")
print("Question:", question)

if message.tool_calls:
    for tool_call in message.tool_calls:
        expression = tool_call.function.arguments

        print("Tool requested:", tool_call.function.name)
        print("Arguments:", expression)

        import json
        args = json.loads(expression)

        result = calculator(args["expression"])

        print("Tool result:", result)
else:
    print("No tool call was requested.")

print("Answer:", message.content)