time_seconds = int(input("Введите время в секундах: "))
hours = time_seconds / 3600
minutes = time_seconds / 60
print(f"время в формате чч:мм:сс {hours:.1f}:{minutes:.1f}:{time_seconds:.1f}")
