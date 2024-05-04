import os
from groq import Groq

def get_completion(
        content: str = "Explain the importance of fast language models",
        prompt: str = "you are a helpful assistant.",
        # model: str = "mixtral-8x7b-32768",
        model: str = "llama3-8b-8192",
        max_tokens: int = 50,
        temperature: float = 1
    ):

    """Return chat completion of input.

    Given some user text `content` as input, generate a chat completion using
    the Groq API and return it. Optionally specify which model to use, as well
    as how it should respond.

    Args:
        content (str): Some text to be passed to an LLM for completion.
        prompt (str): A text prompt to specify how the model should respond.
        model (str): The name of the model to request chat completion from.
        max_tokens (int): The maximum number of tokens the model's response may contain.
        temperature (float): The randomness of responses - larger values are more random. Accepts values > 0 and <= 2.

    Returns:
        completion (str): The model's chat completion response as text.
    """

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": content,
            }
        ],
        model=model,
        max_tokens=max_tokens
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    completion = get_completion()
    print(completion)
