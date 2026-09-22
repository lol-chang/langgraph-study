from typing import TypedDict
from typing import Annotated
from operator import add


class State(TypedDict):
    text: str
    history: Annotated[list[str], add]
    steps: int
