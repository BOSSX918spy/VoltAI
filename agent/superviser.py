from langchain_ollama import ChatOllama

from agent.circuit_agent import circuit_agent
from agent.dsp_agent import dsp_agent
from agent.control_agent import control_agent
from agent.antenna_agent import antenna_agent

llm = ChatOllama(model="llama3.1")

def supervisor(question):

    prompt = f"""
Classify this engineering question into one category:

circuits
dsp
control
antenna

Question: {question}
"""

    category = llm.invoke(prompt).content.lower()

    if "circuit" in category:
        return circuit_agent(question)

    if "dsp" in category:
        return dsp_agent(question)

    if "control" in category:
        return control_agent(question)

    if "antenna" in category:
        return antenna_agent(question)

    return "VoltAI could not classify the question."