from memory.memory import *

save_conversation(
    "David",
    "Billing issue",
    "Please contact billing support"
)

print(get_last_issue("David"))