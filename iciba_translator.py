from wox import Wox
import requests
import json
import webbrowser


class IcibaTranslator(Wox):
    def query(self, query):
        if query == "":
            return [{
                "Title": "iCIBA 翻译",
                "IcoPath": "Image\\icon.png"
            }]

        url = f"http://fy.iciba.com/ajax.php?a=fy&f=auto&t=auto&w={query}"
        ret = []
        resp = json.loads(requests.get(url).text)
        if resp['status'] == 1:
            ret.append({
                "Title": resp['content']['out'],
                "IcoPath": "Image\\icon.png",
                "JsonRPCAction": {
                    "method": "detail",
                    "parameters": [f"http://www.iciba.com/{query}"],
                    "dontHideAfterAction": False
                }
            })
        elif resp['status'] == 0:
            for mean in resp['content']['word_mean']:
                ret.append({
                    "Title": mean,
                    "IcoPath": "Image\\icon.png",
                    "JsonRPCAction": {
                        "method": "detail",
                        "parameters": [f"http://www.iciba.com/{query}"],
                        "dontHideAfterAction": False
                    }
                })
        return ret

    def detail(self, url):
        webbrowser.open(url)


if __name__ == '__main__':
    IcibaTranslator()
