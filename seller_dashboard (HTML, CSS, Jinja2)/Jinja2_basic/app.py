from jinja2 import Template

'''
to run part for the section you just need to uncomment that part by 
selecting that part with mouse then pressing Ctrl button with backslash button (/)
'''

def main():
    # --------------------------------------------------------------------------------------------------
    # Using template inside the code

    html_template='''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Jinja2 Demo</title>
    </head>
    <body>
        <h1>Hello My Name is {{name}}</h1>
    </body>
    </html>
    '''
    # name_input=input('Enter Your Name: ') #input
    # t=Template(html_template)
    # output=t.render(name=name_input)
    # g=open('index.html','w')
    # g.write(output)
    # g.close()

    # --------------------------------------------------------------------------------------------------
    # Using template as external file
    
    # template_file=open('template_1.html.jinja2','r')
    # html_template=template_file.read()
    # name_input=input('Enter Your Name: ')  #input
    # t=Template(html_template)
    # output=t.render(name=name_input)
    # g=open('index.html','w')
    # g.write(output)
    # template_file.close()
    # g.close()

    # --------------------------------------------------------------------------------------------------
    # template using python dictionary

    # dic={'name':'Jayvin','subject':'Appdev-1'}
    # template_file=open('template_2.html.jinja2','r')
    # html_template=template_file.read()
    # t=Template(html_template)
    # output=t.render(student=dic)
    # g=open('index.html','w')
    # g.write(output)
    # template_file.close()
    # g.close()

    # --------------------------------------------------------------------------------------------------
    # another way using python dictionary

    # student={'name':'Jayvin','subject':'Appdev-1'}
    # template_file=open('template_3.html.jinja2','r')
    # html_template=template_file.read()
    # t=Template(html_template)
    # output=t.render(student)          #here jinja2 will automatically unpackge the dictionary
    # g=open('index.html','w')
    # g.write(output)
    # template_file.close()
    # g.close()
    
    # --------------------------------------------------------------------------------------------------
    # template using python list of dictionary (for loop in Jinja2)
    
    # List_of_students=[
    #     {'name':'Jayvin','subject':'Appdev-1'},
    #     {'name':'Laxminandan','subject':'Appdev-2'},
    #     {'name':'Viraj','subject':'MLT'}
    #     ]
    # template_file=open('template_4.html.jinja2','r')
    # html_template=template_file.read()
    # t=Template(html_template)
    # output=t.render(students=List_of_students)
    # g=open('index.html','w')
    # g.write(output)
    # template_file.close()
    # g.close()

    # --------------------------------------------------------------------------------------------------
    # template using python list of dictionary (if, elif, else in Jinja2)
    
    # List_of_students=[
    #     {'name':'Jayvin','subject':'Appdev-1'},
    #     {'name':'Laxminandan','subject':'Appdev-2'},
    #     {'name':'Viraj','subject':'MLT'}
    #     ]
    # template_file=open('template_5.html.jinja2','r')
    # html_template=template_file.read()
    # t=Template(html_template)
    # output=t.render(students=List_of_students)
    # g=open('index.html','w')
    # g.write(output)
    # template_file.close()
    # g.close()


if __name__=='__main__':
    main()
