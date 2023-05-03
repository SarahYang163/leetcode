import json

if __name__ == '__main__':
    json1 = json.loads(
        '{"code":200,"info":[{"goods_id":1300393,"price":10.99},{"goods_id":1300394,"price":21.99},{"goods_id":1300395,"price":1.99}]}')
    print(len(json1["info"]))
    res = [[], [], []]

    for p in json1["info"]:
        if p["price"] <= 10:
            res[0].append(p["goods_id"])
        elif p["price"] <= 20:
            res[1].append(p["goods_id"])
        else:
            res[2].append(p["goods_id"])

    print(res)

