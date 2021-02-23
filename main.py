import time

from aibot import BOT


def main():
    start = time.time()

    my_bot = BOT()

    sentence = "دمای هوای  در ساعت ۱۲:۰۱ در تاریخ ۱۲ بهمن سال ۹۸ نیمه شب شرعی مشهد فردا چقدر است؟"
    answer, answer_sen = my_bot.AIBOT(sentence)
    # print(answer)
    # answer = my_bot.aibot('input.wav')

    print(answer)
    # print("final answer : " + answer_sen)

    end = time.time()
    print(f"Runtime of the program is {end - start}")


if __name__ == "__main__":
    main()
