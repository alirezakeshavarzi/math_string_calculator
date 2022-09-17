from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def cal(s):
    l = len(s)
    i = 0
    ans = 0
    while i < l:
        if s[i] == '+':
            u = s[0:i]
            n = s[i+1:l]
            try:
                u = int(u)
            except ValueError:
                u = float(u)
            try:
                n = int(n)
            except ValueError:
                n = float(n)
            return (u + n)
            break
        elif s[i] == '-':
            u = s[0:i]
            n = s[i + 1:l]
            try:
                u = int(u)
            except ValueError:
                u = float(u)
            try:
                n = int(n)
            except ValueError:
                n = float(n)
            return (u - n)
            break
        elif s[i] == '*':
            u = s[0:i]
            n = s[i + 1:l]
            try:
                u = int(u)
            except ValueError:
                u = float(u)
            try:
                n = int(n)
            except ValueError:
                n = float(n)
            return (u * n)
            break
        elif s[i] == '/':
            u = s[0:i]
            n = s[i + 1:l]
            try:
                u = int(u)
            except ValueError:
                u = float(u)
            try:
                n = int(n)
            except ValueError:
                n = float(n)
            return (u / n)
            break


        i += 1

def index(r):
    a = r.GET.get('str', False)
    temp = loader.get_template('index.html')
    try:
        res = cal(str(a))
    except ValueError:
        eror = " After a operator must be a number!"
        eror2 = "ERROR"
        c = {'e': eror, 'a':a, 'e2':eror2}
        return HttpResponse(temp.render(c,r))

    c = {'res' : res, 'a':a}
    return HttpResponse(temp.render(c,r))
# Create your views here.
