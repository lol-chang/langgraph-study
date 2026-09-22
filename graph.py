from langgraph.graph import StateGraph, START, END

from nodes import upper_case_node
from state import State


def build_graph():
    workflow = StateGraph(State)

    # 노드 등록 ("이름", 함수)
    workflow.add_node("transformer", upper_case_node)

    # 엣지 연결 (시작점 -> 변환기 -> 종료점)
    workflow.add_edge(START, "transformer")
    workflow.add_edge("transformer", END)

    return workflow.compile()
