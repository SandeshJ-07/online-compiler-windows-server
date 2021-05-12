#compilation - javac Main.java
#exectuon - java Main < input.txt
#java -classpath Online_Compiler/code_compile_run/java Main
#java -classpath E:\Online-compiler-testing-ui/compiler/Online_Compiler/code_compile_run/java Main


import os
import os.path
import pprint
import shlex
import subprocess

def compile_Java(code, inputt):
    #path - C:\Program Files\Java\jdk-11.0.1\bin
    save_path = './code_compile_run/java/'
    #save_path = 'E:/Online-compiler-testing-ui/compiler/Online_Compiler/code_compile_run/java/'
    CC = "javac"
    out = "java"
    oout = "Main"
    code = code
    inputt = inputt
    ##
    filename_code = os.path.join(save_path, "Main.java")
    filename_in = os.path.join(save_path, "input.txt")
    # filename_in = "input.txt"
    filename_error = os.path.join(save_path, "error.txt")
    # filename_error = "error.txt"
    runtime_file = os.path.join(save_path, "runtime.txt")
    executable = ".class"
    #for java path works differenlty
    command = CC + ' ' + save_path  +'Main.java'
    command_error = command + " 2> " + filename_error
    runtime_error_command = out+" -classpath "+save_path+" "+oout+ " 2> "+ runtime_file

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

    # compilation
    # making .class to path
    #compiled to the given path
    #-target command : command = CC + ' '+save_path + 'Main.java'
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
        #java runtime error

        '''
        os.system(runtime_error_command)
        with open(runtime_file, "r") as runerrorfile:
            derror = runerrorfile.readlines()
        # checking whether its error or not
        '''
        derror = []

        if len(derror) == 0:
            if input == "":
                #output = subprocess.check_output(out, shell=True)
                out = out +' -classpath '+ save_path +" "+oout+ " > " + output_file
                os.system(out)
            else:
                #out = out + " < " + filename_in
                #output = subprocess.check_output(out, shell=True)
                out1 = out +' -classpath '+ save_path +" "+oout+ " < " + filename_in + " > " + output_file
                os.system(out1)

            # output file generated
            with open(output_file, "r") as outfile:
                d = outfile.readlines()
            output = d

        else:
            output = derror

        return output


    else:
        return error