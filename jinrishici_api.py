import requests
import json


def get_token():
    api_address = "https://v2.jinrishici.com/token"
    result = requests.get(api_address)
    if result.status_code == 200:
        return result.json()
    else:
        return "Error."


def get_info():
    headers = {'X-User-Token': '0gTUtDWNU9Fg9qubXDn4mGq2CrWEZ6wQ'}
    api_address = "https://v2.jinrishici.com/info"
    result = requests.get(api_address, headers=headers)
    if result.status_code == 200:
        return result.json()
    else:
        return "Error."


def get_sentence():
    headers = {'X-User-Token': '0gTUtDWNU9Fg9qubXDn4mGq2CrWEZ6wQ'}
    api_address = "https://v2.jinrishici.com/sentence"
    result = requests.get(api_address, headers=headers)
    if result.status_code == 200:
        return result.json()
    else:
        return "Error."


def output(origin, all=False, ex=False):
    if all:
        print("\t\t", origin["origin"]["title"], "\n\t\t\t\t", origin["origin"]["dynasty"], origin["origin"]["author"])
        for x in origin["origin"]["content"]:
            print(x)
        if ex:
            if origin["origin"]["translate"] is not None:
                for x in origin["origin"]["translate"]:
                    print(x)
            else:
                print("No translations.")
    else:
        print(origin["content"], "\n\t\t\t", origin["origin"]["title"], "-",  origin["origin"]["dynasty"],
              origin["origin"]["author"])
        if ex:
            if origin["origin"]["translate"] is not None:
                i = 0
                flag = False
                for x in origin["origin"]["content"]:
                    if origin["content"] in x:
                        flag = True
                        print("\n", origin["origin"]["translate"][i])
                    i += 1
                if flag is False:
                    print("\n", origin["origin"]["translate"])
            else:
                print("No translations.")


if __name__ == "__main__":
    source = get_sentence()["data"]
    all_sentence = False
    Explanation = True
    output(source, all_sentence, Explanation)
