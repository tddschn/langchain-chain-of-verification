import argparse
from dotenv import load_dotenv
from pprint import pprint

from langchain_community.chat_models import ChatOpenAI
from langchain_chain_of_verification.route_chain import RouteCOVEChain

load_dotenv()


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
