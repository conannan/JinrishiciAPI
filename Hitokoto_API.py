import requests


def get_header(international_type=True):
    if international_type:
        return "https://international.v1.hitokoto.cn/"
    else:
        return "https://v1.hitokoto.cn/"


def get_sentence(international_type=True, category_type=None, encode_type=None, charset_type=None):
    api_address = get_header(international_type) + "?"
    if category_type in ["a", "b", "c", "d", "e", "f", "g"]:
        api_address = api_address + "c=" + category_type + "&"
    if encode_type in ["text", "json"]:
        api_address = api_address + "encode=" + encode_type + "&"
    if charset_type in ["utf-8", "gbk"]:
        api_address = api_address + "charset=" + charset_type
    if api_address.endswith("?") or api_address.endswith("&"):
        api_address = api_address[:-1]
    result = requests.get(api_address)
    if result.status_code == 200:
        if encode_type not in ["text", "js"]:
            return result.json()
        else:
            return result
    else:
        return "Error."


def get_type(s):
    return {"a": "Anime",
            "b": "Comic",
            "c": "Game",
            "d": "Novel",
            "e": "Original",
            "f": "Internet",
            "g": "Others"}.get(s)


def output(result, encode_type=None, charset_type=None):
    if encode_type != "text":
        print(result["hitokoto"], "\n", get_type(result["type"]).rjust(50), result["from"])
    else:
        if charset_type == "gbk":
            print(result.content.decode('utf-8', 'ignore'))
        else:
            print(result.text)


if __name__ == "__main__":
    international = True  # True/False
    category = None
    """
    a	Anime - 动画
    b	Comic – 漫画
    c	Game – 游戏
    d	Novel – 小说
    e	Myself – 原创
    f	Internet – 来自网络
    g	Other – 其他
    """
    encode = None  # text/json
    charset = None  # utf-8/gbk
    sentence = get_sentence(international, category, encode, charset)
    output(sentence, encode, charset)
