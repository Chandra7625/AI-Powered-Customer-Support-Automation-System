def classify_intent(state):

    query = state["query"].lower()

    if "previous issue" in query:
        state["intent"] = "Memory"

    elif any(word in query for word in [
        "password",
        "login",
        "account",
        "profile",
        "activate",
        "deactivate"
    ]):
        state["intent"] = "Account"

    elif any(word in query for word in [
        "refund",
        "invoice",
        "payment",
        "billing",
        "subscription"
    ]):
        state["intent"] = "Billing"

    elif any(word in query for word in [
        "crash",
        "error",
        "bug",
        "upload",
        "installation",
        "configuration",
        "technical"
    ]):
        state["intent"] = "Technical"

    elif any(word in query for word in [
        "pricing",
        "price",
        "plan",
        "product"
    ]):
        state["intent"] = "Sales"

    else:
        state["intent"] = "Memory"

    state["path"].append("Classifier")

    print("Detected Intent:", state["intent"])

    return state