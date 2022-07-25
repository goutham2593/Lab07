from flask import Flask, render_template, request,flash,redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = '@#$%^&*(dftgyujikrty678789'
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if len(password)< 8:  
             flash("No of characters satisfied") 
             return redirect("index.html")
        elif re.search('[0-9]',password) is None:
            flash('No of characters satisfied') 
            return redirect("index.html")
        elif re.search('[A-Z]',password) is None: 
            flash('No of characters satisfied')
            return redirect("index.html")
        else: 
            flash('password correct', category="success")
                           
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)