import requests
from bs4 import BeautifulSoup


def get_english_word():
    url = "http://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Поднимает HTTPError для кода состояния HTTP 4xx/5xx

        soup = BeautifulSoup(response.text, 'html.parser')
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }

    except requests.RequestException as e:
        print(f"Произошла ошибка при запросе: {e}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def word_game():
    print("Добро пожаловать в игру 'Слово'")
    while True:
        word_dict = get_english_word()
        if word_dict is None:
            print("Не удалось получить слово. Попробуйте позже.")
            break

        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Ваш ответ: ")
        if user == word:
            print("Поздравляю, вы выиграли")
            break
        else:
            print(f"ответ неправильный. Правильным было {word}")

        play_again = input("Хотите сыграть ещё раз? y/n ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


if __name__ == '__main__':
    word_game()
