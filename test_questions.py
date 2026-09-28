from config import client, MODEL
from tools import calculator
import json


questions = [
    "What is 15% of 18000?",
    "What is 25% of 12000?",
    "What is the capital of France?"
]


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


for question in questions:

    print("\n====================================")
    print("Question:", question)

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

    if message.tool_calls:

        for tool_call in message.tool_calls:

            print("Tool requested:", tool_call.function.name)

            args = json.loads(tool_call.function.arguments)

            print("Arguments:", args)

            result = calculator(args["expression"])

            print("Tool result:", result)

    else:

        print("No tool requested.")
        print("LLM Answer:", message.content)