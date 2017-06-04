from django.db import models, connection
from tool import util
from tool.logs import getAppLog
from tool.webapp import AppError


# Create your models here.
_log = getAppLog()

class InvitorManager(models.Manager):
    def getCurrentInvitor(self,publishe_id):
        current_time = util.getDayFromZeroTime()
        sql = """SELECT it.* FROM ss_invite_task it WHERE it.project_publisher=%s AND it.project_time>%d """ % (publishe_id,current_time)
        cursor = connection.cursor()
        cursor.execute(sql)
        _result = []
        for row in cursor.fetchall():
            _rs = dict(row)
            _result.append(_rs)
            
        return _result
    
    def countInvitor(self,publishe_id):
        current_time = util.getDayFromZeroTime()
        sql = """SELECT COUNT(0) FROM ss_invite_task it WHERE it.project_publisher=%s AND it.project_time>%d """ % (publishe_id,current_time)
        cursor = connection.cursor()
        cursor.execute(sql)
        _num = 0
        try:
            _num = cursor.fetchall()[0][0]
        except AppError,e:
            print "InvitorManager-->countInvitor,"+e
            _num = 0
        return _num
    
    def getInvitorTask(self,user_id,invitor_id):
        sql = """ SELECT it.* FROM ss_invite_task it WHERE it.project_id=%d AND it.project_publisher=%d """ % (invitor_id,user_id)
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()[0]
        
        
class InvitorTask(models.Model):
    project_id = models.PositiveIntegerField(auto_created=True,primary_key=True)
    project_publisher = models.PositiveIntegerField()
    project_invitors = models.CharField(max_length=50)
    project_context = models.TextField()
    project_time = models.FloatField(default=0.00)
    
    objects = models.Manager()
    invitor_manager = InvitorManager()
    
    class Meta:
        db_table = "ss_invite_project"
        
        
    