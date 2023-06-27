from flask import Flask
from flask import Blueprint, render_template, redirect, url_for,flash
app = Flask(__name__)

@app.route("/")
def att():
    with open('attendance.csv', 'r+', encoding="utf8") as f:
        myDataList = f.readlines()
    my_dict = {}

    for item in myDataList:
        if item != '\n':
            name, timestamp = item.strip().split(',')
            my_dict[name] = timestamp
    # print(myDataList)
    return render_template("att.html",attendance_data=my_dict)
if __name__ == '__main__':
    app.run(debug=True)