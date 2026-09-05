from langgraph.graph import StateGraph, END

from state import SupportState

from agents.classifier import classify_intent

from agents.sales_agent import sales_agent
from agents.technical_agent import technical_agent
from agents.billing_agent import billing_agent
from agents.account_agent import account_agent

from agents.memory_agent import memory_agent

from agents.approval import approval_node
from agents.supervisor import supervisor_agent
# def router(state):

#     return state["intent"]
def router(state):

    intent = state["intent"]

    print("Routing to:", intent)

    return intent
def approval_router(state):

    if state.get("approval_required", False):

        state["response"] = (
            "This request requires human supervisor approval."
        )

        return "supervisor"

    return "supervisor"
builder = StateGraph(SupportState)
builder.add_node(
    "classifier",
    classify_intent
)

builder.add_node(
    "sales",
    sales_agent
)

builder.add_node(
    "technical",
    technical_agent
)

builder.add_node(
    "billing",
    billing_agent
)

builder.add_node(
    "account",
    account_agent
)

builder.add_node(
    "memory",
    memory_agent
)

builder.add_node(
    "approval",
    approval_node
)

builder.add_node(
    "supervisor",
    supervisor_agent
)
builder.set_entry_point(
    "classifier"
)
builder.add_conditional_edges(
    "classifier",
    router,
    {
        "Sales":"sales",
        "Technical":"technical",
        "Billing":"billing",
        "Account":"account",
        "Memory":"memory"
    }
)
builder.add_edge(
    "sales",
    "approval"
)

builder.add_edge(
    "technical",
    "approval"
)

builder.add_edge(
    "billing",
    "approval"
)

builder.add_edge(
    "account",
    "approval"
)
builder.add_edge(
    "memory",
    "supervisor"
)
builder.add_edge(
    "approval",
    "supervisor"
)
builder.add_edge(
    "supervisor",
    END
)
graph = builder.compile()