from django.db import models, connection


class TypeManager(models.Manager):
    def get_parent(self):
        return self.filter(parent_code="0")
    
    
    def get_sub(self):
        cursor = connection.cursor()
        cursor.execute("""
        SELECT t.type_code,t.type_desc,t.parent_code FROM ss_user_type t WHERE t.parent_code!='0'
           """ )
        _list = []
        for row in cursor.fetchall():
            _r = dict(code=row[0],desc=row[1],parent=row[2])
            _list.append(_r)
        return _list
    



# Create your models here.
class LabelType(models.Model):
    type_id = models.SmallIntegerField(auto_created=True,primary_key=True)
    type_code = models.CharField(max_length=20,null=False,blank=False)
    type_desc = models.CharField(max_length=200,null=False,blank=False)
    parent_code = models.CharField(max_length=20,null=False,blank=False,default="0")

    def __unicode(self):
        return u"%d %s %s" %(self.type_id,self.type_code,self.type_desc)
    
    class Meta:
        db_table = "ss_label_type"
        
    objects = TypeManager()
    