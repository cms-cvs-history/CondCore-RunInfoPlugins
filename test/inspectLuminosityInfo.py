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
    print iov.list()
    print "===payload dump ==="
    payload = inspect.PayLoad(db,'[DB=00000000-0000-0000-0000-000000000000][CNT=LuminosityInfo][CLID=418F38D4-68F7-018F-944F-1B0B230A0B1D][TECH=00000B01][OID=00000004-00000056]')
    print payload.summary()
except Exception, er :
    print er


