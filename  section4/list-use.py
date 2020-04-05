# 相乗りタクシーwhileループで作成
count = 0
while True:
    if count >= 5:
        break

    if count == 0:
        count += 1
        print(count)
        print("乗車1人目")

    if count == 1:
        count += 1
        print(count)
        print("相乗り乗車２人目")

    if count == 2:
        count += 1
        print(count)
        print("更に１人増える・３人目")
        continue

    if count == 3:
        count -= 2
        print(count)
        print("２人降りる１人乗車中")

    count += 1
    print("更に１人増える２人目")
    print(count)
