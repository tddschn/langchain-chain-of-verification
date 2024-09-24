# langchain-chain-of-verification 

Based off https://github.com/ritun16/chain-of-verification , packaged and updated for newer langchain versions for easier consumption.

Can be used as CLI or library.

- [langchain-chain-of-verification](#langchain-chain-of-verification)
  - [Usage](#usage)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)

## Usage

```plain
# uvx --from langchain-chain-of-verification cove --help
$ cove --help

usage: cove [-h] --question QUESTION [--llm-name LLM_NAME] [--temperature TEMPERATURE] [--max-tokens MAX_TOKENS] [--show-intermediate-steps SHOW_INTERMEDIATE_STEPS]

Chain of Verification (CoVE) parser.

options:
  -h, --help            show this help message and exit
  --question QUESTION   The original question user wants to ask
  --llm-name LLM_NAME   The openai llm name
  --temperature TEMPERATURE
                        The temperature of the llm
  --max-tokens MAX_TOKENS
                        The max_tokens of the llm
  --show-intermediate-steps SHOW_INTERMEDIATE_STEPS
                        The max_tokens of the llm
```


## Installation

To run without installing with `uv`, try `uvx --from langchain-chain-of-verification cove --help`.

### pipx

This is the recommended installation method.

```
$ pipx install langchain-chain-of-verification
```

### [pip](https://pypi.org/project/langchain-chain-of-verification/)

```
$ pip install langchain-chain-of-verification
```
