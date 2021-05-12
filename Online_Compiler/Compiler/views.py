from django.shortcuts import render, HttpResponse, redirect
from .compilers import compiler_selection
import json
import os.path
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

#path_for_every output
#c_path = '../code_compile_run/c/output.txt'
c_path ="E:\Online-compiler-testing-ui\compiler\Online_Compiler\code_compile_run\c\output.txt"


# Create your views here.
def First_Compiler(request):
    output = None
    code = ""
    fname= None
    language= None
    if request.method == 'POST'and request.is_ajax:
        print(request.POST)
        dd = request.POST
        fname = dd['fname']
        if (fname == ""):
            fname = "Untitled document"
        language = dd['language']
        code = dd['code_code']
        inputt = ""
        output = compile(language, code, inputt)

        return HttpResponse(output)

        #d = {'output': output, 'code':code, 'language':language, 'fname':fname}
        #return render(request, 'compiler.html', d)

        # dic = {'output':output}
        # return HttpResponse(json.dumps(dic), content_type='application/json')

    #fetching file
    #output = None
    #fname = ['codefile']
    #language = 'c'
    #c_code = '#include <stdio.h>\r\n   int main(){\r\n    printf("hello");\r\n    return 0;\r\n  }'
    #p_code = 'a= int(input())\nb=int(input())\nprint("sum is",a+b)\nprint("run through internal not from form")'
    #code = c_code
    #inputt = "20\n20"

    #sending to compiler
    #output = compile(language, code, inputt)

    d = {'output': output, 'code':code, 'language':language, 'fname':fname}
    return render(request, 'compiler-no-ui.html', d)



def compile(language,code, inputt):
    if language =='c':
        output = compiler_selection.c_compiler(code, inputt)
        return output

    elif language =='c++':
        output = compiler_selection.cpp_compiler(code, inputt)
        return output

    elif language =='c++11':
        output = compiler_selection.cpp11_compiler(code, inputt)
        return output

    elif language =='c++14':
        output = compiler_selection.cpp14_compiler(code, inputt)
        return output

    elif language =='c++17':
        output = compiler_selection.cpp17_compiler(code, inputt)
        return output

    elif language =='java':
        output = compiler_selection.java_compiler(code, inputt)
        return output

    elif language =='python3':
        output = compiler_selection.python3_compiler(code, inputt)
        return output

def Main_Compiler(request):
    output = None
    code = ""
    inputt = ""
    language = None
    #if request.method == 'POST' and request.is_ajax:
    if request.method == 'POST' and request.is_ajax:
        dd = request.POST
        try:
            inputt = dd['inputt']
        except:
            inputt= ""
        language = dd['language']
        code = dd['code_code']
        output = compile(language, code, inputt)

        #ajax_response
        return HttpResponse(output)

        #d = {'output': output, 'code':code, 'language':language, 'inputt':inputt}
        #return render(request, 'main_compiler.html', d)

        # dic = {'output':output}
        # return HttpResponse(json.dumps(dic), content_type='application/json')

    d = {'output': output, 'code': code, 'language': language, 'inputt':inputt}
    return render(request, 'main_compiler.html', d)

def Profile(request):

    return render(request, 'user_profile.html')

#signup
'''
def signup(request):
    error = False
    if request.method == 'POST':
        dd = request.POST
        n = dd['name']
        u = dd['un']
        e = dd['em']
        p = dd['pwd']
        i = request.FILES['img']
        udata = User.objects.filter(username=u)
        if udata:
            error = True
        else:
            user = User.objects.create_user(username=u, password=p, email=e, first_name=n)
            UserDetail.objects.create(usr=user, image=i)
            return redirect('login')
    d = {"allcat": All_category(), "error": error}
    return render(request, 'signup.html', d)
'''

def Login(request):
    error = False
    if request.method == 'POST':
        x = request.POST
        us = x['usr']
        pa = x['pwd']
        user = authenticate(username=us, password=pa)

        if user:
            login(request, user)
            return redirect('Compiler:Profile')
        else:
            error = True
    d = {"error": error}
    return render(request, 'login.html', d)

def Logout(request):
    logout(request)
    return redirect('Compiler:Login')


##run and get output
def Test(inputt, exoutput, youroutput):
    pass


##pratice

#1. all_questions
def Pratice(request):
    question_data = Pratice_Problems.objects.all()
    solution_data = User_Pratice_Solution.objects.all()
    d = {'question':question_data}
    return render(request, 'pratice_questions.html',d)

import re
#a=''
#for k in a.split("\n"):
    #print(re.sub(r"[^a-zA-Z0-9]+", ' ', k))

#2. question_compile dyanmic dynamic url
def Solve_Pratice_Problem(request, pid):
    data = Pratice_Problems.objects.get(id=pid)

    #if getting request
    if request.method == 'POST' and request.is_ajax:
        dd = request.POST
        try:
            inputt = dd['inputt']
        except:
            inputt = ""
        inputt = data.inputt1

        language = dd['language']
        code = dd['code_code']
        output = compile(language, code, inputt)

        #test case check
        inn = data.inputt1
        ou = data.ex_outputt1

        #putting into txt for compairing
        #ex_output
        file_ex = open('./ex_output.txt', "w")
        file_ex.write(ou)
        file_ex.close()


        #read and remove ex
        with open('./ex_output.txt', "r") as myfile:
            output_ex = myfile.readlines()
        os.remove('./ex_output.txt')

        #checking and passing for the test case
        x = re.sub(r"[^a-zA-Z0-9]+", ' ', str(output_ex))

        if output == output_ex:
            message = "Test case Passed!"
            dic = {'output': x, 'message': message, 'test_case': inn, 'expected_output': ou}

        else:
            message = "Test case did'nt passed!"
            dic = {'output': x, 'message': message, 'test_case': inn, 'expected_output': ou}

        jfile = json.dumps(dic)
        return HttpResponse(jfile, content_type='application/json')


            #return HttpResponse(output, message)
            #ddd ={'output':output,"message":message,"expected_output":ou}
            #return render(request, 'pratice_compiler.html', ddd)

    d = {'data':data}
    return render(request, 'pratice_compiler.html',d)


##contest
#1.all_contest
def All_Contest(request):
    data = All_Contest_Data.objects.all()
    dm = {"all_contest":data}
    print(dm)
    return render(request, 'contest.html',dm)

#2.single_contest dyanmic
def Get_Into_Competition(request, cid):
    data = All_Contest_Data.objects.get(id=cid)
    contest_questions = Contest_Questions.objects.all()

    #contest_data.title == con.contest_id

    dm ={"contest_data":data, 'contest_question':contest_questions}
    return render(request, 'single-contest.html', dm)

#3.competition_compiler dyanmic
def Solve_Competition_Problem(request, cpid):
    data = Contest_Questions.objects.get(id=cpid)

    #if getting request
    if request.method == 'POST' and request.is_ajax:
        dd = request.POST
        try:
            inputt = dd['inputt']
        except:
            inputt = ""
        inputt = data.inputt1

        language = dd['language']
        code = dd['code_code']
        output = compile(language, code, inputt)

        # test case check
        inn = data.inputt1
        ou = data.ex_outputt1

        # putting into txt for compairing
        # ex_output
        file_ex = open('./ex_output.txt', "w")
        file_ex.write(ou)
        file_ex.close()

        # read and remove ex
        with open('./ex_output.txt', "r") as myfile:
            output_ex = myfile.readlines()
        os.remove('./ex_output.txt')

        # checking and passing for the test case
        output_ex = re.sub(r"[^a-zA-Z0-9]+", ' ', str(output_ex))
        output = re.sub(r"[^a-zA-Z0-9]+", ' ', str(output))


        if output == output_ex:
            message = "Test case Passed!"
            dic = {'output': output_ex, 'message': message, 'test_case': inn, 'expected_output': ou}

        else:
            message = "Test case did'nt passed!"
            dic = {'output': output, 'message': message, 'test_case': inn, 'expected_output': ou}

        jfile = json.dumps(dic)
        return HttpResponse(jfile, content_type='application/json')

    d = {'data':data}
    return render(request, 'competition_compiler.html',d)