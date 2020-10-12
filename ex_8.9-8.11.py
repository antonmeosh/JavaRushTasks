def show_messages(messages, send_message):
    print("\nList of messages: ")
    while messages:
        current_message = messages.pop()
        print(f"{current_message}")
        send_message.append(current_message)


def show_send_messages(send_message):
    print("\nThis message will be send: ")
    for message in send_message:
        print(message)


messages = ['hello', 'hi', 'privet', 'salute']
send_message = []
show_messages(messages[:], send_message)
show_send_messages(send_message)
print(messages)
