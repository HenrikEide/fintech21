import requests
import json
import mysql.connector

if __name__=="__main__":
    test = "https://api.opensea.io/api/v1/assets?"
    testJson = requests.request("GET", test).text
    testData = json.loads(testJson)

    print(testData["assets"][0].keys())
    taskdb = mysql.connector.connect(host="localhost",user="root",database="fintechtask")
    db = taskdb.cursor()



