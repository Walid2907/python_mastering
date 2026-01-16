def ft_count_harvest_iterative():
    harvest_time = int(input("Days until harvest: "))
    for i in range(1, harvest_time + 1):
        print(f"Day {i}")
    print("Harvest time!")
