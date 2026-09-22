from state import State


def upper_case_node(state: State):
    print("🤖 [일꾼] 변환 작업을 시작합니다.")
    original_text = state["user_input"]

    return {"bot_response": original_text.upper()}
