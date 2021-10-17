import requests
import json
from nftmysql import setup_db

def get_assets(endpoint):
    testJson = requests.request("GET", endpoint).text
    return json.loads(testJson)

def nft_list(all_nfts : dict):
    nfts = []
    for nft in all_nfts["assets"]:
        print((nft["id"], nft["token_id"], nft["name"], nft["top_bid"], nft["permalink"]))
        nfts.append((nft["id"], nft["token_id"], nft["name"], nft["top_bid"], nft["permalink"]))
    return nfts

if __name__=="__main__":
    # test = "https://api.opensea.io/api/v1/assets?"
    # testJson = requests.request("GET", test).text
    # testData = json.loads(testJson)

    # print(testData["assets"][0].keys())

    # nfts = []
    # for nft in testData["assets"]:
    #     print((nft["id"], nft["token_id"], nft["name"], nft["top_bid"], nft["permalink"]))
    #     nfts.append((nft["id"], nft["token_id"], nft["name"], nft["top_bid"], nft["permalink"]))

    data = get_assets("https://api.opensea.io/api/v1/assets?")
    data_cleaned = nft_list(data)
    connection, cursor = setup_db("fintechtask", data_cleaned)
    



