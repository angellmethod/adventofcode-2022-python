with open('input.txt') as f:
    calories = []
    curr_calories = 0
    cnt = 0
    for line in f:
        if line == "\n":
            if len(calories) < 3:
                calories.append(curr_calories)
                if len(calories) == 3:
                    calories.sort(reverse=True)
            else:
                if curr_calories > calories[-1]:
                    calories[-1] = curr_calories
                    calories.sort(reverse=True)
            print(f"Elf {cnt}: Calories: {curr_calories}")
            curr_calories = 0
            cnt += 1
        else:
            curr_calories += int(line)
    print(f"{calories[:3]}")
    print(f"Sum {sum(calories[:3])}")
    