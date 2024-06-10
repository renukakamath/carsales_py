from flask import *
from database import*

user=Blueprint('user',__name__)


@user.route('/user_home')
def user_home():

	return render_template('user_home.html')

@user.route('/user_viewvehicle',methods=['post','get'])
def user_viewvehicle():
	data={}

	if "Searchhere" in request.form:
		s=request.form['search']+'%'


		q="SELECT * FROM `vehicle` INNER JOIN `type` USING (`type_id`) INNER JOIN `varients` USING (`variant_id`) INNER JOIN `sepecification` USING (`vehicle_id`) INNER JOIN `feature` USING (vehicle_id) INNER JOIN company USING (company_id) where company like '%s' or features like '%s' or specification like '%s' or vehicle like '%s'"%(s,s,s,s)
		res=select(q)
		data['vehicle']=res


	else:
		q="SELECT * FROM `vehicle` INNER JOIN `type` USING (`type_id`) INNER JOIN `varients` USING (`variant_id`) INNER JOIN `sepecification` USING (`vehicle_id`) INNER JOIN `feature` USING (vehicle_id) INNER JOIN company USING (company_id)"
		res=select(q)
		data['vehicle']=res


	return render_template('user_viewvehicle.html',data=data)


@user.route('/user_booktestdrive',methods=['post','get'])
def user_booktestdrive():
	data={}
	from datetime import date

	today = date.today()
	print("Today's date:", today)
		
	if "book" in request.form:
		date=request.form['date']
		vid=request.args['vid']
		uid=session['customer_id']
		q="insert into testbooking values(null,'%s','%s',curdate(),'%s','booked')"%(uid,vid,date)
		insert(q)
		flash('successfully')
		return  redirect(url_for('user.user_viewvehicle'))

		return render_template('user_booktestdrive.html',today=today)

@user.route('/user_bookcar',methods=['post','get'])
def user_bookcar():
	data={}

	amt=request.args['amt']
	data['amou']=amt


	
	
	if "bookcar" in request.form:
		date=request.form['date']
		amount=request.form['amount']

		vid=request.args['vid']
		uid=session['customer_id']
		q="insert into carbooking values(null,'%s','%s','%s','%s','pending')"%(vid,uid,date,amount)
		insert(q)
		flash('successfully')
		return  redirect(url_for('user.user_viewvehicle'))


		
	

	return render_template('user_bookcar.html',data=data,amt=amt)

@user.route('/user_testdrive',methods=['post','get'])
def user_testdrive():
	data={}
	uid=session['customer_id']
	q="SELECT * FROM  `testbooking` INNER JOIN `vehicle` USING (vehicle_id) INNER JOIN `customer` USING (customer_id) where customer_id='%s'"%(uid)
	res=select(q)
	data['test']=res

	return render_template('user_testdrive.html',data=data)

@user.route('/user_viewcarbook',methods=['post','get'])
def user_viewcarbook():
	data={}
	uid=session['customer_id']
	q="SELECT * FROM `carbooking` INNER JOIN `vehicle` USING (`vehicle_id`) INNER JOIN `customer` USING (`customer_id`) where customer_id='%s'"%(uid)
	res=select(q)
	data['carbook']=res
	
	return render_template('user_viewcarbook.html',data=data)

@user.route('/usermakepayment',methods=['post','get'])
def usermakepayment():
	data={}
	amt=request.args['amt']
	data['amt']=amt
	if "payment" in request.form:

		amt=request.args['amt']
		bid=request.args['bid']
		q="insert into payment values(null,'%s','%s',curdate())"%(bid,amt)
		insert(q)
		q="update set carbooking set status='Paid' where carbooking_id='%s'"%(bid)
		update(q)
		flash('successfully')
		return redirect(url_for('user.user_viewcarbook'))


	
	return render_template('usermakepayment.html',data=data)

@user.route('/user_viewparts',methods=['post','get'])
def user_viewparts():
	data={}

	q="SELECT * FROM `parts` INNER JOIN `company` USING (`company_id`)"
	res=select(q)
	data['parts']=res
	
	return render_template('user_viewparts.html',data=data)

@user.route('/user_addtocart',methods=['post','get'])
def user_addtocart():
	data={}
	amt=request.args['amt']
	data['amt']=amt

	parts=request.args['parts']
	data['parts']=parts



	q="select * from vehicle"
	res=select(q)
	data['vehicle']=res



	if "add" in request.form:
		pid=request.args['pid']
		qua=request.form['qua']
		amo=request.form['amo']
		total=request.form['total']
		uid=session['customer_id']
		vehicle=request.form['vehicle']

		q="select * from partbook where customer_id='%s' and status='pending'"%(uid)
		res=select(q)
		if res:
			pbid=res[0]['partbook_id']
		else:
			q="insert into partbook values(null,'%s','0',curdate(),'pending')"%(uid)
			pbid=insert(q)
		q="select * from partbookdetail where parts_id='%s' and partbook_id='%s'"%(pid,pbid)
		res=select(q)
		if res:
			pdid=res[0]['partdetail_id']

			q="update partbookdetail set amount=amount+'%s' , quantity=quantity+'%s' where partdetail_id='%s'"%(total,qua,pdid)
			update(q)

		else:
			
			q="insert into partbookdetail values(null,'%s','%s','%s','%s','%s')"%(pbid,pid,vehicle,total,qua)
			insert(q)

		q="update partbook set total=total+'%s' where partbook_id='%s'"%(total,pbid)
		update(q)
		return redirect(url_for('user.user_viewcarts'))


	return render_template('user_addtocart.html',data=data)


@user.route('/user_viewcarts',methods=['post','get'])
def user_viewcarts():
	data={}
	uid=session['customer_id']
	q="SELECT * FROM `partbookdetail` INNER JOIN `partbook` USING(`partbook_id`) INNER JOIN `parts` USING (`parts_id`) INNER JOIN `customer` USING (`customer_id`) where customer_id='%s'"%(uid)
	res=select(q)
	data['partbook']=res
	
	return render_template('user_viewcarts.html',data=data)

@user.route('/user_makepartpayment',methods=['post','get'])
def user_makepartpayment():
	data={}
	# amt=request.args['amt']
	# data['amt']=amt
	if "payment" in request.form:

		amt=request.form['amo']
		bid=request.args['bid']
		q="insert into payment values(null,'%s','%s',curdate())"%(bid,amt)
		insert(q)
		q="update partbook set status='halfPaid' where partbook_id='%s'"%(bid)
		update(q)
		flash('successfully')
		return redirect(url_for('user.user_viewcarbook'))

	return render_template('user_makepartpayment.html',data=data)


@user.route('/payment',methods=['post','get'])
def payment():
	data={}
	amt=request.args['amt']
	data['amt']=amt
	if "payment" in request.form:

		amo=request.form['amo']
		bid=request.args['bid']

		q="select * from payment where book_id='%s'"%(bid)
		res=select(q)
		if res:
			
			# q="insert into payment values(null,'%s','%s',curdate())"%(bid,amo)
			# insert(q)
			q="update payment set amount='%s' where book_id='%s'"%(amo,bid)
			update(q)
			q="update partbook set status='Paid' where partbook_id='%s'"%(bid)
			update(q)
			flash('successfully')
			return redirect(url_for('user.user_viewcarbook'))

	return render_template('payment.html',data=data)


@user.route('/user_sendenquiry' ,methods=['post','get'])	
def user_sendenquiry():

	data={}
	uid=session['customer_id']
	q="select * from enquiry inner join customer using (customer_id) where customer_id='%s'"%(uid)
	res=select(q)
	data['comp']=res

	q="select * from company"
	res=select(q)
	data['compdrop']=res

	if "enquiry" in request.form:
		comp=request.form['comp']
		uid=session['customer_id']
		emq=request.form['emq']
		q="insert into enquiry values(null,'%s','%s','%s',curdate(),'pending')"%(uid,comp,emq)
		insert(q)
		flash('successfully')
		return redirect(url_for('user.user_sendenquiry'))

	return render_template('user_sendenquiry.html',data=data)


@user.route('/user_sendcomplaint' ,methods=['post','get'])	
def user_sendcomplaint():

	data={}
	uid=session['customer_id']
	q="select * from complaint inner join customer using (customer_id) where customer_id='%s'"%(uid)
	res=select(q)
	data['comp']=res

	if "complaint" in request.form:
		uid=session['customer_id']
		c=request.form['comp']
		q="insert into complaint values(null,'%s','%s','pending',now())"%(uid,c)
		insert(q)
		flash('successfully')
		return redirect(url_for('user.user_sendcomplaint'))

	return render_template('user_sendcomplaint.html',data=data)


@user.route('/user_addloan' ,methods=['post','get'])	
def user_addloan():

	data={}
	uid=session['customer_id']
	q="select * from loan inner join customer using (customer_id) where customer_id='%s'"%(uid)
	res=select(q)
	data['comp']=res

	if "enquiry" in request.form:
		uid=session['customer_id']
		a=request.form['amt']
		d=request.form['details']
		q="insert into loan values(null,'%s','%s','%s','pending')"%(uid,d,a)
		insert(q)
		flash('successfully')
		return redirect(url_for('user.user_addloan'))

	return render_template('user_addloan.html',data=data)







