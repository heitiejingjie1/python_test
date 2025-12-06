from survey import AnonymousSurvey

"""定义问题"""
question = "你最喜欢的编程语言是？"
language_survey = AnonymousSurvey(question)

"""显示问题并存储答案"""
language_survey.show_question()

print("输入'q'退出.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

print("谢谢你的参与!")
language_survey.show_results()
