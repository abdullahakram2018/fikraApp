from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Company(models.Model):
    name_ar = models.CharField(max_length=180 , blank=True)
    name_en = models.CharField(max_length=180 , blank=True)
    note_ar = models.CharField(max_length=180 , blank=True)
    note_en = models.CharField(max_length=180 , blank=True)
    logo = models.ImageField(upload_to="logo",blank=True)
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_com")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_com")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name_ar
    
class Branch(models.Model):
    name = models.CharField(max_length=180 , blank=True)
    address = models.CharField(max_length=180 , blank=True)
    manager = models.CharField(max_length=180 , blank=True)
    note = models.CharField(max_length=180 , blank=True)
    company = models.ForeignKey(Company,on_delete=models.PROTECT, blank=True,null=True,)
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_branch")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_branch")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name

class TypeDoc(models.Model):
    name = models.CharField(max_length=180 , blank=True)
    note = models.CharField(max_length=180 , blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT, blank=True,null=True, related_name="typedoc_branch")
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_typedoc")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_typedoc")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name
    
class Currency(models.Model):
    code = models.CharField(max_length=10 , blank=True)
    name = models.CharField(max_length=180 , blank=True)
    note = models.CharField(max_length=180 , blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT, blank=True,null=True, related_name="currency_branch")
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_curr")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_curr")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return str(self.name) + " " + str(self.code)
class CurrencyPrice(models.Model):
    currency = models.ForeignKey(Currency,on_delete=models.PROTECT, blank=True,null=True, related_name="currencyprice")
    selling = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    buying = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    note = models.CharField(max_length=180 , blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT, blank=True,null=True, related_name="branchpricecurr")
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="user_addpricecurr")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="user_editpricecurr")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return str(self.selling) + " " + str(self.buying)
    

    
class Account(models.Model):
    name = models.CharField(max_length=180 , blank=True)
    ceiling = models.DecimalField(max_digits=10, decimal_places=2)
    group = models.CharField(max_length=180 , blank=True)
    currency = models.ForeignKey(Currency,blank=True,null=True,on_delete=models.PROTECT)
    typeAccount = models.CharField(max_length=180 , blank=True)
    note = models.CharField(max_length=180 , blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT, blank=True,null=True, related_name="account_branch")
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_acc")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_acc")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name
    
class Unit(models.Model):
    typeUnit = models.CharField(max_length=180 , blank=True)
    name = models.CharField(max_length=180 , blank=True)
    note = models.CharField(max_length=180 , blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT, blank=True,null=True, related_name="unit_branch")
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_unit")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_unit")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=180 , blank=True)
    color = models.CharField(max_length=180 , blank=True)
    note = models.CharField(max_length=180 , blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT, blank=True,null=True, related_name="category_branch")
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_cate")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_cate")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name
class Item(models.Model):
    name = models.CharField(max_length=180 , blank=True)
    lessAmount = models.FloatField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,blank=True,null=True)
    unit = models.ForeignKey(Unit,on_delete=models.PROTECT, blank=True,null=True)
    note = models.CharField(max_length=180 , blank=True)
    barcode = models.CharField(max_length=180 , blank=True)
    tracking = models.BooleanField(default= False,blank=True,null=True)
    sku = models.CharField(max_length=180 , blank=True)
    color = models.CharField(max_length=180 , blank=True)
    image = models.CharField(max_length=180 , blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    package = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT, blank=True,null=True, related_name="item_branch")
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_item")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_item")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name
class ItemPrice(models.Model):
    item = models.ForeignKey(Item,on_delete=models.PROTECT, blank=True,null=True, related_name="itemprice")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    note = models.CharField(max_length=180 , blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT, blank=True,null=True, related_name="priceitem_branch")
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_priceitem")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_priceitem")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return str(self.item) + " " + str(self.price)
    
class Store(models.Model):
    name = models.CharField(max_length=180 , blank=True)
    location = models.CharField(max_length=180 , blank=True)
    capacity = models.CharField(max_length=180 , blank=True)
    storage_status = models.CharField(max_length=180 , blank=True)
    note = models.CharField(max_length=180 , blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT, blank=True,null=True, related_name="store_branch")
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_stor")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_stor")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    desentry = models.CharField(max_length=180 , blank=True,null=True)
    docid =  models.CharField(max_length=180 , blank=True,null=True)
    dateentry = models.DateField( blank = True,null=True)
    typeDoc = models.ForeignKey(TypeDoc,blank=True,null=True,on_delete=models.PROTECT)
    review = models.BooleanField(default= False,blank=True,null=True)
    arvhive = models.ImageField(upload_to='img',blank=True,null=True)
    currency = models.ForeignKey(Currency,blank=True,null=True,on_delete=models.PROTECT)
    noteentry = models.CharField(max_length=180 , blank=True,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.PROTECT, blank=True,null=True, related_name="entry_branch")
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_entry")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_entry")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True,null=True)
    date_edit = models.DateTimeField(auto_now = True, blank = True,null=True)

    def __str__(self):
        return str(self.pk) + " " + str(self.desentry)


class AccountEntry(models.Model):
    entry = models.ForeignKey(Entry,on_delete=models.CASCADE, blank=True,null=True ,related_name="entry_account")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    creditor =  models.ForeignKey(Account,on_delete=models.CASCADE, blank=True,null=True ,related_name="creditor_account")
    debtor =models.ForeignKey(Account,on_delete=models.CASCADE, blank=True,null=True ,related_name="debtor_account")
    note_acc_en = models.CharField(max_length=180 , blank=True)
    def __str__(self):
        return str(self.entry)
    


class EntryDetails(models.Model):
   
    entry = models.ForeignKey(Entry,on_delete=models.CASCADE, blank=True,null=True,related_name="entry_details")
    item = models.ForeignKey(Item,on_delete=models.PROTECT, blank=True,null=True)
    unit = models.ForeignKey(Unit,on_delete=models.PROTECT, blank=True,null=True)
    quantity = models.FloatField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    note_dat_en = models.CharField(max_length=180 , blank=True)
    store = models.ForeignKey(Store,on_delete=models.PROTECT, blank=True,null=True)
    success = models.BooleanField(default= False,blank=True)

    def __str__(self):
        return str(self.entry)
 
