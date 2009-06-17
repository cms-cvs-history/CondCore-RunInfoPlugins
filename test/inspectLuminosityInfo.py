import os,sys, DLFCN
sys.setdlopenflags(DLFCN.RTLD_GLOBAL+DLFCN.RTLD_LAZY)

from pluginCondDBPyInterface import *

a = FWIncantation()
rdbms = RDBMS()
dbName =  "sqlite_file:offlinelumi.db"
print 1
from CondCore.Utilities import iovInspector as inspect
print 3
db = rdbms.getDB(dbName)
print 4
tags = db.allTags()
print 'all tags ',tags
tag = 'lumitest'

try :
    iov = inspect.Iov(db,tag)
    print "===iov list ==="
    iovlist=iov.list()
    print iovlist
    print "===iov summaries ==="
    print iov.summaries()
    print "===payload dump lumisec 1==="
    payloadstrdump=iov.payloadSummaries()
    print payloadstrdump[0]
    for p in iovlist:
        payload=inspect.PayLoad(db,p[0])
        print payload.summary()
    print "===print lumi vs time values==="
    print inspect.extractorWhat(db,tag)
    #print 'trend lumivalue vs. lumiid'
    what={}
    print iov.trend(what)
    print "===user comment===="
    print iov.comment()
    print "===iov revision==="
    print iov.revision()
    print "===payload container name==="
    print iov.payloadContainerName()
except Exception, er :
    print er

print "-------------------------------------------------------"
tag2 = 'hltscalertest'

try :
    iov2 = inspect.Iov(db,tag2)
    print "===iov list ==="
    iov2list=iov2.list()
    print iov2list
    print "===payload 2 dump lumisec 1==="
    payloadstrdump2=iov2.payloadSummaries()
    print payloadstrdump2[0]
    for p in iov2list:
        payload=inspect.PayLoad(db,p[0])
        print payload.summary()
    #print 'trend lumivalue vs. lumiid'
    print iov2.payloadContainerName()
except Exception, er :
    print er
