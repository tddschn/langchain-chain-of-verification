import argparse
from trace import CoverageResults
from dotenv import load_dotenv
from pprint import pprint

from langchain_community.chat_models import ChatOpenAI
from langchain_chain_of_verification.route_chain import RouteCOVEChain
from langchain_chain_of_verification.types import CoVeChainResult

load_dotenv()


def create_cove_chain(
    original_query: str,
    llm_name="gpt-4o",
    temperature=0.1,
    router_max_tokens=500,
    show_intermediate_steps=True,
) -> CoverageResults:
    """
       Creates a Chain of Verification (CoVE) using specified language models.

       Args:
           original_query (str): The original question to be processed.
           llm_name (str, optional): The name of the language model to use. Defaults to "gpt-4o".
           temperature (float, optional): The temperature setting for the language model. Defaults to 0.1.
           router_max_tokens (int, optional): The maximum number of tokens for the language model. Defaults to 500.
           show_intermediate_steps (bool, optional): Whether to show intermediate steps. Defaults to True.

       Returns:
           dict: The result (final answer) of the CoVE chain processing.
           Something like this:
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

       Example:
           >>> result = create_cove_chain("What is the capital of France?")
           >>> print(result)
    """
    chain_llm = ChatOpenAI(
        model_name=llm_name,
        temperature=temperature,
        max_tokens=router_max_tokens,
    )

    route_llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.1, max_tokens=500)

    router_cove_chain_instance = RouteCOVEChain(
        original_query, route_llm, chain_llm, show_intermediate_steps
    )
    router_cove_chain = router_cove_chain_instance()
    router_cove_chain_result = router_cove_chain({"original_question": original_query})

    return router_cove_chain_result


def cli_main():
    parser = argparse.ArgumentParser(description="Chain of Verification (CoVE) parser.")
    parser.add_argument(
        "--question",
        type=str,
        required=True,
        help="The original question user wants to ask",
    )
    parser.add_argument(
        "--llm-name",
        type=str,
        required=False,
        default="gpt-4o",
        help="The openai llm name",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        required=False,
        default=0.1,
        help="The temperature of the llm",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        required=False,
        default=500,
        help="The max_tokens of the llm",
    )
    parser.add_argument(
        "--show-intermediate-steps",
        type=bool,
        required=False,
        default=True,
        help="The max_tokens of the llm",
    )
    args = parser.parse_args()

    router_cove_chain_result = create_cove_chain(
        original_query=args.question,
        llm_name=args.llm_name,
        temperature=args.temperature,
        router_max_tokens=args.max_tokens,
        show_intermediate_steps=args.show_intermediate_steps,
    )

    if args.show_intermediate_steps:
        print("\n" + 80 * "#" + "\n")
        pprint(router_cove_chain_result)
        print("\n" + 80 * "#" + "\n")
    print("Final Answer: {}".format(router_cove_chain_result["final_answer"]))


if __name__ == "__main__":
    cli_main()
