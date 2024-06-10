from flask import * 
from database import*



admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():

	return render_template('admin_home.html')


@admin.route('/admin_viewcompany')
def admin_viewcompany():
	data={}
	q="select * from company inner join login using (login_id)"
	res=select(q)
	data['comp']=res


	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=='accept':
		q="update login set usertype='company' where login_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewcompany'))

	if action=='reject':
		q="update login set usertype='block' where login_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewcompany'))

	return render_template('admin_viewcompany.html',data=data)

@admin.route('/admin_viewcustomer')
def admin_viewcustomer():
	data={}
	q="select * from customer inner join login using (login_id)"
	res=select(q)
	data['cust']=res


	return render_template('admin_viewcustomer.html',data=data)


@admin.route('/admin_viewcarbooking')
def admin_viewcarbooking():
	data={}
	q="SELECT * FROM `carbooking` INNER JOIN `vehicle` USING (`vehicle_id`) INNER JOIN `customer` USING (`customer_id`)"
	res=select(q)
	data['carbook']=res


	return render_template('admin_viewcarbooking.html',data=data)

@admin.route('/admin_testdrive')
def admin_testdrive():
	data={}
	q="SELECT * FROM  `testbooking` INNER JOIN `vehicle` USING (vehicle_id) INNER JOIN `customer` USING (customer_id)"
	res=select(q)
	data['test']=res


	return render_template('admin_testdrive.html',data=data)


@admin.route('/admin_viewpartsbooking')
def admin_viewpartsbooking():
	data={}
	q="SELECT * FROM `partbookdetail` INNER JOIN `partbook` USING(`partbook_id`) INNER JOIN `parts` USING (`parts_id`) INNER JOIN `customer` USING (`customer_id`)"
	res=select(q)
	data['partbook']=res


	return render_template('admin_viewpartsbooking.html',data=data)

@admin.route('/admin_viewcomplaint')
def admin_viewcomplaint():
	data={}
	q="select * from complaint inner join customer using (customer_id)"
	res=select(q)
	data['compl']=res
	return render_template('admin_viewcomplaint.html',data=data)

@admin.route('/admin_sendreply',methods=['post','get'])	
def admin_sendreply():
	if "sendreply" in request.form:
		cid=request.args['cid']
		r=request.form['Reply']
		q="update complaint set reply='%s' where complaint_id='%s'"%(r,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewcomplaint'))
	return render_template('admin_sendreply.html')
