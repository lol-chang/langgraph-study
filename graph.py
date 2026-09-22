from langgraph.graph import StateGraph, START, END

from nodes import trim_node, shorten, finalize, LIMIT
from state import State


def route_after_trim(state: State):
    if len(state["text"]) > LIMIT:
        return "shorten_node"
    return "finalize_node"


def build_graph():
    workflow = StateGraph(State)

    workflow.add_node("trim_node", trim_node)
    workflow.add_node("shorten_node", shorten)
    workflow.add_node("finalize_node", finalize)

    workflow.add_edge(START, "trim_node")
    workflow.add_conditional_edges("trim_node", route_after_trim)
    workflow.add_edge("shorten_node", "finalize_node")
    workflow.add_edge("finalize_node", END)
    return workflow.compile()
