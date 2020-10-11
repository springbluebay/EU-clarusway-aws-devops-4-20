from flask import Flask, request, render_template

from julietmilisecondsconverter import milisecondsconverter

app = Flask(__name__)

@app.route("/", methods=["GET"])
def adder_page_get():
    return render_template ("index.html", not_valid=False, developer_name = "Mehmet")

@app.route("/", methods=["POST"])
def adder_page_post():
    alfa = request.form["number"]
    if not alfa.isdigit():
        return render_template ("index.html", not_valid=True, developer_name = "Mehmet")
    number = int(alfa)
    if number >= 1000:
        miliseconds = milisecondsconverter(number)
        number = number
        return render_template ("result.html", miliseconds=miliseconds, number=number, developer_name = "Mehmet", valid = True)   
    elif 0 <number < 1000:
        return render_template ("result.html", errors= number, developer_name = "Mehmet", validnot = True)
    else:
        return render_template ("index.html", not_valid=True, developer_name = "Mehmet")  
    
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)