from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route ("/", methods=["GET", "POST"])
def home ():
    result = ""
    if "result" in request.args: 
        result = request.args["result"]
    if request.method == "POST":
        entered_number = request.form ["number"]
        result = converter(entered_number)
        if result == "Not Valid Input !!":
            return redirect (url_for ("home", result = "Not Valid! Please enter a number between 1 and 3999, inclusively."))
        else:
        	return redirect (url_for("result", number_decimal=entered_number, number_roman = result))
    else:
        return render_template ("index.html", result = result)
    
def converter(entry):	
	if entry.isdigit():
		if int(entry) > 3999:
			return "Not Valid Input !!"
		else:
			number = int(entry)
			rest1 = number%1000
			valueM = "M" * int(number/1000)
			
			rest2 = rest1%500
			valueD = "D" * int(rest1/500) if rest2 < 400 else "CD" * abs(int(rest1/500)-1)+"CM" * int(rest1/500)
			rest3 = rest2 % 100
			valueC = "C" * int(rest2/100) if rest1 <400 else ""
			rest4 = rest3 % 50
			valueL = "L" * int(rest3/50) if rest4<40 else "XL" * abs(int (rest3/50)-1) +"XC" * int(rest3/50)
			rest5 = rest4 % 10
			valueX = "X" * int(rest4/10) if rest4<40 else ""
			rest6 = rest5 % 5
			valueV = "V" * int(rest5/5) if rest6 < 4 else "IV" * abs(int (rest5/5)-1) +"IX" * int(rest5/5)
			valueI = "I" * rest6 if rest6<4 else ""
			result = valueM + valueD + valueC + valueL + valueX + valueV + valueI
			return result
	else:
		return "Not Valid Input !!"

@app.route("/result", methods = ["GET"])
def result():
    if "number_decimal" in request.args and "number_roman" in request.args: 
        number_decimal = request.args["number_decimal"]
        number_roman = request.args["number_roman"]
        print(request)
        print()
        print(request.args)
        return render_template("result.html", number_decimal = number_decimal, number_roman = number_roman)
    else:
        return render_template("result.html")
    

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
#    app.run(debug=True)
   