import os
from groq import Groq

def complete(content: String = "Explain the importance of fast language models"):
    """Print some content's completion to the terminal.

    Extended description of function.

    Args:
        content (str): Some text to be passed to an LLM for completion.

    Returns:
        None
    """

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    print(chat_completion.choices[0].message.content)
    return

if __name__ == "__main__":
    complete()
