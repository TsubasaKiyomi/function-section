#  集合型の使い所
def set_use(a):
    a


#  重複するgroup_colorをfor文でkyeとvalueにわけて出力。重複項目はset型なので統一される
group_color = {
    "あか": "red",
    "あお": "blue",
    "きいろ": "yellow",
    "きみどり": "greenish_yellow",
    "あお": "blue",
    "しろ": "white",
    "あか": "red",
    "しろ": "white",
    "きみどり": "greenish_yellow", }

for key in group_color.values():
    print(key)
for key in group_color.keys():
    print(key)
