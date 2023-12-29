enames=[{'id':101,'name':'siddu','email':'siddu@gmail.com','gender':'male'},
        {'id':102,'name':'Rahul','email':'siddu@gmail.com','gender':'male'},
        {'id':103,'name':'sonia','email':'siddu@gmail.com','gender':'female'}
        ]
for ename in enames:
    if (ename['gender']== 'male'):
        print(ename['name'])