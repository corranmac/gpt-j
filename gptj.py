import requests


class GPTJ:

    def __init__(self):
        pass

    def generate(self, context, token_max_length, temperature, top_p):
        assert isinstance(token_max_length, int), "Max token most be integer value"
        assert isinstance(temperature, float), "Max token most be float value"
        assert isinstance(top_p, float), "Max token most be float value"
        payload = {"context": str(context), "token_max_length": token_max_length, "temperature": temperature,"top_p": top_p}
        URL = requests.post("http://34.90.255.118:5000/generate", params=payload)
        text = URL.json()
        print(text["text"])