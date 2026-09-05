from agents.llm import llm
from rag.retriever import retrieve
from memory.memory import save_conversation

def account_agent(state):

    query = state["query"]

    context = retrieve(query)

    prompt = f"""
You are an Account Support Agent.

Context:
{context}

Customer Query:
{query}

Answer professionally.
"""

    response = llm.invoke(
    f"""
Answer ONLY using the provided context.

If the answer is not in the context, say:
'I could not find that information.'

Context:
{context}

Question:
{query}

Keep the answer under 5 lines.
"""
)

    # state["retrieved_context"] = context
    # state["response"] = response.content
    state["response"] = context
    state["path"].append("Account Agent")
    print("Account Agent Selected")
    save_conversation(
    state["customer_name"],
    state["query"],
    state["response"]
    )
    return state