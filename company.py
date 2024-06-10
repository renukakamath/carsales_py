from flask import *
from database import*

company=Blueprint('company',__name__)


@company.route('/company_home')
def company_home():

	return render_template('company_home.html')


@company.route('/company_managetype',methods=['post','get'])	
def company_managetype():
	data={}
	q="select * from type"
	res=select(q)
	data['typeview']=res

	if "action" in request.args:
		action=request.args['action']
		tid=request.args['tid']

	else:
		action=None

	if action=='delete':
		q="delete from type where type_id='%s' "%(tid)
		delete(q)
		flash('successfully')
		return redirect(url_for('company.company_managetype'))

	if action=='update':
		q="select * from type where type_id='%s'"%(tid)
		res=select(q)
		data['typeup']=res
		


	if "update" in request.form:
		t=request.form['type']
		q="update type set type='%s' where type_id='%s' "%(t,tid)
		update(q)
		flash('successfully')
		return redirect(url_for('company.company_managetype'))


	if "addtype" in request.form:
		t=request.form['type']
		q="insert into type values(null,'%s')"%(t)
		insert(q)

		flash('successfully')
		return redirect(url_for('company.company_managetype'))
	
	return render_template('company_managetype.html',data=data)


@company.route('/company_managevarients',methods=['post','get'])	
def company_managevarients():
	data={}
	q="select * from varients"
	res=select(q)
	data['varientview']=res




	if "action" in request.args:
		action=request.args['action']
		vid=request.args['vid']

	else:
		action=None

	if action=='delete':
		q="delete from varients where variant_id='%s' "%(vid)
		delete(q)
		flash('successfully')
		return redirect(url_for('company.company_managevarients'))

	if action=='update':
		q="select * from varients where variant_id='%s'"%(vid)
		res=select(q)
		data['varientup']=res
		


	if "update" in request.form:
		v=request.form['varient']
		q="update varients set variant='%s' where variant_id='%s' "%(v,vid)
		update(q)
		flash('successfully')
		return redirect(url_for('company.company_managevarients'))


	if "addvarient" in request.form:
		v=request.form['varient']
		q="insert into varients values(null,'%s')"%(v)
		insert(q)

		flash('successfully')
		return redirect(url_for('company.company_managevarients'))
	
	return render_template('company_managevarients.html',data=data)



@company.route('/compant_managevehicle',methods=['post','get'])
def compant_managevehicle():
	data={}
	cid=session['company_id']
	q="SELECT * FROM `vehicle` INNER JOIN `company` USING (`company_id`) INNER JOIN `type` USING (`type_id`) INNER JOIN `varients` USING (`variant_id`) where company_id='%s'"%(cid)
	res=select(q)
	data['vehicleview']=res



	q="select * from type"
	res=select(q)
	data['droptype']=res


	q="select * from varients"
	res=select(q)
	data['dropvariant']=res


	if "action" in request.args:
		action=request.args['action']
		vid=request.args['vid']

	else:
		action=None
		

	if action=='delete':
		q="delete from vehicle where vehicle_id='%s'"%(vid)
		delete(q)
		flash('successfully')
		return redirect(url_for('company.compant_managevehicle'))

	if action=='update':
		q="select * from vehicle inner join type using (type_id) inner join varients using (variant_id) where vehicle_id='%s'"%(vid)
		res=select(q)

		data['vehicleup']=res


	if "update" in request.form:
		vh=request.form['vehicle']
		a=request.form['amount']
		t=request.form['type']
		v=request.form['variant']
		cid=session['company_id']
		q="update vehicle set type_id='%s',variant_id='%s',vehicle='%s',amount='%s' where vehicle_id='%s'"%(t,v,vh,a,vid)
		update(q)
		flash('successfully')
		return redirect(url_for('company.compant_managevehicle'))


	if "add" in request.form:
		vh=request.form['vehicle']
		a=request.form['amount']
		t=request.form['type']
		v=request.form['variant']
		cid=session['company_id']
		q="insert into vehicle values(null,'%s','%s','%s','%s','%s')"%(cid,t,v,vh,a)
		insert(q)
		flash('successfully')
		return redirect(url_for('company.compant_managevehicle'))
	return render_template('compant_managevehicle.html',data=data)

@company.route('/company_managefeatures',methods=['post','get'])	
def company_managefeatures():
	data={}
	vid=request.args['vid']
	q="select * from feature inner join vehicle using (vehicle_id) where vehicle_id='%s'"%(vid)
	res=select(q)
	data['fea']=res

	if "action" in request.args:
		action=request.args['action']
		fid=request.args['fid']
		vid=request.args['vid']

	else:
		action=None

	if action=='delete':
		q="delete from feature where feature_id='%s' "%(fid)
		delete(q)
		flash('successfully')
		return redirect(url_for('company.company_managefeatures',vid=vid))

	if action=='update':
		q="select * from feature inner join vehicle using (vehicle_id) where feature_id='%s'"%(fid)
		res=select(q)
		data['prod']=res
		


	if "update" in request.form:
		f=request.form['feature']
		vid=request.args['vid']

		q="update feature set features='%s' where feature_id='%s' "%(f,fid)
		update(q)
		flash('successfully')
		return redirect(url_for('company.company_managefeatures',vid=vid))


	if "addfeature" in request.form:
		f=request.form['feature']
		vid=request.args['vid']
		q="insert into feature values(null,'%s','%s')"%(vid,f)
		insert(q)

		flash('successfully')
		return redirect(url_for('company.company_managefeatures',vid=vid))
	
	return render_template('company_managefeatures.html',data=data,vid=vid)

@company.route('/company_managespecification',methods=['post','get'])	
def company_managespecification():
	data={}
	vid=request.args['vid']
	q="select * from sepecification inner join vehicle using (vehicle_id) where vehicle_id='%s'"%(vid)
	res=select(q)
	data['sep']=res

	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']
		vid=request.args['vid']

	else:
		action=None

	if action=='delete':
		q="delete from sepecification where sepicification_id='%s' "%(sid)
		delete(q)
		flash('successfully')
		return redirect(url_for('company.company_managespecification',vid=vid))

	if action=='update':
		q="select * from sepecification inner join vehicle using (vehicle_id) where sepicification_id='%s'"%(sid)
		res=select(q)
		data['specificationup']=res
		


	if "update" in request.form:
		s=request.form['specification']
		vid=request.args['vid']

		q="update sepecification set specification='%s' where sepicification_id='%s' "%(s,sid)
		update(q)
		flash('successfully')
		return redirect(url_for('company.company_managespecification',vid=vid))


	if "addspecification" in request.form:
		s=request.form['specification']
		vid=request.args['vid']
		q="insert into sepecification values(null,'%s','%s')"%(vid,s)
		insert(q)

		flash('successfully')
		return redirect(url_for('company.company_managespecification',vid=vid))
	
	return render_template('company_managespecification.html',data=data,vid=vid)

@company.route('/company_viewcarbookings')
def company_viewcarbookings():
	data={}
	q="SELECT * FROM `carbooking` INNER JOIN `vehicle` USING (`vehicle_id`) INNER JOIN `customer` USING (`customer_id`)"
	res=select(q)
	data['carbook']=res


	return render_template('company_viewcarbookings.html',data=data)

@company.route('/company_viewtestbooking')
def company_viewtestbooking():
	data={}
	q="SELECT * FROM  `testbooking` INNER JOIN `vehicle` USING (vehicle_id) INNER JOIN `customer` USING (customer_id)"
	res=select(q)
	data['test']=res


	return render_template('company_viewtestbooking.html',data=data)


@company.route('/company_managepart',methods=['post','get'])	
def company_managepart():
	data={}
	cid=session['company_id']
	q="select * from parts where company_id='%s'"%(cid)
	res=select(q)
	data['parts']=res




	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']

	else:
		action=None

	if action=='delete':
		q="delete from parts where parts_id='%s' "%(pid)
		delete(q)
		flash('successfully')
		return redirect(url_for('company.company_managepart'))

	if action=='update':
		q="select * from parts where parts_id='%s'"%(pid)
		res=select(q)
		data['partsup']=res
		


	if "update" in request.form:
		p=request.form['parts']
		f=request.form['features']
		d=request.form['details']
		a=request.form['amount']
		q="update parts set parts='%s' ,features='%s',details='%s',amount='%s' where parts_id='%s' "%(p,f,d,a,pid)
		update(q)
		flash('successfully')
		return redirect(url_for('company.company_managepart'))


	if "add" in request.form:
		cid=session['company_id']
		p=request.form['parts']
		f=request.form['features']
		d=request.form['details']
		a=request.form['amount']
		q="insert into parts values(null,'%s','%s','%s','%s','%s')"%(cid,p,f,d,a)
		insert(q)

		flash('successfully')
		return redirect(url_for('company.company_managepart'))
	
	return render_template('company_managepart.html',data=data)

@company.route('/company_viewpartbooking')
def company_viewpartbooking():
	data={}
	q="SELECT * FROM `partbookdetail` INNER JOIN `partbook` USING(`partbook_id`) INNER JOIN `parts` USING (`parts_id`) INNER JOIN `customer` USING (`customer_id`)"
	res=select(q)
	data['partbook']=res


	return render_template('company_viewpartbooking.html',data=data)


@company.route('/company_viewenquiry')
def company_viewenquiry():
	data={}
	cid=session['company_id']
	q="SELECT * FROM `enquiry` INNER JOIN `customer` USING (`customer_id`) INNER JOIN `company` USING (`company_id`) where company_id='%s'"%(cid)
	res=select(q)
	data['enqu']=res


	return render_template('company_viewenquiry.html',data=data)

@company.route('/company_sendreply',methods=['post','get'])	
def company_sendreply():
	if "sendreply" in request.form:
		eid=request.args['eid']
		r=request.form['Reply']
		q="update enquiry set reply='%s' where enquiry_id='%s'"%(r,eid)
		update(q)
		flash('successfully')
		return redirect(url_for('company.company_viewenquiry'))
	return render_template('company_sendreply.html')


@company.route('/company_viewpayment')
def company_viewpayment():
	data={}
	pid=request.args['pid']
	
	q="SELECT * FROM `payment`inner join partbook on payment.book_id=partbook.partbook_id where partbook_id='%s'"%(pid)
	res=select(q)
	data['pay']=res


	return render_template('company_viewpayment.html',data=data)

@company.route('/company_viewloan')
def company_viewloan():
	data={}
	
	
	q="select * from loan inner join customer using (customer_id)"
	res=select(q)
	data['loan']=res


	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:
		action=None

	if action=='accept':
		q="update loan set status='Accept' where  loan_id='%s'"%(lid)
		update(q)
		flash('successfully')

		return redirect(url_for('company.company_viewloan'))

	if action=='reject':
		q="update loan set status='reject' where loan_id='%s'"%(lid)
		update(q)
		flash('successfully')

		return redirect(url_for('company.company_viewloan'))
		





	return render_template('company_viewloan.html',data=data)
