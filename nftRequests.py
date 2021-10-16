import requests

if __name__=="__main__":
    test = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20"
    print(requests.request("GET", test).text)