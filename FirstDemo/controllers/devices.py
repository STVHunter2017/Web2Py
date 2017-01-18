# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index(): 
    devices = db(db.device).select()
    message= "List Method"    
    return locals()

#@auth.requires_membership('Device Configuration')
def edit():       
    device = db.device(db.device.id == request.args[0])
    return locals()

def add():
    form = SQLFORM(db.device).process()
    return locals()
