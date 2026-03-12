from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
from tools.plots import rc_bode_plot, first_order_step
from tools.circuits import voltage_divider, rc_cutoff
from tools.parser import parse_value
from agent.retriever import search

llm = ChatOllama(model="llama3.1")


class AgentState(TypedDict):
    question: str
    result: str

def rc_plot_node(state):

    text = state["question"]

    r = parse_value(text, "r")
    c = parse_value(text, "c")

    if None in (r, c):
        return {"result": "Provide R and C values."}

    img = rc_bode_plot(r, c)

    return {
    "result": {
        "text": "RC Bode plot generated.",
        "image": img_path
    }
}


def step_node(state):

    text = state["question"]

    K = parse_value(text, "k")
    tau = parse_value(text, "tau")

    if None in (K, tau):
        return {"result": "Provide K and tau."}

    img = first_order_step(K, tau)

    return {"result": f"Step response plot generated: {img}"}

def tutor_node(state: AgentState):

    response = llm.invoke(
        f"You are an electronics engineering tutor.\n\nQuestion: {state['question']}"
    )

    return {"result": response.content}

def knowledge_node(state):

    docs = search(state["question"])

    context = "\n".join(docs)

    response = llm.invoke(
        f"Use the following engineering knowledge to answer the question:\n\n{context}\n\nQuestion: {state['question']}"
    )

    return {"result": response.content}

def divider_node(state: AgentState):

    text = state["question"]

    vin = parse_value(text, "vin")
    r1 = parse_value(text, "r1")
    r2 = parse_value(text, "r2")

    if None in (vin, r1, r2):
        return {"result": "Please provide Vin, R1, and R2 values."}

    vout = voltage_divider(vin, r1, r2)

    return {
        "result": f"Voltage Divider Result\n\nVin={vin}\nR1={r1}\nR2={r2}\n\nVout={vout:.3f} V"
    }


def rc_node(state: AgentState):

    text = state["question"]

    r = parse_value(text, "r")
    c = parse_value(text, "c")

    if None in (r, c):
        return {"result": "Please provide R and C values."}

    fc = rc_cutoff(r, c)

    return {
        "result": f"RC Cutoff Frequency\n\nR={r}\nC={c}\n\nfc={fc:.2f} Hz"
    }


def router_node(state: AgentState):

    q = state["question"].lower()

    if "voltage divider" in q:
        return {"route": "divider"}

    if "rc" in q or "cutoff" in q:
        return {"route": "rc"}

    if "nyquist" in q or "alias" in q:
        return {"route": "dsp"}

    if "wavelength" in q or "antenna" in q:
        return {"route": "antenna"}

    if "explain" in q or "theorem" in q or "law" in q:
        return {"route": "knowledge"}
    
    if "plot rc" in q or "bode" in q:
        return {"route": "rcplot"}

    if "step response" in q:
        return {"route": "step"}

    return {"route": "tutor"}


builder = StateGraph(AgentState)

builder.add_node("router", router_node)
builder.add_node("tutor", tutor_node)
builder.add_node("divider", divider_node)
builder.add_node("rc", rc_node)
builder.add_node("knowledge", knowledge_node)
builder.add_edge("knowledge", END)
builder.add_node("rcplot", rc_plot_node)
builder.add_node("step", step_node)
builder.add_edge("rcplot", END)
builder.add_edge("step", END)

builder.set_entry_point("router")

builder.add_edge("router", "tutor")
builder.add_edge("divider", END)
builder.add_edge("rc", END)
builder.add_edge("tutor", END)

graph = builder.compile()