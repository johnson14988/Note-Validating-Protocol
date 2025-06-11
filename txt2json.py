import json

def init():
    return {
        "definedIn": "",
        "signature": {
            "funcName": "",
            "argList": [],
            "returnWithCode": []
        },
        "explanation": ""
    }


def parse(txt_input):
    data = init()
    with open(txt_input, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines() if l]
        for l in lines:
            if l.startswith("$funcName"):
                data["signature"]["funcName"] = l.split("=")[1].strip()
            elif l.startswith("$"):
                data[l.split("=")[0][1:].strip()] = l.split("=")[1].strip()
            elif "|" in l:
                items = l.split("|")
                data["signature"]["argList"].append({
                    "argName": items[0].strip(),
                    "argType": items[1].strip(),
                    "argDesc": items[2].strip()
                })
            elif "->" in l:
                items = l.split("->")
                data["signature"]["returnWithCode"].append({
                    "returnValue": items[0].strip(),
                    "meaning": items[1].strip()
                })
    return data

data = parse("function_demo.txt")
with open(f"{data[funcName]}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)