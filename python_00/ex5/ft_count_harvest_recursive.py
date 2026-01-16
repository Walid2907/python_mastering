def ft_count_harvest_recursive(day=1):
    if day == 1:
        days = int(input("Days until harvest: "))
        # since functions in python are objects
        # that means we can store attributes in it (variables)
        # which works as a global variable but only for the function
        ft_count_harvest_recursive.days = days

    if day > ft_count_harvest_recursive.days:
        print("Harvest time!")
        return

    print(f"Day {day}")
    ft_count_harvest_recursive(day + 1)
