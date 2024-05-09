import argparse
import sys
from .groqcli import get_completion
from .defaults import DEFAULT

def main():
    parser = argparse.ArgumentParser(
        description="A command line tool for chatting with LLMs through Groq."
    )
    parser.add_argument(
        "-p", "--prompt",
        type = str,
        default = DEFAULT['prompt'],
        help = "A text prompt to specify how the model should respond."
    )
    parser.add_argument(
        "-m", "--model",
        type = str,
        default = DEFAULT['model'],
        help = "The name of the model to request chat completion from."
    )
    parser.add_argument(
        "-k", "--max_tokens",
        type = int,
        default = DEFAULT['max_tokens'],
        help = "The max token cutoff for model responses."
    )
    parser.add_argument(
        "-t", "--temperature",
        type = float,
        default = DEFAULT['temperature'],
        help = "The randomness of responses - larger values are more random. Accepts values > 0 and <= 2."
    )
    parser.add_argument(
        "content",
        type = str,
        default = DEFAULT['content'],
        nargs = '*',
        help = "The query you have for the model."
    )

    args = parser.parse_args()

    # append any piped args
    # isatty breaks on windows; this could be improved
    if not sys.stdin.isatty():
        args = parser.parse_args(sys.stdin, args)

    args.content = ' '.join(args.content)
    # print(vars(args))

    response = get_completion(**vars(args))
    print(response)

if __name__ == "__main__":
    main()
