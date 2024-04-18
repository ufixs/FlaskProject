from flask import Flask, render_template, request, url_for, redirect
from mysql import *
# 实例化
app = Flask(__name__)


# 默认进入登录页
@app.route('/')
def hello_world():
    # 调用render_template方法可以进行网页文件的返回
    return render_template("login.html")


# 进行登录退出验证
@app.route('/login', methods=["POST", "GET"])
def hello_index():
    # 登录
    if request.method == "POST":
        # pymysql.login_verify
        res = login_verify(request.form)
        if res and res['status'] != "error":
            return render_template("index.html", name=res['name'])
        else:
            return render_template("login.html", status=res['status'])
    # 退出
    elif request.method == "GET":
        return render_template('login.html')


@app.route('/student', methods=["GET", "POST"])
def hello_student():
    if request.method == "GET":
        search = request.args.get("search")
        delete = request.args.get("delete")
        if delete is not None:
            # print(delete)
            stu_data = delete_stu(delete)
            return render_template("student_list.html", stu_data=stu_data)
        else:
            stu_data = select_stu(search)
            # print(stu_data)
            return render_template("student_list.html", stu_data=stu_data)

    if request.method == "POST":
        # print(request.form)
        stu_data = edit_stu(request.form)
        return render_template("student_list.html", stu_data=stu_data)


@app.route('/edit_route', methods=["GET"])
def edit_route():
    stu_data = dict()
    for key, value in request.args.items():
        stu_data[key] = value
    # print(stu_data)
    class_data = select_class(None)
    # print(class_data)
    return render_template("stu_edit.html", stu_data=stu_data, class_data=class_data)


@app.route('/add_student', methods=["GET", "POST"])
def add_student():
    if request.method == "GET":
        class_data = select_class(None)
        return render_template("stu_add.html", class_data=class_data)
    if request.method == "POST":
        res = add_stu(request.form)
        # print(res)
        if res == "success":
            return redirect(url_for('hello_student'))
        else:
            pass


@app.route('/class', methods=["GET", "POST"])
def hello_class():
    if request.method == "GET":
        class_data = select_class(request.args.get("search"))
        # print(class_data)
        return render_template("class_list.html", class_data=class_data)


@app.route('/add_class', methods=["GET", "POST"])
def add_class():
    if request.method == "GET":
        return render_template("class_add.html")
    if request.method == "POST":
        print(request.form)
        res = add_cla(request.form)
        if res == "success":
            return redirect(url_for('hello_class'))
        else:
            pass


if __name__ == '__main__':
    app.run(debug=True)
