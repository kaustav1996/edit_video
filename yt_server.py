from flask import Flask, redirect, url_for, request
from flask import render_template, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import os
from edit import download_and_edit
import sys

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '2020aprilfbvideopost19042020'
class ReusableForm(Form):
	u = TextField('URL: ', validators=[validators.required()])
	f = TextField('From Time (sec): ', validators=[validators.required()])
	t = TextField('To Time (sec): ', validators=[validators.required()])
	c = TextField('Caption (Keep it Short) :', validators=[validators.required()])
    
	@app.route('/',methods = ['POST','GET'])
	def get_video_details():
		form = ReusableForm(request.form)
		if(request.method=='POST'):
			from_time=int(request.form['f'])
			to_time=int(request.form['t'])
			caption=request.form['c']
			url=request.form['u']
			'''if form.validate():
				flash('Added in queue :)')
			else:
            			flash('All the form fields are required. ')'''
			download_and_edit(from_time,to_time,caption,url)
		return render_template('get_video.html', form=form)
			
			


if __name__ == '__main__':
   app.run(debug = False,host='192.168.0.104',port='3000')
