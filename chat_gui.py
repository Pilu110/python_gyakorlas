def main():
    print("Elindult a chat kliens")
    messages = []
    while True:
        message = input("Üzenet: ").strip()
        if not message:
            continue
        if message in ["quit", "exit"]:
            print("Kilépés...")
            break
        elif message == "history":
            print("Üzenet előzmények:")
            for msg in messages:
                print("- " + msg)
            continue
        elif message == "fordit":
            if messages:
                reversed_msg = messages[-1][::-1]
                print("Fordított üzenet: " + reversed_msg)
            else:
                print("Nincs még üzenet a fordításhoz!")
            continue
        print("Üzenet: " + message)
        messages.append(message)

if __name__ == "__main__":
    main()
