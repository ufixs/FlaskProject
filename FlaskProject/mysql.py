from pymysql import Connection
# 连接数据库
conn = Connection(
    host="localhost",
    user="root",
    password="123456",
    database="flaskdb",
    autocommit=True
)


# 验证登录
def login_verify(data):
    cursor = None
    try:
        username = data.get('username')         # 用户名
        password = data.get('password')    # 密码
        cursor = conn.cursor()                  # 建立cursor游标
        sql = "SELECT * FROM admin WHERE a_username=%s"    # sql语句
        cursor.execute(sql, (username,))        # 执行sql语句
        result = cursor.fetchone()              # 获取返回结果
        # print(result)
        if result and (password == result[2]):  # 判断 result是否为空且密码等于返回的结果
            return {                            # 为真返回状态码和name
                'status': 'success',
                'name': result[1]
            }
        else:                                   # 为假返回状态码
            return {
                'status': 'error'
            }
    except Exception as e:
        print("登录异常", e)
    finally:
        if cursor is not None:
            cursor.close()                      # 关闭cursor


# 查询
def select_stu(stu_name):
    cursor = None
    try:
        cursor = conn.cursor()
        if stu_name is not None:
            sql = "select a.c_name,a.c_grade,b.* from class a join student b on a.c_id=b.c_id where b.s_name like %s"
            cursor.execute(sql, ('%' + stu_name + '%',))
        else:
            sql = "select a.c_name,a.c_grade,b.* from class a join student b on a.c_id=b.c_id"
            cursor.execute(sql)
        stu_data = []
        result = cursor.fetchall()
        # print(result)
        for row in result:
            stu_data.append({
                'c_name': row[0],
                'c_grade': row[1],
                "s_id": row[2],
                "c_id": row[3],
                "name": row[4],
                "age": row[5],
                "sex": row[6]
            })
        return stu_data
    except Exception as e:
        print("获取学生表异常", e)
    finally:
        if cursor is not None:
            cursor.close()


# 删除
def delete_stu(stu_id):
    cursor = None
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM student WHERE s_id=%s"
        cursor.execute(sql, (stu_id,))
        # conn.commit()     # 因为我设置了默认提交，可以省略
        return select_stu(None)
    except Exception as e:
        print("删除异常", e)
    finally:
        cursor.close()


# 更新
def edit_stu(data):
    cursor = None
    try:
        cursor = conn.cursor()
        name = data.get('name')
        sex = data.get('sex')
        age = int(data.get('age'))
        c_id = int(data.get('class_id'))
        s_id = int(data.get('s_id'))
        sql = "UPDATE student SET s_name=%s, s_age=%s, s_sex=%s, c_id=%s WHERE s_id=%s"
        cursor.execute(sql, (name, age, sex, c_id, s_id))
        return select_stu(None)
    except Exception as e:
        print("编辑异常", e)
    finally:
        if cursor is not None:
            cursor.close()


# 新增学生
def add_stu(data):
    cursor = None
    try:
        cursor = conn.cursor()
        name = data.get('name')
        sex = data.get('sex')
        age = int(data.get('age'))
        c_id = int(data.get('class_id'))
        sql = "INSERT INTO student(s_name,s_age,s_sex,c_id) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (name, age, sex, c_id))
        result = conn.insert_id()
        if result is not None:
            return 'success'
        else:
            return 'error'
    except Exception as e:
        print("新增异常", e)
    finally:
        if cursor is not None:
            cursor.close()


# 查询班级
def select_class(class_name):
    cursor = None
    try:
        cursor = conn.cursor()
        if class_name is not None:
            sql = "SELECT * FROM class WHERE c_name like %s"
            cursor.execute(sql, ('%'+class_name+'%',))
        else:
            sql = "SELECT * FROM class"
            cursor.execute(sql)
        result = cursor.fetchall()
        # print(result)
        class_data = []
        for row in result:
            class_data.append({
                'class_id': row[0],
                'class_name': row[1],
                'class_grade': row[2]
            })
        # print(class_data)
        return class_data
    except Exception as e:
        print("查询班级异常", e)
    finally:
        if cursor is not None:
            cursor.close()


def add_cla(data):
    cursor = None
    try:
        print("chufale")
        # print(data)
        cursor = conn.cursor()
        name = data.get('name')
        grade = data.get('grade')
        print(name, grade)
        sql = "INSERT INTO class(c_name,c_grade) VALUES (%s,%s)"
        cursor.execute(sql, (name, grade))
        result = conn.insert_id()
        if result is not None and result != " ":
            return 'success'
        else:
            return 'error'
    except Exception as e:
        print("新增班级异常", e)
    finally:
        if cursor is not None:
            cursor.close()
