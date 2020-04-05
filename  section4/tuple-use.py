def chose_from_two(a, b, c):
    ans = a, b, c
    return ans


chose_from_two = ("リンゴ", "バナナ", "さくらんぼ")
set_add = ("の中で赤いのは？",)
get_fruits = chose_from_two + set_add

answers = []
answers.append("リンゴ")
answers.append("さくらんぼ")

print(get_fruits)
print(answers)
