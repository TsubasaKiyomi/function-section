def chose_from_two(a, b, c):
    ans = a, b, c
    return ans


chose_from_two = ("リンゴ", "バナナ", "さくらんぼ")
lo = ("の中で赤いのは？",)
ar = chose_from_two + lo

answers = []
answers.append("リンゴ")
answers.append("さくらんぼ")

print(ar)
print(answers)
