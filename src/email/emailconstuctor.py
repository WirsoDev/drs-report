

html =f'''
<html lang="en">
    <head>
        <style>
            body{{
                font-family: sans-serif;
            }}
            .cont{{
                display: flex;
                width: 100vw;
                height: 100vh;
            }}
            .title{{
                display: flex;
                flex-direction: column;
                align-items: center;
                align-self: center;
            }}
            .hello{{
                color: rgb(66, 66, 66);
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="cont">
            <div class="title">
                <h1 class="hello">Hello World</h1>
            </div>
        </div>
    </body>
</html>
'''

with open(r'./email.html', 'w') as file:
    file.write(html)
    print('email.html updated')

