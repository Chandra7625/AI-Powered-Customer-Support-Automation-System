def approval_node(state):

    query = state["query"].lower()

    keywords = [
        "refund",
        "cancel subscription",
        "account closure",
        "close account",
        "compensation",
        "management"
    ]

    state["approval_required"] = False

    for word in keywords:

        if word in query:

            state["approval_required"] = True
            break
    state["path"].append("Approval Check")
    return state