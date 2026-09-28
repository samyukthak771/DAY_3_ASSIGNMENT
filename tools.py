def calculator(expression):
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as error:
        return f"Calculation error: {error}"


if __name__ == "__main__":
    print("Calculator Tool Test")
    print("10 + 20 =", calculator("10 + 20"))
    print("50 * 2 =", calculator("50 * 2"))