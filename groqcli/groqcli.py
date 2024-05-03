import os
from groq import Groq

def foo():
    """Summary line.

    Extended description of function.

    Args:
        foo (str): Description of arg1

    Returns:
        str: Description of return value
    """

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the importance of fast language models",
            }
        ],
        model="mixtral-8x7b-32768",
    )

    print(chat_completion.choices[0].message.content)


    return "foo"


if __name__ == "__main__":
    foo()
