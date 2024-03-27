import os
from subprocess import check_output

from .models import LanguageChoice, QuestionChoice

def run_python(file):
    pass

def execute(language, question, binary_code):
    if language==LanguageChoice.python:
        runner = os.path.join('runtime_environment','python',"runner.py")
        path = os.path.join('runtime_environment','python')
        ext = ".py"
    elif language==LanguageChoice.cpp:
        runner = os.path.join('runtime_environment','cpp',"runner.cpp")
        path = os.path.join('runtime_environment','cpp')
        ext = ".cpp"
    elif language==LanguageChoice.java:
        runner = os.path.join('runtime_environment','java',"Runner.java")
        path = os.path.join('runtime_environment','java')
        ext = ".java"
    
    if question==QuestionChoice.q1:
        file_name='q1' + ext
    if question==QuestionChoice.q2:
        file_name='q2' + ext
    if question==QuestionChoice.q3:
        file_name='q3' + ext
    if question==QuestionChoice.q4:
        file_name='q4' + ext

    with open(os.path.join(path,file_name),"rb") as template_file:
        template = template_file.read()
    

    out = ""
    if language==LanguageChoice.python:
        with open(runner,"wb") as runner_file:
            runner_file.write(binary_code)
            runner_file.write(template)
        try:
            out = check_output(f"python {runner}",shell=True).decode()
        except:
            out = "Code has error"
    elif language==LanguageChoice.java:
        with open(runner,"wb") as runner_file:
            runner_file.write(template)
            runner_file.write(binary_code)
            runner_file.write(b'}')
        try:
            check_output(f"javac {runner}",shell=True)
            out = check_output(f"cd {path} && java Runner",shell=True)
        except:
            out = "Code has error"
    
    elif language==LanguageChoice.cpp:
        with open(runner,"wb") as runner_file:
            runner_file.write(template)
            runner_file.write(binary_code)
        try:
            check_output(f"g++ {runner}",shell=True)
            out = check_output("./a.out",shell=True)
        except:
            out = "Code has error"
            

    return out
