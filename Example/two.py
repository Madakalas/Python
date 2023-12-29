enames=[{'id':101,'name':'siddu','email':'siddu@gmail.com','gender':'male'},
        {'id':102,'name':'Rahul','email':'siddu@gmail.com','gender':'male'},
        {'id':103,'name':'sonia','email':'siddu@gmail.com','gender':'female'}
        ]
def femaledata():
    if ename['gender']=='female':
        return True
    else:
        return False

filterobj = filter(femaledata,enames)
print(list(filterobj))