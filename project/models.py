from accountapp import models
from django.contrib.auth.models import User

class Project(models.Model):
    name_ar = models.CharField(max_length=180 , blank=True)
    name_en = models.CharField(max_length=180 , blank=True)
    note_ar = models.CharField(max_length=180 , blank=True)
    note_en = models.CharField(max_length=180 , blank=True)
    user_add = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True, related_name="add_unit")
    user_edit = models.ForeignKey(User,on_delete=models.PROTECT, blank=True,null=True , related_name="edit_unit")
    date_add = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    date_edit = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name