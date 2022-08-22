from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/testfun')
def test():
    get_name = request.args.get("get_name")           # Asking to pass name as argument.
    mobile_num = request.args.get("mobile")
    mail_id = request.args.get("email")
    return "this is my first function for GET. {} {} {}".format(get_name, mobile_num, mail_id)



"""
This is how I was able to pass value in browser. Using ? and then passing argument
http://127.0.0.1:5002/testfun?get_name=himanshu

In case of more than one argument, then use & in between.
http://127.0.0.1:5002/testfun?get_name=himanshu%20&mobile=813064%20&email=himgos@gmail
"""


# TODO : FETCH SQL DATABASE INTO BROWSER

# @app.route('/fetchy')
# def fetchy():
#     db = request.args.get("db")
#     tab = request.args.get("tab")
#     cursor.execute("SELECT * FROM {}.{}".format(db,tab))
#     return "{}".format(cursor.fetchall())


# TODO: Other Method

# @app.route('/get_data')
# def get_data_from():
#     db = request.args.get('db')
#     tn = request.args.get('tn')
#     try:
#         con = conn.connect(host="localhost", user="root", password="Jaijai1@11", database=db)
#         cur = con.cursor(dictionary=True)
#         cur.execute(f'select * from {tn}')
#         data = cur.fetchall()
#         con.commit()
#         con.close()
#     except Exception as e:
#         return jsonify(str(e))
#     return jsonify(data)

if __name__ == "__main__":
    app.run(port=5002)