def show_messages(text_list):
    for text in text_list:
        print(text)

def send_messages(text_list, sent_list):
    while text_list:
        current_text = text_list.pop(0)
        print(f"sending {current_text}")
        sent_list.append(current_text)


texts = ['hello', 'hi', 'ily', 'Im pregnant']
sent_texts = []

#show_messages(texts)
send_messages(texts[:], sent_texts)
print(f"text list: {texts}")
print(f"sent texts: {sent_texts}")