from graph import build_graph


def main():
    app = build_graph()

    user_input_text = input("입력해주세요~")

    initial_state = {"user_input": user_input_text}
    result = app.invoke(initial_state)

    print("\n✨ 최종 결과:")
    print(result["bot_response"])


if __name__ == "__main__":
    main()
