from flask import Flask, url_for, render_template, request

app=Flask(__name__)

def romenconcert(num):
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    num=int(num)
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman

@app.route("/",methods=["GET"])
def main():
    return render_template("index.html", developer_name="E2127 Murat", not_valid=False)
@app.route("/",methods=["POST"])
def index():
    number_decimal = request.form.get('number')
    if not number_decimal.isdigit():
        return render_template("index.html", developer_name="E2127 Murat", not_valid=True)
    number_decimal =int(number_decimal)
    if not 0<number_decimal<4000:
        return render_template("index.html", developer_name="E2127 Murat", not_valid=True)
        
    number_roman = romenconcert(number_decimal) 
    return render_template("result.html", number_decimal = number_decimal, number_roman=number_roman, developer_name="E2127 Murat")
    
if __name__=="__main__":
    app.run(debug="True")
    #app.run(host="0.0.0.0/0", port=80)