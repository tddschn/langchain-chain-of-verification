import json

from langchain.chains import ConversationChain
from langchain.schema import HumanMessage

from langchain_chain_of_verification.cove_chains import (
    WikiDataCategoryListCOVEChain,
    MultiSpanCOVEChain,
    LongFormCOVEChain,
)
import langchain_chain_of_verification.prompts as prompts


class RouteCOVEChain(object):
    def __init__(self, question, llm, chain_llm, show_intermediate_steps):
        self.llm = llm
        self.question = question
        self.show_intermediate_steps = show_intermediate_steps

        wiki_data_category_list_cove_chain_instance = WikiDataCategoryListCOVEChain(
            chain_llm
        )
        wiki_data_category_list_cove_chain = (
            wiki_data_category_list_cove_chain_instance()
        )

        multi_span_cove_chain_instance = MultiSpanCOVEChain(chain_llm)
        multi_span_cove_chain = multi_span_cove_chain_instance()

        long_form_cove_chain_instance = LongFormCOVEChain(chain_llm)
        long_form_cove_chain = long_form_cove_chain_instance()

        self.destination_chains = {
            "WIKI_CHAIN": wiki_data_category_list_cove_chain,
            "MULTI_CHAIN": multi_span_cove_chain,
            "LONG_CHAIN": long_form_cove_chain,
        }
        self.default_chain = ConversationChain(llm=chain_llm, output_key="final_answer")

    def __call__(self):
        route_message = [
            HumanMessage(content=prompts.ROUTER_CHAIN_PROMPT.format(self.question))
        ]
        response = self.llm(route_message)
        response_str = response.content
        try:
            chain_dict = json.loads(response_str)
            try:
                if self.show_intermediate_steps:
                    print("Chain selected: {}".format(chain_dict["category"]))
                return self.destination_chains[chain_dict["category"]]
            except KeyError:
                if self.show_intermediate_steps:
                    print(
                        "KeyError! Switching back to default chain. `ConversationChain`!"
                    )
                return self.default_chain
        except json.JSONDecodeError:
            if self.show_intermediate_steps:
                print(
                    "JSONDecodeError! Switching back to default chain. `ConversationChain`!"
                )
            return self.default_chain
