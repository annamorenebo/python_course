mon_down = int(input("Сколько монет гербом? "))
mon_up = int(input("Сколько монет решкой? "))
if mon_up <= mon_down:
    print(f"перевернуть {mon_up}")
else:
    print(f"перевернуть {mon_down}")
