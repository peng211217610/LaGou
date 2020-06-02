#!/usr/bin/python3
# -*- coding:utf-8 -*-
#备注
remark = '''面向对象编程'''

#变量


#引入相关包


class Animal(object):

    def __init__(self,name,color,age,sex):
        self.name=name
        self.color=color
        self.age=age
        self.sex=sex

    def huijiao(self):
        print('jiao')

    def huipao(self):
        print('pao')




class Cat(Animal):

    def __init__(self,name,color,age,sex,hair='short'):
        Animal.__init__(self,name,color,age,sex)
        self.hair=hair

    def huizhuolaoshu(self):
        print('zhuolaoshu')


    def huijiao(self):
        print('maomaojiao')


class Dog(Animal):

    def __init__(self,name,color,age,sex,hair='long'):
        Animal.__init__(self,name,color,age,sex)
        self.hair = hair

    def huikanjia(self):
        print('huikanjia')

    def huijiao(self):
        print('wangwangjiao')


#猫猫实例
cat=Cat('xiaomao','black',5,'male')
catchmouse=cat.huizhuolaoshu()
print(cat.name,cat.color,cat.age,cat.sex,cat.hair,cat.huizhuolaoshu())





if __name__=="__main__":
    pass