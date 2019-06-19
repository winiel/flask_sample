from flask import render_template

from app import app

@app.route('/')
def home():
    print("flask_sample");
    return render_template('home.html')
# def hello_world():
#     return 'Hello World!'



@app.route('/test')
def test():
    # dbUtil = DbUtil();
    # dbUtil = DbUtil();
    #
    # sql = "SELECT * FROM abitree.tbl_test";
    # res = dbUtil.exeQuery(sql, None );
    # print(res);
    return "hello12";




@app.route('/mail', methods=['post'])
def PostMail():

    # pushMail = PushMail();
    # pushMail.push(request);

    return "post_mail22";

