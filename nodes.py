from state import State


# 노드	하는 일
# trim	앞뒤 공백 제거, 연속 공백 1칸으로
def trim_node(state: State):
    step = state["steps"] + 1

    txt = " ".join(state["text"].split())
    return {"text": txt, "history": [f"trim: {txt}"], "steps": step}


LIMIT = 8
MARK = "..."


def shorten(state: State):
    step = state["steps"] + 1
    txt = state["text"]
    if len(txt) > LIMIT:
        txt = txt[: LIMIT - len(MARK)] + MARK

    return {"text": txt, "history": [f"shorten: {txt}"], "steps": step}


def finalize(state: State):
    step = state["steps"] + 1
    txt = state["text"].capitalize() + "!"
    return {"text": txt, "history": [f"finalize: {txt}"], "steps": step}
