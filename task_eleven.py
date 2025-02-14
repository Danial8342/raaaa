def send_bad_marks_to_parents(slownyk):
    strichkas = []
    for strichka in slownyk:
        if len(strichka) > 10:
            strichkas.append(strichka)
    print(strichkas)


send_bad_marks_to_parents(["short", "muchlongerstring", "raaa", "adequate", "extremelylongstringexample"])
