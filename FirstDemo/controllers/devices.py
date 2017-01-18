# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index(): 
    devices = db(db.device).select()
    message= "List Method"    
    return locals()

#@auth.requires_membership('Device Configuration')
def edit():
    form = SQLFORM(db.device).process()
    form2=SQLFORM.factory(Field('deviceName')).process()
    deviceId = request.args[0]
    return locals()
