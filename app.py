from graph import graph

customer = input(
    "Customer Name: "
)

query = input(
    "Customer Query: "
)

initial_state = {

    "customer_name": customer,

    "query": query,

    "intent": "",

    "retrieved_context": "",

    "response": "",

    "approval_required": False,

    "approved": False,

    "path": []
}

result = graph.invoke(
    initial_state
)
print("\nWORKFLOW PATH\n")

print(
    " -> ".join(result["path"])
)

print("\nFINAL RESPONSE\n")

print(
    result["response"]
)