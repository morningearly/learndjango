from django.db import models

# Create your models here.

# 定义模型类需要继承models.Models
# 自动添加主键 id

class BookInfo(models.Model):
    # 字段类型 字符
    name = models.CharField(max_length=10)
    # 将模型类以字符串的方式输出
    def __str__(self):
        return self.name
    
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    # 布尔
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name