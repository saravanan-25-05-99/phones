from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from .models import Student

def mathoperation(request, operationType):
    
    if (request.GET.get('number1') and  request.GET.get('number2')):
        number1 = request.GET['number1']
        number2 = request.GET['number2']
        result = 0
        if(operationType == 'add'):
            result = float(number1) + float(number2)

        if(operationType == 'sub'):
            result = float(number1) - float(number2)

        if(operationType == 'mul'):
            result = float(number1) * float(number2)

        if(operationType == 'div'):
            result = float(number1) / float(number2)
            
        return HttpResponse("Result :" + str(result))
    return HttpResponse("Please provide number1 and number2")
   

def primenumber(request):
    if (request.GET.get('number')):
        number = request.GET['number']
        if int(number) == 1:
            return HttpResponse(str(number) +" "+"Is not a prime number")
        elif int(number) > 1:
            for i in range(2, int(number)):
                if ((int(number)) % i )== 0 :
                    return HttpResponse(str(number)+" "+ "Is not a prime number")   
                else:
                    return HttpResponse(str(number) +" "+"Is a prime number")
        else:
            return HttpResponse(str(number) +" "+"Is a prime number")
    return HttpResponse("Please provide number")
            
   
   
def factorial(request):
    if (request.GET.get('factorial')):
        factorial = request.GET['factorial']
        fact = 1
        result = 0
        returnValue= ''
        for i in range (1 ,int(factorial)+1):
            fact = fact * i
            returnValue += "factorial of given number is:"+str(fact)+"<br>"
        return HttpResponse(returnValue)
    return HttpResponse("PLease Enter Number")


def forpage(request):
    
        students = {
            'Subjectname': "maths",
            
            'mark':[
              
              {
                  "name": "Sandrine", 
                  "score": 100
                  },
              {
                  "name": "Gergeley",
                  "score": 87
                  },
              {
                  "name": "Frieda",
                  "score": 92
                  },
              {
                  "name": "Fritz", 
                  "score": 40
                  },
              {
                  "name": "Sirius",
                  "score": 75
                  }
            ] 
        }
        return render(request,"forpage.html", {'students': students})

def simplehtmlpage(request):
    
        students = {
           
            "name1": "Sandrine",  "score1": 100,
              "name2": "Gergeley", "score2": 87,
              "name3": "Frieda", "score3": 92,
              "name4": "Fritz", "score4": 40,
              "name5": "Sirius", "score5": 75,
   
   
        }
        return render(request,"simple.html", {'data': students})
    
def block(request):
    return render(request,"childblock.html")

def variable(request):
    return render(request,"variable.html")

def simpleform(request):
    result=0
    if request.method == "GET":
        return render(request, "simpleform.html",{})
    if request.method == "POST":
        number1=request.POST.get('number1')
        number2=request.POST.get('number2')
        method=request.POST.get('method')
        if method=='add':
            result= float(number1) + float(number2)
        elif method=='sub':
            result= float(number1) - float(number2)
        elif method=='mul':
            result= float(number1) * float(number2)
        elif method=='div':
            result= float(number1) % float(number2)
        return render(request,"simpleform.html",{"number1":number1,"number2":number2,'method':method,'result':str(result)})
    
    
def multiplemath(request):
    result=0
    if request.method == "GET":
        return render(request, "multiplemath.html",{})
    if request.method == "POST":
        number=request.POST.get('number')
        method=request.POST.get('method')
        if method == 'primenumber':
            if int(number) == 1:
                     returnValue = str(number) +" "+"Is not a prime number"
            elif int(number) > 1:
                for i in range(2, int(number)):
                    if ((int(number)) % i )== 0 :
                             returnValue = str(number)+" "+ "Is not a prime number"   
                else:
                         returnValue = str(number) +" "+"Is a prime number"
            else:
                     returnValue = str(number) +" "+"Is a prime number"
        elif method == 'addoreven':
            if (int(number)%2)==0:
                returnValue = str(number) +" "+"Is Even number"
            else:
                returnValue = str(number) +" "+"Is Even number"
                
        elif method == 'factorial':
             fact = 1
             result = 0
             returnValue= ''
             for i in range (1 ,int(number)+1):
                fact = fact * i
             returnValue += "factorial of given number is:"+str(fact)+""
             
        return render(request,"multiplemath.html",{"number":number,'method':method,'result':str(returnValue)})
       
        #return render(request,"multiplemath.html",{"number":number,'method':method,'result':str(result)})
    
def palindrome(request):
    result=0
    returnValue=''
    if request.method == "GET":
        return render(request, "palindrome.html",{})
    if request.method == "POST":
        name=request.POST.get('name')
        method=request.POST.get('method')
        if method == 'palindrome':
            nam=name[::-1]
            if nam==name:
                returnValue += str(name) +" "+"Is Palindrome"
            else:
                returnValue += str(name) +" "+"Is Not Palindrome"
                
    elif request.method == 'fibonacci':
        n1, n2 = 0, 1
        count = 0
        if name <= 0:
            returnValue +="Please enter a positive integer"
        elif name == 1:
            returnValue += "Fibonacci sequence upto",name,":"
        else:
           returnValue +="Fibonacci sequence:"
           while count < name:
              returnValue +=(n1)
              nth = n1 + n2
              n1 = n2
              n2 = nth
              count += 1
    
    return render(request,"palindrome.html",{'name':name,'method':method,'result':str(returnValue)})
        
        
        
        
def studentregistrationform(request):
    if request.method == "GET":
        return render(request, "studentregistrationform.html",{})
    
    if request.method == "POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        phone=request.POST.get('phone')
        course= request.POST.get('course')
        gender= request.POST.get('gender')
        address= request.POST.get('address')
        email= request.POST.get('email')
        student = Student();
        student.firstname = firstname
        student.lastname = lastname
        student.phone = phone
        student.course = course
        student.gender = gender
        student.address = address
        student.email = email
        student.save()
        return render(request,"studentform.html",student) 
    
def calculator(request):
    return render(request,"calculator.html")    