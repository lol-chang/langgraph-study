from graph import build_graph


def main():
    app = build_graph()

    user_input_text = input("입력해주세요: ")

    initial_state = {"text": user_input_text, "steps": 0}
    result = app.invoke(initial_state)

    print("\n✨ 최종 결과:")
    print(result)


if __name__ == "__main__":
    main()
