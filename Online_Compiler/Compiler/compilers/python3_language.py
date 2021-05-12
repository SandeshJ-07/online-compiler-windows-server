import os.path
import os
import pprint
import shlex
import subprocess

def compile_Python3(code, inputt):
    save_path = './code_compile_run/python/'
    #set the path
    CC = "py"
    #out = "./a.out"
    code = code
    inputt = inputt
    #filename_code = "main.py"
    filename_code = os.path.join(save_path, "main.py")
    filename_in = os.path.join(save_path, "input.txt")
    # filename_in = "input.txt"
    filename_error = os.path.join(save_path, "error.txt")
    # filename_error = "error.txt"
    #executable = "a.out"
    command = CC+" "+filename_code
    command_error = command+" 2>"+filename_error
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
    #function exec(system call)
    #referenc - https://en.wikipedia.org/wiki/Exec_(system_call)
    # python - https://www.programiz.com/python-programming/methods/built-in/exec
    #exec("chmod 777 executable")
    #exec(filename_error)

    #shlex.split(command_error)
    '''
    error = open(filename_error, 'r')
    error = error.read()
    '''
    # error check
    os.system(command_error)

    with open(filename_error, "r") as myfile:
        data = myfile.readlines()

    # checking whether its error or not
    if len(data) == 0:
        error = ""
    else:
        error = data
    #print("direct_program run\n")
    #exec(code, inputt)

    if error =="":
        if input=="":
            #output = os.system(command)
            #output = subprocess.check_output(command, shell=True)
            out = command + " > " + output_file
            os.system(out)

        else:
            command = command+" < "+ filename_in + " > " + output_file
            os.system(command)
            #output = subprocess.check_output(command, shell=True)

        # output file generated
        with open(output_file, "r") as outfile:
            d = outfile.readlines()
        output = d

        return output

    else:
        return error

