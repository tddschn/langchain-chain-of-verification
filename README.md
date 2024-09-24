# langchain-chain-of-verification 

Based off CoVe CLI at https://github.com/ritun16/chain-of-verification , packaged (with `uv`) and updated for newer langchain versions for easier consumption.

`langchain-chain-of-verification` Can be used as CLI or library.

CoVe: https://arxiv.org/pdf/2309.11495

Enhanced by DuckDuckGo search (by ritun16)

- [langchain-chain-of-verification](#langchain-chain-of-verification)
  - [Usage](#usage)
    - [CLI](#cli)
    - [Library](#library)
  - [Examples](#examples)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)

## Usage


### CLI

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

### Library

```python
from langchain_chain_of_verification import create_cove_chain

def create_cove_chain(
    original_query: str,
    llm_name="gpt-4o",
    temperature=0.1,
    router_max_tokens=500,
    show_intermediate_steps=True,
) -> str:
    """
    Creates a Chain of Verification (CoVE) using specified language models.

    Args:
        original_query (str): The original question to be processed.
        llm_name (str, optional): The name of the language model to use. Defaults to "gpt-4o".
        temperature (float, optional): The temperature setting for the language model. Defaults to 0.1.
        router_max_tokens (int, optional): The maximum number of tokens for the language model. Defaults to 500.
        show_intermediate_steps (bool, optional): Whether to show intermediate steps. Defaults to True.

    Returns:
        str: The result (final answer) of the CoVE chain processing.

    Example:
        >>> result = create_cove_chain("What is the capital of France?")
        >>> print(result)
    """
    ...
```

## Examples

```plain
cove --question 'name athletes born in raleigh'
Chain selected: WIKI_CHAIN

################################################################################

{'baseline_response': '1. Chasity Melvin\n'
                      '2. Ryan Jeffers\n'
                      "3. Devonte' Graham\n"
                      '4. Trea Turner',
 'final_answer': 'Based on the verification questions and answers, the refined '
                 'answer should only include athletes who were confirmed to be '
                 'born in Raleigh. Therefore, the final refined answer is:\n'
                 '\n'
                 '1. Ryan Jeffers\n'
                 "2. Devonte' Graham",
 'original_question': 'name athletes born in raleigh',
 'verification_answers': 'Question: 1. Was Chasity Melvin born in Raleigh? '
                         'Answer: No, Chasity Melvin was not born in Raleigh. '
                         'She was born in Roseboro, North Carolina.\n'
                         'Question: 2. Was Ryan Jeffers born in Raleigh? '
                         'Answer: Yes, Ryan Jeffers was born in Raleigh, North '
                         'Carolina.\n'
                         "Question: 3. Was Devonte' Graham born in Raleigh? "
                         "Answer: Yes, Devonte' Graham was born in Raleigh, "
                         'North Carolina.\n'
                         'Question: 4. Was Trea Turner born in Raleigh? '
                         'Answer: No, Trea Turner was not born in Raleigh. '
                         'According to the provided context, Trea Turner was '
                         'born on June 30, 1993, in Boynton Beach, Florida.\n',
 'verification_question_template': 'Was [athlete] born in [Raleigh]?',
 'verification_questions': '1. Was Chasity Melvin born in Raleigh?\n'
                           '2. Was Ryan Jeffers born in Raleigh?\n'
                           "3. Was Devonte' Graham born in Raleigh?\n"
                           '4. Was Trea Turner born in Raleigh?'}

################################################################################

Final Answer: Based on the verification questions and answers, the refined answer should only include athletes who were confirmed to be born in Raleigh. Therefore, the final refined answer is:

1. Ryan Jeffers
2. Devonte' Graham
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
