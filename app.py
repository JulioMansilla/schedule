from flask import Flask, render_template, url_for, flash, redirect
import helper
from dict import *
from forms import LoginForm, RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY']='f0902237d035d764f7d9cd235d64d860'
#https://github.com/JulioMansilla/schedule


@app.route('/')
@app.route('/time')
def timeDisplay():
    timeData = helper.time()
    return render_template('time.html', posts=posts, time=timeData)
    #return str(posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    #create an instace of our class like we do in java
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('timeDisplay'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'bob@bob.com' and form.password.data == 'bobster123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__name__':
    app.run(debug=True)
    #$env:FLASK_ENV= "development"
    #export
