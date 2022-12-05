from random import choice

UserAgents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 "
    "Edg/106.0.1370.47 ",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 "
    "OPR/91.0.4516.20 "
]


def print_warning(text):
    print("\033[93m" + text + "\033[0m")


def print_error(text):
    print("\033[91m" + str(text) + "\033[0m ❌")


def print_green(text):
    print("\033[92m" + str(text) + "\033[0m ✅")


def user_agent() -> str:
    """
    :return: Random user-agent
    """
    return choice(UserAgents)