from django.db import models

# Create your models here.
import uuid



class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    user_name = models.CharField(verbose_name= '姓名',max_length= 10)
    user_age = models.PositiveIntegerField(verbose_name= '年龄'  , default= 1)
    user_sex = models.CharField(verbose_name= '性别', max_length= 10, choices= (('male','男'),('female','女')), default= 'male')

    def __str__(self):
        return "当前用户的id为：" + self.user_id.__str__() +", 名字是："+self.user_name + "，性别是："+self.user_sex+"，年龄是："+ self.user_age.__str__()
        #"当前用户的id为：" + self.user_id ++"，年龄是："+ self.user_age


# class Person(models.Model):
#     name = models.CharField(max_length = 30)
#     age = models.IntegerField()
#
#     def __unicode__(self):
#         #在python3中使用def __str__(self)
#         return self.name
#
# class img(models.Model):
#     img = models.ImageField(upload_to = 'img')
#     name = models.CharField(max_length= 20)
#
#     def __str__(self):
#         #在python3中使用def __str__(self)
#         return self.name



