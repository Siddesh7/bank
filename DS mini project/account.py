accounts = {
    "12": {"name": "Sankhya", "pass": "apple", "Balance": 4000, "Type": "Savings"},
    "13": {"name": "Mike", "pass": "bat", "Balance": 400, "Type": "Savings"},
    "14": {"name": "Siva", "pass": "cat", "Balance": 40, "Type": "Savings"},
    "15": {"name": "Senthil", "pass": "dog", "Balance": 8000, "Type": "Savings"},
    "16": {"name": "Surya", "pass": "elephant", "Balance": 4000, "Type": "Savings"},
    "17": {"name": "Elon Musk", "pass": "nap", "Balance": 3000000000, "Type": "Savings"},
    "18": {"name": "Jeff", "pass": "cap", "Balance": 2000000000, "Type": "Savings"},
    "19": {"name": "Bezos", "pass": "akon", "Balance": 4000, "Type": "Savings"},
    "20": {"name": "Ark", "pass": "eminem", "Balance": 400, "Type": "Savings"},
    "21": {"name": "Jack", "pass": "datastructure", "Balance": 90000, "Type": "Savings"}
}


def checkAcc(id, password):
    if id in accounts.keys() and accounts[id]["pass"] == password:
        return accounts[id]["name"]
    else:
        return "Hey Stranger, looks like you don't have an account in LaLaLand"


def balance(id, password):
    if id in accounts.keys() and accounts[id]["pass"] == password:
        return accounts[id]["Balance"]


def writeAcc(id):
    f = open("notes.txt", "w")
    f.write(id)
    f.close


def readAcc():
    f = open("notes.txt", "r")
    k = f.read()
    return k
