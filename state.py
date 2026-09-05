from typing import TypedDict

class SupportState(TypedDict):

    customer_name: str
    query: str
    intent: str
    retrieved_context: str
    response: str
    approval_required: bool
    approved: bool

    path: list