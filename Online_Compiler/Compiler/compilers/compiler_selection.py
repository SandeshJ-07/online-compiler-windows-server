from .c_language import compile_C
from .cpp_language import compile_Cpp
from .cpp11_language import compile_Cpp11
from .cpp14_language import compile_Cpp14
from .cpp17_language import compile_Cpp17
from .java_language import compile_Java
from .python3_language import compile_Python3


def c_compiler(code, inputt):
    output = compile_C(code, inputt)
    return output

def cpp_compiler(code, inputt):
    output = compile_Cpp(code, inputt)
    return output

def cpp11_compiler(code, inputt):
    output = compile_Cpp11(code, inputt)
    return output

def cpp14_compiler(code, inputt):
    output = compile_Cpp14(code, inputt)
    return output

def cpp17_compiler(code, inputt):
    output = compile_Cpp17(code, inputt)
    return output

def java_compiler(code, inputt):
    output = compile_Java(code, inputt)
    return output


def python3_compiler(code, inputt):
    output = compile_Python3(code, inputt)
    return output