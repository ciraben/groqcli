import os
from groq import Groq
from .defaults import DEFAULT

def get_completion(
        content: str = DEFAULT['content'],
        prompt: str = DEFAULT['prompt'],
        model: str = DEFAULT['model'],
        max_tokens: int = DEFAULT['max_tokens'],
        temperature: float = DEFAULT['temperature']
    ):

    """Return chat completion of input.

    Given some user text `content` as input, generate a chat completion using
    the Groq API and return it. Optionally specify which model to use, as well
    as how it should respond.

    Args:
        content (str): Some text to be passed to an LLM for completion.
        prompt (str): A text prompt to specify how the model should respond.
        model (str): The name of the model to request chat completion from.
        max_tokens (int): The max token cutoff for model responses.
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
        max_tokens=max_tokens,
        temperature=temperature
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    completion = get_completion()
    print(completion)
