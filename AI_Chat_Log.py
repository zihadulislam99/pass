def AI_Chat_Log():
    question = input("Question: ")
    answer = input(f"{question}\nAnswer")
    FileLog = open("AI_Chat_Log.txt", "r")
    chat_log_template = FileLog.read()
    chat_log_template_update = chat_log_template + f"\nYou : {question}\nAI  : {answer}"
    FileLog = open("AI_Chat_Log.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
while True:
    AI_Chat_Log()
