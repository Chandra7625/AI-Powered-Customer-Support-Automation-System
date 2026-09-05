# AI-Powered Customer Support Automation System

## Project Overview

The **AI-Powered Customer Support Automation System** is a multi-agent customer support application built using **LangGraph, LangChain, Ollama, ChromaDB, and SQLite**.

The system automates customer support queries by identifying the customer's issue, routing it to the appropriate support department, retrieving relevant information from company documents, maintaining conversation history, and escalating sensitive requests to a human supervisor.

---

## Objectives

The main objectives of the system are:

- Accept customer support queries.
- Automatically classify customer intent.
- Route queries to the appropriate support department.
- Retrieve relevant information from company documents using RAG.
- Maintain customer conversation history.
- Support memory-based queries.
- Identify high-risk requests.
- Require human approval for sensitive operations.
- Generate accurate and context-aware final responses.
- Provide a structured and traceable LangGraph workflow.

---

# System Architecture

```text
                         Customer Query
                               |
                               v
                       +----------------+
                       |  Input / State |
                       +-------+--------+
                               |
                               v
                       +----------------+
                       |    Classifier  |
                       +-------+--------+
                               |
                +--------------+--------------+
                |              |              |
                v              v              v
             Sales         Technical       Billing
             Agent           Agent          Agent
                |              |              |
                |              |              |
                +--------------+--------------+
                               |
                               v
                         RAG Retrieval
                               |
                               v
                       +----------------+
                       | Approval Check |
                       +-------+--------+
                               |
                    +----------+----------+
                    |                     |
                    v                     v
              Human Approval          No Approval
                    |                     |
                    +----------+----------+
                               |
                               v
                       +----------------+
                       |   Supervisor   |
                       +-------+--------+
                               |
                               v
                       Final Response
                               |
                               v
                           Customer

                 +--------------------------+
                 |      SQLite Memory       |
                 | Conversation History     |
                 +--------------------------+
