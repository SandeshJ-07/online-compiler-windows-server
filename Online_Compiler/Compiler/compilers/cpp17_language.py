#g++ -std=c++17 main.cpp
#a.exe < input.txt > output.txt
import os
import os.path
import pprint
import shlex
import subprocess

def compile_Cpp17(code, inputt):
    # set the path
    # path =C:\Program Files (x86)\CodeBlocks\MinGW\bin
    save_path = './code_compile_run/c++17/'
    CC = "g++ -std=c++17"
    out = "a.exe"
    code = code
    inputt = inputt
    filename_code = os.path.join(save_path, "main.cpp")
    # filename_code = "main.cpp"
    filename_in = os.path.join(save_path, "input.txt")
    # filename_in = "input.txt"
    filename_error = os.path.join(save_path, "error.txt")
    # filename_error = "error.txt"
    executable = "a.exe"
    command = CC + " " + filename_code
    command_error = command + " 2>" + filename_error
    output_file = os.path.join(save_path, "output.txt")
    # output_file = "output.txt"

    # empty condition will se later
    if code == "":
        output = "code is empty"
        return output

    ##writing code to main file
    file_code = open(filename_code, "w")
    file_code.write(code)
    file_code.close()

    ##giving input to main file
    file_in = open(filename_in, "w")
    file_in.write(inputt)
    file_in.close()

    ##execution
    # function exec(system call)
    # referenc - https://en.wikipedia.org/wiki/Exec_(system_call)
    # python - https://www.programiz.com/python-programming/methods/built-in/exec

    # compilation
    command = command + ' -o ' + save_path + 'a.exe'
    os.system(command)

    # error check
    os.system(command_error)

    with open(filename_error, "r") as myfile:
        data = myfile.readlines()

    # checking whether its error or not
    if len(data) == 0:
        error = ""
    else:
        error = data

    # futher execution
    if error == "":
        if input == "":
            out = out + " > " + output_file
            os.system(out)
        else:
            out1 = out + " < " + filename_in + " > " + output_file
            os.system(out1)

        # output file generated
        with open(output_file, "r") as outfile:
            d = outfile.readlines()
        output = d

        return output

    else:
        return error