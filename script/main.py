import openai
from decouple import config
from colorama import init, Fore, Style

init()
API_KEY = config("API_KEY", cast=str)
model_engine = "text-davinci-003"


def operation(key: str = API_KEY, engine: str = model_engine) -> str:
    """
    Returns a bot response about a question you've asked for.
    """

    user_input = str()

    while user_input != "F":

        print("*" * 50 + "  New Quote - Insert F to Exit  " + "*" * 50)

        try:
            user_input = str(input())
        except:
            print("Houve um erro na entrada de dados do usuário.")

        openai.api_key = key

        if user_input != "F":
            function = openai.Completion.create(
                engine=engine,
                prompt=user_input,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
        else:
            return True

        response = function.choices[0].text

        print(Fore.YELLOW + response + Fore.RESET)

    return True


if __name__ == "__main__":

    operation()
    print("\n\nBye bye")
