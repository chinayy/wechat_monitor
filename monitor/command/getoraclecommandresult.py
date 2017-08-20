import re
import os
import subprocess
import cx_Oracle
def getdatafilecreationtime(cursor):
    fp=open('/home/oracle/mysite/monitor/command/oracle_command/getdatafilecreationtime.sql','r')
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

def getanalyzedtime(cursor,table_name):
    fp1='SELECT owner,table_name,num_rows,sample_size,last_analyzed FROM DBA_TABLES WHERE  TABLE_NAME in ('+table_name+') order by table_name'
    s=cursor.execute(fp1)
    row=s.fetchall()
    return row
def getsegmentssize(cursor):
    fp1='SELECT OWNER,segment_name,SEGMENT_TYPE,TABLESPACE_NAME ,BYTES/1024/1024 FROM DBA_SEGMENTS WHERE BYTES/1024/1024>1024 ORDER BY BYTES DESC'
    s=cursor.execute(fp1)
    row=s.fetchall()
    return row
def getprocesstext(cursor,pid):
    fp1='select a.spid,b.sid,c.hash_value,substr(c.sql_text, 0, 40),b.logon_time,b.program from v$process a, v$session b, V$SQL c where a.addr = b.paddr and b.sql_hash_value = c.hash_value and a.spid in ('+pid+')'
    s=cursor.execute(fp1)
    row=s.fetchall()
    return row

