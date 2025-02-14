def stricha_for_ten_long(slownyk):
    strichkas = []
    for strichka in slownyk:
        if len(strichka) > 10:
            strichkas.append(strichka)
    print(strichkas)


stricha_for_ten_long(["short", "muchlongerstring", "raaa", "adequate", "extremelylongstringexample"])
