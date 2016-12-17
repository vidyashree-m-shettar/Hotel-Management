from __future__ import unicode_literals


from django.db import models


class Room(models.Model):
    #room_id=models.IntegerField(room_id,on_delete=models.CASCADE)
    type=models.CharField(max_length=200)
    cost=models.IntegerField()
    status=models.CharField(max_length=200)

    def __str__(self):
        return self.type



class Menu(models.Model):
    #menu_id=models.IntegerField(menu_id,on_delete=models.CASCADE)
    category=models.CharField(max_length=200)
    #type=models.CharField(max_length=200)

    def __str__(self):
        return self.category
        #print self.type

class Food(models.Model):
    # food_id=models.IntegerField(food_id,on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    cost = models.IntegerField()

    def __str__(self):
            return self.name

#class NorthIndianVeg(models.Model):
    #food_id=models.IntegerField(food_id,on_delete=models.CASCADE)
    #menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
    #name=models.CharField(max_length=200)
    #cost=models.IntegerField()

#    def __str__(self):
    #   return self.name

#class South_Indian_Veg(models.Model):
    #food_id=models.IntegerField(food_id,on_delete=models.CASCADE)
    #menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
    #name=models.CharField(max_length=200)
    #cost=models.IntegerField()

    #def __str__(self):
        #return self.name

#class NorthIndianNonveg(models.Model):
    #food_id=NorthIndianNonvegmodels.IntegerField(food_id,on_delete=models.CASCADE)
    #menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
    #name=models.CharField(max_length=200)
    #cost=models.IntegerField()

    #def __str__(self):
        #return self.name

#class South_Indian_Nonveg(models.Model):
    #food_id=models.IntegerField(food_id,on_delete=models.CASCADE)
    #menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
    #name=models.CharField(max_length=200)
    #cost=models.IntegerField()

    #def __str__(self):
     #   return self.name

class Sweet(models.Model):
    #food_id=models.IntegerField(food_id,on_delete=models.CASCADE)
    menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    cost=models.IntegerField()

    def __str__(self):
        return self.name

class Chat(models.Model):
    #food_id=models.IntegerField(food_id,on_delete=models.CASCADE)
    menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    cost=models.IntegerField()

    def __str__(self):
        return self.name

class Bevage(models.Model):
    #food_id=models.IntegerField(food_id,on_delete=models.CASCADE)
    menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    cost=models.IntegerField()

    def __str__(self):
        return self.name

#class Contact(models.Model):
    #name=models.CharField(max_length=200)
    #contactno=models.IntegerField()
    #designation=models.CharField(max_length=200)

    #def __str__(self):
        #return self.name


class Order(models.Model):
    #order_id=models.IntegerField(order_id,on_delete=models.CASCADE)
    food_item=models.ForeignKey(Food,on_delete=models.CASCADE)
    #food_item1 = models.ForeignKey(NorthIndianVeg, on_delete=models.CASCADE)
    #food_item2 = models.ForeignKey(NorthIndianNonveg, on_delete=models.CASCADE)
    #food_item3 = models.ForeignKey(South_Indian_Veg, on_delete=models.CASCADE)
    #food_item4 = models.ForeignKey(South_Indian_Nonveg, on_delete=models.CASCADE)
    room_type=models.ForeignKey(Room,on_delete=models.CASCADE)
    user_id=models.IntegerField()
    order_timestamp=models.DateTimeField()
    status=models.CharField(max_length=200)

    def __str__(self):
        return self.status

