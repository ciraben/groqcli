# groqcli 🥦

A command line tool for chatting with LLMs through Groq.

### install

Clone the repo and install with `pip install /dir/to/groqcli`.

### setup

Add your [**Groq API key**](https://console.groq.com/keys) as an environment variable called `GROQ_API_KEY`.

```zsh
$ echo 'export GROQ_API_KEY="gsk_your_key_here"' >> ~/.zshrc
```

### use

Use `groq "query"` to chat with a model, or pipe queries into `groq` from other commands. See `groq --help` for optional arguments to further customize model outputs.
