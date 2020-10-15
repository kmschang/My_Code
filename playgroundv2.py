def ending():
    import sys
    import time
    print("End Game. Please Wiat!")
    for i in range(0, 100):
        time.sleep(.03)
        width = (i + 1) / 4
        bar = "[" + " " * int(width) + "•" * (25 - int(width)) + "]"
        sys.stdout.write(u"\u001b[1000D" + bar)
        sys.stdout.flush()
    print("\n")

ending()