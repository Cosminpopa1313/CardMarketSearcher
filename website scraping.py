from urllib.request import Request,urlopen
req = Request(
    url = "https://www.cardmarket.com/it/OnePiece/Products/Singles/Romance-Dawn/MonkeyDLuffy-OP01-024-V1",
    headers={'User-Agent': 'Mozilla/5.0'}
)
page = urlopen(req).read()
html = page.decode("utf-8")
print (html)
