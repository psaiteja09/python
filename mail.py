#sending mail using python

import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com','587')
	s.startls()
	sender='pvgsh09@gmail.com'
	receiver='pvns9112@gmail.com'
	msg="hii saiteja."
	s.login(sender,'ammanana9112')
	s.sendmail(sender,receiver,msg)
except:
	print("some error occured")
else:
	print("msg sent successfully")
	s.quit()