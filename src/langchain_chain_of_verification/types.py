from typing import TypedDict


class CoVeChainResult(TypedDict):
    baseline_response: str
    final_answer: str
    original_question: str
    verification_answers: str
    verification_question_template: str
    verification_questions: str
