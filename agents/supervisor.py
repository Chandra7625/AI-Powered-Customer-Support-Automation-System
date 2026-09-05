from agents.llm import llm

def supervisor_agent(state):

    state["path"].append("Supervisor")

    prompt = f"""
Improve the response below.

Rules:
- Keep all technical details.
- Do not invent information.
- Make it professional.
- Keep it concise.

Response:
{state['response']}
"""

    result = llm.invoke(prompt)

    state["response"] = result.content

    return state