

from flask import Flask , render_template , request
import pickle
app = Flask(__name__) 
model = pickle.load(open('jaya.pkl','rb')) 
@app.route('/') 
def helloworld():
    return render_template("index.html")
@app.route('/login',methods = ['POST']) 
def admin():
    p = request.form["MAY"]
    q = request.form["JUN"]
    r = request.form["JUL"]
    s = request.form["AUG"]
    t = request.form["SEP"]
    u = request.form["PRECIPITATE"]
    v = request.form["LABEL"]
    z = [[float(p),float(q),float(r),float(s),float(t),float(u),float(v)]]
    y = model.predict(z)
    return render_template("index.html",y = "Occurence of Flood in % :"+str(y))
@app.route('/result')#url
def result():
    return "hie user"
if __name__ == "__main__" :
    app.run(debug = True)


