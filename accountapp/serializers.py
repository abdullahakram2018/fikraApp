from rest_framework import serializers
from accountapp.models import *

class TypeDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDoc
        fields = "__all__"
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class EntryAccountSerializer(serializers.ModelSerializer):
    typeDoc = TypeDocSerializer()
    currency = CurrencySerializer()
    class Meta:
        model = Entry
        fields = "__all__"   
class AccountEntrySerializer(serializers.ModelSerializer):
    #entry = EntryAccountSerializer()
    #account = AccountSerializer()
    class Meta:
        model = AccountEntry
        fields = "__all__"
class AccountEntryDisplaySerializer(serializers.ModelSerializer):
    #entry = EntryAccountSerializer()
    account = AccountSerializer()
    class Meta:
        model = AccountEntry
        fields = "__all__"


class EntryDetailsSerializer(serializers.ModelSerializer):
   # entry = EntrySerializer()
    
    class Meta:
        model = EntryDetails
        fields = "__all__"
class EntryDetailsDisplaySerializer(serializers.ModelSerializer):
   # entry = EntrySerializer()
    item = ItemSerializer()
    unit = UnitSerializer()
    
    class Meta:
        model = EntryDetails
        fields = "__all__"

class EntrySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Entry
        fields = "__all__"
class EntrySerializerDisplay(serializers.ModelSerializer):
    accountentry = AccountEntryDisplaySerializer(source='entry_account',many=True)
    Entrydetails = EntryDetailsDisplaySerializer(source='entry_details',many=True)
    typeDoc = TypeDocSerializer()
    currency = CurrencySerializer()
    class Meta:
        model = Entry
        fields = "__all__"

