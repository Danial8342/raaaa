def stricha_for_ten_long(slownyk):
    strichkas = []
    for strichka in slownyk:
        if len(strichka) > 10:
            strichkas.append(strichka)
    print(strichkas)

def is_konsisd(slownyk):
    is_konsisd_hand = False
    for word in slownyk:
        if word  == "hand":
            is_konsisd_hand = True
            print(is_konsisd_hand)


stricha_for_ten_long([" short", "muchlongerstring", "hand", "adequate", "extremelylongstringexample"])
is_konsisd([" short", "muchlongerstring", "hand", "adequate", "extremelylongstringexample"])

