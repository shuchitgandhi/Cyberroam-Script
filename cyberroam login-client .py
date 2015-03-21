import sys
import mechanize
import time
import datetime

TIME_BETWEEN_LOGIN=((2*60*60)-(5*60))
USERNAME='your_username'
PASSWORD='your_password'


br=mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
#print 'Made browser'

while True:
    response=br.open('https://10.100.56.55:8090/httpclient.html')
    #    print 'Opened cyberoam'

    form_exists=False
    for form in br.forms():
        if form.name=='frmHTTPClientLogin':
            form_exists=True
    if not form_exists:    
        sys.exit('Error!! Form not found')

    br.select_form(name='frmHTTPClientLogin')
    button=br.form.find_control('btnSubmit')
    button.readonly=False
    if button.readonly:
        sys.exit("Error! Couldn't change readonly setting of button")

    br.select_form(name='frmHTTPClientLogin')
    button=br.form.find_control('btnSubmit')
    button.readonly=False
    #    print 'Button readied'
    if button.value!='Login':
        br.submit()
        print 'Logged out'
    br['username']=USERNAME
    br['password']=PASSWORD
    br.submit()
    print 'Logged in'
    print 'Submitted:', datetime.datetime.now().__str__()
    response=br.response().read()
    br._factory.is_html = True
    #    print br.forms()
    #print response
    #br.submit()
    time.sleep(TIME_BETWEEN_LOGIN)
    #break


