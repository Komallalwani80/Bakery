
def getMinPacks(availPacks, qty):
    container = {}

    for i in range(len(availPacks)):
        if (int(qty) % int(availPacks[i]) == 0):
            x = (int(qty) // int(availPacks[i]))
            y = int(availPacks[i])
            container.__setitem__(str(x), str(y))
            break

        elif (int(qty) > int(availPacks[i])):
            if int(qty) % int(availPacks[i]) not in availPacks:
                continue
            else:
                x = int(qty) // int(availPacks[i])
                y = int(availPacks[i])
                container.__setitem__(str(x), str(y))
                qty = int(qty) - (int(availPacks[i]) * x)
                getMinPacks(availPacks, qty)

        else:
            return "Packs Unavailable."

    return container


def getBill(packs, price, x, pCode, totalQuant):
    getPrice = 0
    bill = " "
    for key in x:
        temp = x[str(key)]
        pack_price = price[pCode]
        k = pack_price[temp]

        getPrice = getPrice + int(key) * float(k)
        bill = bill + "\t" + str(key) + " " + "X" + " " + str(temp) + " " + "$" + str(k) + "\n"

    print(str(totalQuant) + " " + pCode + " " + "$" + str(getPrice))
    print(bill)


if __name__ == '__main__':

    packs = {"VS5": [5, 3], "MB11": [8, 5, 2], "CF": [9, 5, 3]}
    price = {"VS5": {'5': '8.99', '3': '6.99'}, "MB11": {'8': '24.95', '5': '16.95', '2': '9.95'},
             "CF": {'9': '16.99', '5': '9.95', '3': '5.95'}}

    print("""Input number of items followed by product code,
    eg. 10 VS5
        14 MB11
        13 CF""")

    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    order = '\n'.join(lines)

    placedOrder = order.splitlines()
    print("placedOrder: ", placedOrder)

    # for each order, get Minimum number of packs
    for ord in placedOrder:
        quantity = ord.split()

        x = getMinPacks(packs[quantity[1]], quantity[0])
        # print("Final Min Packs and it's quantity :",x)

        y = getBill(packs, price, x, quantity[1], quantity[0])

