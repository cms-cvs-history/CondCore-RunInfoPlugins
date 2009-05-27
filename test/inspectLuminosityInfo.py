import os,sys, DLFCN
sys.setdlopenflags(DLFCN.RTLD_GLOBAL+DLFCN.RTLD_LAZY)

from pluginCondDBPyInterface import *
a = FWIncantation()
rdbms = RDBMS()
dbName =  "sqlite_file:offlinelumi.db"

from CondCore.Utilities import iovInspector as inspect

db = rdbms.getDB(dbName)
tags = db.allTags()

tag = 'lumitest'

try :
    iov = inspect.Iov(db,tag)
    print "===iov list ==="
    iovlist=iov.list()
    print iovlist
    
    print "===payload dump ==="
    for p in iovlist:
        payload=inspect.PayLoad(db,p[0])
        print payload.summary()
except Exception, er :
    print er


