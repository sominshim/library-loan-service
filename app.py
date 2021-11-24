from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
userinfo = {'Elice': '1q2w3e4r!!'}

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        try:
            if name in userinfo:
                # 비밀번호 검증 후 일치하는 경우 초기 페이지로 이동하세요.
                if userinfo[name] == password:
                    session['logged_in'] = True
                    return redirect(url_for('home'))
                else:
                    return '비밀번호가 틀립니다.'
            return '아이디가 없습니다.'
        except:
            return 'Dont login'
    else:
        return render_template('login.html')
        
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # username을 key, password를 value로 하여 userinfo 딕셔너리에 추가하세요.
        userinfo[request.form['username']] = request.form['password']
        
        return redirect(url_for('login'))
    else:
        return render_template('register.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)