def function_work_with_stroke(list_of_words) -> list[str]:
    strings = []
    for str in list_of_words:
        if len(str) > 10:
            strings.append(str)
    print(strings)
    return strings

def is_сonsist(list_of_words) -> bool:
    is_сonsist = False
    for word in list_of_words:
        if word  == "hand":
            is_сonsist = True
            break
        else: is_сonsist=False
    print(is_сonsist)
    return is_сonsist

function_work_with_stroke([" short", "muchlongerstring", "hand", "adequate", "extremelylongstringexample"])
is_сonsist([" short", "muchlongerstring", "hand", "adequate", "extremelylongstringexample"])

