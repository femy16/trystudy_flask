from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__) #app is a flask application


messages=["hello","happy birthday","to","me"]

@app.route("/",methods=["GET"]) #"/"root of the website
def show_hi():
    # print("***************")
    # print(request.method)
    # return render_template("index.html",data=messages)
    return "<h1><a href='http://www.example.com'>Hi</h1>"
    # with open("templates/index.html")as f:
    #     html=f.read()
    #     return html

@app.route("/add", methods=["POST"])
def add_message():
    messages.append(request.form['msg'].upper())
    return redirect(url_for("show_hi"))
    

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)