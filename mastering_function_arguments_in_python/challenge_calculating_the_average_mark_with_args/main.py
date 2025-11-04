def average_mark(name, *args):
    mark = round(sum(args)/len(args), 1) # average value rounded to the 1 num after the dot
    print(f"{name} got {mark}")


average_mark("Tom", 4.0, 3.5, 3.0, 3.3, 3.8)
average_mark("Dick", 2.5, 3.8)