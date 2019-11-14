from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

msg=[{
    'text':'hi',
    'author':'richard'
},{
    'text':'hi',
    'author':'tony'
}]

@app.route("/",methods=["GET"])
def show_Hello():
    # return "<h1>Hello World</h1>"
#   print(request.method)
     return render_template("index.html",mylist=msg)
   
@app.route("/", methods=["POST"])
def add_message():
    msseg=request.form['inputmsg']
    msseg_dic={
        'author':'bunny',
        'text':msseg
    }
    msg.append(msseg_dic)
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)



