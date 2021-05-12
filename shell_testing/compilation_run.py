import subprocess

print("inside python file")
subprocess.call(["gcc", "main.c"])
subprocess.call("./a.out")
print("executed c")


# c-compile gcc main.c
# a.exe < input.txt

# c++-compile g++ main.cpp
# a.exe < input.txt