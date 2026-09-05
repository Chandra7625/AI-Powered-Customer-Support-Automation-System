from memory.memory import get_last_issue

def memory_agent(state):

    customer = state["customer_name"]

    last_issue = get_last_issue(customer)
    state["path"].append("Memory Agent")
    state["response"] = (
        f"Your previous support issue was: {last_issue}"
    )

    return state