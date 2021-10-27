from flask import Flask, render_template, request,redirect,url_for,flash,jsonify
import my_sql
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "hello"



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add",methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        title = request.form.get("title")
        username = request.form.get("username")
        email = request.form.get("email")
        pwd = request.form.get("pwd")
        date = datetime.today()
        date = str(date)
        date = pretify_date(date)
        if title and username and email and pwd:
            my_sql.add_to_table(title,username,email,pwd,date)
            flash("You added data seccessfully!!")
            return redirect(url_for("passwords"))
        else:
            flash("You have to add all inputs!!!")
            return redirect(url_for("add"))

@app.route("/passwords")
def passwords():
    return render_template("passwords.html",data = my_sql.get_data())


@app.route("/delete/<int:id_>")
def delete(id_):
    test_data = my_sql.get_data_where(id_)
    if not test_data:
            return render_template("error.html")
    my_sql.delet_from_table(id_)
    flash("Deleted password seccessfully!")
    return redirect(url_for("passwords"))

@app.route("/edit/<int:id_>",methods = ["GET","POST"])
def edit(id_):
    if request.method == "GET":
        test_data = my_sql.get_data_where(id_)
        if not test_data:
            return render_template("error.html")
        return render_template("edit.html",data = my_sql.get_data_where(id_))
    else:
        title = request.form.get("title")
        username = request.form.get("username")
        email = request.form.get("email")
        pwd = request.form.get("pwd")
        date = datetime.today()
        date = str(date)
        date = pretify_date(date)
        if title and username and email and pwd:
            my_sql.edit_from_table(title, username, email, pwd, date, id_)
            flash("password edited seccessfully!")
            return redirect(url_for("passwords"))
        else:
            flash("You have to add all inputs!!!")
            return redirect(url_for("edit",id_=id_))
        

def generate_password(length=10):
    Cletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Sletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    Numbers = "1234567890"

    # create alphanumerical from string constants
    printable = f'{Cletters}{Numbers}{Sletters}'

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password and convert to string
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password

def pretify_date(date):
    day,clock = date.split(" ")
    day = day.replace("-","/")
    wanted_time, milliseconds = clock.split(".")
    hh,mm,ss = wanted_time.split(":")
    hh = int(hh)
    print(hh)
    if(hh > 12):
        hh = hh - 12
    elif hh == 0:
        hh = "12"
    wanted_time = str(hh)+":"+mm+":"+ss
    final_time ="|"+day + "|    |" + wanted_time+"|"
    return final_time

@app.route("/generate/<int:length>")
def generate(length):
    password = generate_password(length)
    return jsonify({"pwd":password})
if __name__ == "__main__":
    my_sql.create_table()
    app.run(debug=True)







