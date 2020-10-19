from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def convert_miliseconds(ms):
    result = ""
    lst = [(ms // 3600000, ' hour/s '), ((ms // 60000) % 60, ' minute/s '), ((ms // 1000) % 60, ' second/s ')]
    for t, text in lst:
        result += f"{t and (str(t) + text) or ''}"
    return f"{result or ('just ' + str(ms) + ' miliseconds') }"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        number = request.form["number"]
        if number.isdigit():
            return render_template("result.html", milliseconds = number, result = convert_miliseconds(int(number)), developer_name = "Baris YURTTAV") 
        else:    
            return render_template("index.html", not_valid = True, developer_name = "Group_Kilo")                   
    else:
        return render_template("index.html", not_valid = False, developer_name = "Group_Kilo")

if __name__ == "__main__":
    #app.run(debug = True)
    app.run(host='0.0.0.0', port=80)