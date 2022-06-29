import sys

from django.shortcuts import render

# Create your views here.

#indexfunction
def index(request):
    return render(request, 'index.html')

def scratch(request):
    return render(request, 'scratch.html')

#runcodefunction
def runcode(request):
    if request.method == "POST":
        code = request.POST['codearea']

        try:
            #save original standart output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the stdout to the file we made

            #execute code

            exec(code)
            sys.stdout.close()

            sys.stdout = original_stdout #reset the value

            #finally read output from file and save output variable

            output = open('file.txt', 'r').read()
        except Exception as e:
            #to return errors in the code
            sys.stdout = original_stdout
            output = "Error: \n" + str(e)

    return render(request, 'index.html', {
        'code': code,
        'output': output,
    })