from flask import Flask, render_template,redirect, request

from sklearn.externals import joblib

#__name__== __main__

app=Flask(__name__)

model=joblib.load("model.pkl")

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def marks():
	if request.method=='POST':
		hours=float(request.form['hours'])

		marks=float(model.predict([[hours]])[0][0])
		marks=round(marks, 2)

		return render_template("index.html", your_marks=marks)

if __name__=='__main__':
	app.run(debug=True)