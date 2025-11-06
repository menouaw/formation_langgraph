import random
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# état
class State(TypedDict, total=False):
    graph_state: str

# noeud conditionnel
def roll_dice(state=None) -> Literal["node_2", "node_3"]:
    if random.random() < 0.5:
        return "node_2"
    return "node_3"

# noeuds
def node_1(state=None):
    current = state.get('graph_state', '') if state else ''
    print("---Node 1---")
    return {"graph_state": current}

def node_2(state=None):
    current = state.get('graph_state', '') if state else ''
    print("---Node 2---")
    return {"graph_state": current + "Pile!\n"}

def node_3(state=None):
    current = state.get('graph_state', '') if state else ''
    print("---Node 3---")
    return {"graph_state": current + "Face!\n"}

# construction
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", roll_dice)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# compilation
graph = builder.compile()