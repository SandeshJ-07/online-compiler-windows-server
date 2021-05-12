#gcc main.c
#a.exe < input.txt
#a.exe < input.txt > output.txt
#name
#gcc main.c -o executablefile

#if output.txt == given_true_output:
    #question will be right

import os.path
import os
import pprint
import shlex
import subprocess


def compile_C(code, inputt):
    #set the path
    #path =C:\Program Files (x86)\CodeBlocks\MinGW\bin

    #path to save code
    #save_path = 'E:/Online-compiler-testing-ui/compiler/Online_Compiler/code_compile_run/'
    save_path = './code_compile_run/c/'
    CC = "gcc"
    #out = os.path.join(save_path, "a.exe")
    out = "a.exe"
    code = code
    inputt = inputt
    filename_code = os.path.join(save_path, "main.c")
    #filename_code = "main.c"
    filename_in = os.path.join(save_path, "input.txt")
    #filename_in = "input.txt"
    filename_error = os.path.join(save_path, "error.txt")
    #filename_error = "error.txt"
    executable = "a.exe"
    command = CC+" "+filename_code
    command_error = command+" 2> "+filename_error
    output_file = os.path.join(save_path, "output.txt")
    #output_file = "output.txt"

    #empty condition will se later

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
    #function exec(system call)
    #referenc - https://en.wikipedia.org/wiki/Exec_(system_call)
    # python - https://www.programiz.com/python-programming/methods/built-in/exec

    #compilation
    #making exe to path
    command = command+' -o '+ save_path + 'a.exe'
    os.system(command)

    #error check
    os.system(command_error)

    with open(filename_error, "r") as myfile:
        data = myfile.readlines()

    #checking whether its error or not
    if len(data)==0:
        error=""
    else:
        error = data

    #futher execution
    if error == "":
        if input=="":
            out = out + " > " + output_file
            os.system(out)

        else:
            #out = out + " < " + filename_in
            # output = subprocess.check_output(out, shell=True)

            # without subprocess getting only output.txt with - os.system(command_to_be_executed)
            out1 = out + " < " + filename_in + " > " + output_file
            os.system(out1)

        # output file generated
        with open(output_file, "r") as outfile:
            d = outfile.readlines()
        output = d



        return output

    else:
        return error