from flask import *
from database import*


public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('home.html')

@public.route('/company_registration',methods=['post','get'])	
def company_registration():
	if "company" in request.form:
		c=request.form['fname']
		l=request.form['licence']
		
		ph=request.form['phone']
		e=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:

			flash('already exist')

		else:
			
			q="insert into login values(null,'%s','%s','pending')"%(u,pa)
			id=insert(q)
			q="insert into company values(null,'%s','%s','%s','%s','%s')"%(id,c,l,ph,e)
			insert(q)
			flash('successfully')
			return redirect(url_for('public.company_registration'))

	return render_template('company_registration.html')

@public.route('/user_registration',methods=['post','get'])	
def user_registration():
	if "user" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		p=request.form['place']
		
		ph=request.form['phone']
		e=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:

			flash('already exist')

		else:
			
			q="insert into login values(null,'%s','%s','customer')"%(u,pa)
			id=insert(q)
			q="insert into customer values(null,'%s','%s','%s','%s','%s','%s')"%(id,f,l,p,ph,e)
			insert(q)
			flash('successfully')
			return redirect(url_for('public.user_registration'))

	return render_template('user_registration.html')


@public.route('/login',methods=['post','get'])	
def login():
	if "login" in request.form:
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']
			lid=session['login_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.admin_home'))

			elif res[0]['usertype']=="customer":
				q="select * from customer where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['customer_id']=res[0]['customer_id']
					uid=session['customer_id']
				return redirect(url_for('user.user_home'))

			elif res[0]['usertype']=="company":
				q="select * from company where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['company_id']=res[0]['company_id']
					cid=session['company_id']



				return redirect(url_for('company.company_home'))


		else:
			flash('invalid username and password')

	return render_template('login.html')