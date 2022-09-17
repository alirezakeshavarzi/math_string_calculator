from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def initio(str):
    i = 0
    lo = len(str)
    while i < lo:
        str[i] = "00"
        i += 1

def getnum(str):
    i = 0
    l = len(str)
    while i < l:
        if str[i].isdigit():
            return int(str[i])
            break

        i += 1

st2 = "1+2-3*4/8"
lstr = len(st2)

ans = [None] * lstr
initio(ans)
topans = 0

stack = [None] * 8
initio(stack)
top = -1
stack[top] = "00"

i = 0
while i < lstr:
    if st2[i].isdigit():
        ans[topans] = st2[i]
        topans += 1
    else:
        if st2[i] == '+':
            num = getnum(stack[top])

            if 2 > num:
                top += 1
                stack[top] = "+2"

            elif 2 < num:
                top += 1
                ans[topans] = stack[top]
                stack[top] = "+2"
                topans += 1
        elif st2[i] == '-':
            num = getnum(stack[top])
            if 1 > num:
                top += 1
                stack[top] = '-1'

            elif 1 < num:
                ans[topans] = stack[top]
                stack[top] = '-1'
                topans += 1
        elif st2[i] == '*':
            num = getnum(stack[top])
            if 4 > num:
                top += 1
                stack[top] = '*4'

            elif 4 < num:
                ans[topans] = stack[top]
                stack[top] = '*4'
                topans += 1
        elif st2[i] == '/':
            num = getnum(stack[top])
            if 3 > num:
                top += 1
                stack[top] = '/3'

            elif 3 < num:
                ans[topans] = stack[top]
                stack[top] = '/3'
                topans += 1
        elif st2[i] == '^':
            num = getnum(stack[top])
            if 5 > num:
                top += 1
                stack[top] = '^5'

            elif 5 < num:
                ans[topans] = stack[top]
                stack[top] = '^5'
                topans += 1
    i += 1

def stackintoArr(s2, stack3, t):
    i = 0
    t = t
    l = len(s2)
    while i < l:
        if s2[i] == '00':
            s2[i] = stack3[t]
            t -= 1
        i += 1

def zero(st):
    i = 0
    l = len(st)
    while i < l:
        st[i] = 0
        i += 1

def isfloat(w):
    w = str(w)
    i = 0
    l = len(w)
    while i < l:
        if w[i] == '.':
            return True
        i += 1

def cal(arr, stack2):
    i = 0
    l = len(arr)
    top = -1
    zero(stack2)
    while i < l:
        print('stack = ', stack2)
        print('ans = ', arr)
        print('top = ', top)
        print(' ')
        if arr[i].isdigit():
            top += 1
            stack[top] = arr[i]

        else:
            if arr[i] == '+2':
                if isfloat(stack2[top - 1]) or isfloat(stack2[top]):
                    stack2[top - 1] = float(stack2[top - 1]) + float(stack2[top])
                    stack2[top] = 0
                    top -= 1
                else:
                    stack2[top - 1] = int(stack2[top - 1]) + int(stack2[top])
                    stack2[top] = 0
                    top -= 1


            elif arr[i] == '*4':
                if isfloat(stack2[top - 1]) or isfloat(stack2[top]):
                    stack2[top - 1] = float(stack2[top - 1]) * float(stack2[top])
                    stack2[top] = 0
                    top -= 1
                else:
                    stack2[top - 1] = int(stack2[top - 1]) * int(stack2[top])
                    stack2[top] = 0
                    top -= 1
            elif arr[i] == '-1':
                if isfloat(stack2[top - 1]) or isfloat(stack2[top]):
                    stack2[top - 1] = float(stack2[top - 1]) - float(stack2[top])
                    stack2[top] = 0
                    top -= 1
                else:
                    stack2[top - 1] = int(stack2[top - 1]) - int(stack2[top])
                    stack2[top] = 0
                    top -= 1
            elif arr[i] == '/3':
                if isfloat(stack2[top - 1]) or isfloat(stack2[top]):
                    stack2[top - 1] = float(stack2[top - 1]) / float(stack2[top])
                    stack2[top] = 0
                    top -= 1
                else:
                    stack2[top - 1] = int(stack2[top - 1]) / int(stack2[top])
                    stack2[top] = 0
                    top -= 1
        i += 1
    return stack[0]

stackintoArr(ans, stack, top)

print('answer = ', ans)
print('stack = ', stack)
print(str)
print('cal = ', cal(ans, stack))


def index(r):
    a = r.GET.get('str', False)
    temp = loader.get_template('index.html')
    res = cal(ans, stack)

    c = {'res' : res, 'a':a}
    return HttpResponse(temp.render(c,r))
# Create your views here.
