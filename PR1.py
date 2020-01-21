from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():

    if request.method == "POST":

        a=float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        value=round((-b+(b**2-4*a*c)**0.5)/2*a,3)
        value2 = round((-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a, 3)
        return render_template("1.html", a=a, b=b,c=c, value=value,value2=value2)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug = True)