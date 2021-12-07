count = 0

prev_window = (0, 0, 0)

with open("input") as input:
    for line in input.readlines():
        int_val = int(line)
        new_window = (prev_window[1], prev_window[2], int_val)
        if all(depth > 0 for depth in prev_window) and sum(new_window) > sum(
            prev_window
        ):
            print(prev_window, new_window, sum(prev_window), sum(new_window))
            count += 1
        prev_window = new_window

print(f"Total Count: {count}")
