from agents.approval import approval_node

state = {
    "query": "What pricing plans are available?"
}

result = approval_node(state)

print(result)