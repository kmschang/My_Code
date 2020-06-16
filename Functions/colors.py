import sys,time

print("Print in red")
print("\u001b[31mHelloWorld")
print("\u001b[0m")

print("Print in 8 colors")
print("\u001b[30m A \u001b[31m B \u001b[32m C \u001b[33m D \u001b[0m")
print("\u001b[34m E \u001b[35m F \u001b[36m G \u001b[37m H \u001b[0m")
print("\u001b[0m")

print("Print in 16 colors")
print("\u001b[30m A \u001b[31m B \u001b[32m C \u001b[33m D \u001b[0m")
print("\u001b[34m E \u001b[35m F \u001b[36m G \u001b[37m H \u001b[0m")
print("\u001b[30;1m A \u001b[31;1m B \u001b[32;1m C \u001b[33;1m D \u001b[0m")
print("\u001b[34;1m E \u001b[35;1m F \u001b[36;1m G \u001b[37;1m H \u001b[0m")
print("\u001b[0m")

print("Print in 256 colors")
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write("\u001b[38;5;" + code + "m " + code.ljust(4))
    print("\u001b[0m")
print("\u001b[0m")

print("Print 16 background colors")
print("\u001b[40m A \u001b[41m B \u001b[42m C \u001b[43m D \u001b[0m")
print("\u001b[44m A \u001b[45m B \u001b[46m C \u001b[47m D \u001b[0m")
print("\u001b[40;1m A \u001b[41;1m B \u001b[42;1m C \u001b[43;1m D \u001b[0m")
print("\u001b[44;1m A \u001b[45;1m B \u001b[46;1m C \u001b[47;1m D \u001b[0m")
print("\u001b[0m")

print("Print 256 background colors")
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write("\u001b[48;5;" + code + "m " + code.ljust(4))
    print("\u001b[0m")
print("\u001b[0m")

print("Print decorations")
print("\u001b[1m BOLD \u001b[0m\u001b[4m Underline \u001b[0m\u001b[7m Reversed \u001b[0m")
print("\u001b[1m\u001b[4m\u001b[7m BOLD Underline Reversed \u001b[0m")
print("\u001b[1m\u001b[31m Red Bold \u001b[0m")
print("\u001b[4m\u001b[44m Blue Background Underline \u001b[0m")
print("\u001b[0m")

def loading1():
    print("Loading progress percentage...")
    for i in range(0, 100):
        time.sleep(0.005)
        sys.stdout.write("\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print("\n")
loading1()

def loading2():
    print("Loading progress bar...")
    for i in range(0, 100):
        time.sleep(0.01)
        width = (i + 1) / 4
        bar = "[" + "#" * int(width) + " " * (25 - int(width)) + "]"
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    print("\n")
loading2()
