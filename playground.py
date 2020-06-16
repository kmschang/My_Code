def loading2():
    import sys
    import time
    print("Loading progress bar...")
    for i in range(0, 100):
        time.sleep(0.05)
        width = (i + 1) / 4
        bar = "[" + "#" * int(width) + " " * (25 - int(width)) + "]"
        sys.stdout.write(u"\u001b[1000D" + bar)
        sys.stdout.flush()
    print("\n")

loading2()

print("Hello")
