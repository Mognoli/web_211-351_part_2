from flask import Flask, render_template, request, make_response

app = Flask(__name__)
application = app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/headers')
def headers():
    return render_template("headers.html")
    
@app.route('/args')
def args():
    return render_template("args.html")

@app.route('/cookies')
def cookies():
    resp = make_response(render_template("cookies.html"))
    if 'q' in request.cookies: 
        resp.set_cookie('q', 'qq', expires = 0)
    else:
        resp.set_cookie('q', 'qq')

    return resp

@app.route('/form', methods = ['GET', 'POST'])
def form():
    return render_template("form.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/number', methods = ['GET', 'POST'])
def number():
    errormsg = None
    true_numbermsg = None
    chek_mas = ['.', ' ', '(', ')', '-', '+']
    if request.method == 'POST': 
        # try: 
            op1 = str(request.form.get('operand1'))
            n=0
            for i in op1:
                if i.isdigit():
                    n+=1
                elif not i in chek_mas:
                    errormsg = "Недопустимый ввод. В номере телефона встречаются недопустимые символы."
                    break
            if not n == 10 and not errormsg:
                if not (n == 11 and ( op1[0] == '+' and op1[1] == '7' or op1[0] == '8')):
                    errormsg = "Недопустимый ввод. Неверное количество цифр."
            if not errormsg:
                true_numbermsg = "Номер введен верно"
    return render_template('number.html', true_numbermsg=true_numbermsg, errormsg=errormsg)