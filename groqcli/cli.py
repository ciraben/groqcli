import argparse
from groqcli import get_completion

def main():
    parser = argparse.ArgumentParser(
        description=""
    )
    # parser.add_argument(
    #     "-m", "--model",
    #     type = str,
    #     help = "The model you'd like to chat with."
    # )
    parser.add_argument(
        "content",
        type = str,
        nargs = '*',
        help = "The query you have for the model."
    )

    args = parser.parse_args()
    # print()
    # return
    response = get_completion(
        content = ' '.join(args.content)
    )
    print(response)

if __name__ == "__main__":
    main()
