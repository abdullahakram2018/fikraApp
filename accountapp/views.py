from userapp.models import Profile
import json
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response
from accountapp.serializers import *
from accountapp.models import *
from django.db import connection
from django.db.models import Sum , Count
# Create your views here.


@api_view(['GET', 'PUT', 'DELETE','POST'])
@permission_classes((IsAuthenticated, ))
def companys(request):
 
    try:
        company_id = request.POST['company_id']
        company = Company.objects.filter(id=company_id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer(company,many=True)

        return Response({"detailcompany":serializer.data})
    
    elif request.method == 'POST':
        serialize = CompanySerializer(data=request.data, many=isinstance(request.data,list))
       
        if serialize.is_valid(raise_exception=True) :
            
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save(id=Company.objects.get(id=company_id))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE','POST'])
@permission_classes((IsAuthenticated, ))
def branch(request):

    try:
        company_id = request.POST['company_id']
        branch_id = request.POST['branch_id']
        company = Branch.objects.filter(company=company_id)
        branch = Branch.objects.filter(id=branch_id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer(branch,many=True)

        return Response({"detailbranch":serializer.data})
    
    elif request.method == 'POST':
        serialize = BranchSerializer(data=request.data, many=isinstance(request.data,list))
        if serialize.is_valid(raise_exception=True) :
            serialize.save(company=Company.objects.get(id=company_id))
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save(company=Company.objects.get(id=company_id))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class SaleUserViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def create(self, request, *args, **kwargs):
        data = request.data.get('items', request.data)
        many = isinstance(data, list)
        print (data, many)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
        )
"""
    Retrieve, Insert , update or delete a code TypeDoc.
"""

@api_view(['POST','GET'])
@permission_classes((IsAuthenticated, ))
def typeDoc_api(request):

    """
    Retrieve or post a code typeDoc.
    """
    
    try:
        typeDoc = TypeDoc.objects.all()
        user = request.user
    except TypeDoc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer_typeDoc = TypeDocSerializer(typeDoc,many=True)
        return Response({"typeDoc":serializer_typeDoc.data})
    
    user = request.user
    serialize_typeDoc = TypeDocSerializer(data=request.data)
    if serialize_typeDoc.is_valid(raise_exception=True):
        serialize_typeDoc.save(user_add = user)
        return Response(serialize_typeDoc.data,status=status.HTTP_201_CREATED)
    return Response(serialize_typeDoc.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def typeDoc_detail(request, pk):
  
    """
    Retrieve, update or delete a code TypeDoc.
    """
    try:
        
        typeDoc = TypeDoc.objects.get(pk=pk)
        user = request.user
    except TypeDoc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_typeDoc = TypeDocSerializer(typeDoc)
        return Response(serializer_typeDoc.data)

    elif request.method == 'PUT':
        serializer_typeDoc = TypeDocSerializer(typeDoc, data=request.data)
        if serializer_typeDoc.is_valid():
            serializer_typeDoc.save(user_edit = user)
            return Response(serializer_typeDoc.data)
        return Response(serializer_typeDoc.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        typeDoc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



"""
    Retrieve, Insert , update or delete a code Currency.
"""
@api_view(['POST','GET'])
@permission_classes((IsAuthenticated, ))
def currency_api(request):

    """
    Retrieve or post a code Currency.
    """
    
    try:
        currency = Currency.objects.all()
        user = request.user
    except Currency.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer_currency = CurrencySerializer(currency,many=True)
        return Response({"currency":serializer_currency.data})
    
    elif request.method == 'POST':
        serialize_currency = CurrencySerializer(data=request.data, many=isinstance(request.data,list))
        if serialize_currency.is_valid(raise_exception=True):
            serialize_currency.save(user_add = user)
            return Response(serialize_currency.data,status=status.HTTP_201_CREATED)
        return Response(serialize_currency.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def currency_detail(request, pk):
  
    """
    Retrieve, update or delete a code Currency.
    """
    try:
        
        currency = Currency.objects.get(pk=pk)
        user = request.user
    except Currency.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_currency = CurrencySerializer(currency)
        return Response(serializer_currency.data)

    elif request.method == 'PUT':
        serializer_currency = CurrencySerializer(currency, data=request.data)
        if serializer_currency.is_valid():
            serializer_currency.save(user_edit = user)
            return Response(serializer_currency.data)
        return Response(serializer_currency.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        currency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




"""
    Retrieve, Insert , update or delete a code Accounts.
"""
@api_view(['POST','GET'])
@permission_classes((IsAuthenticated, ))
def account_api(request):

    """
    Retrieve or Insert a code Accounts.
    """
    
    try:
        account = Account.objects.all()
        user = request.user
        profile = Profile.objects.filter(user=user.id)
        branch_id = profile
        print(branch_id)
        
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        print(branch_id)
        serializer = AccountSerializer(account,many=True)
        return Response({"account":serializer.data})
    
    elif request.method == 'POST':
        serialize = AccountSerializer(data=request.data, many=isinstance(request.data,list))
        if serialize.is_valid(raise_exception=True):
            serialize.save(user_add = user)
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def group_account_api(request):    
    try:
        account = Account.objects.filter(typeAccount="main")
        
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AccountSerializer(account,many=True)
        return Response({"account":serializer.data})


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def account_detail(request, pk):
  
    """
    Retrieve, update or delete a code Account.
    """
    try:
        
        account = Account.objects.get(pk=pk)
        user = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save(user_edit = user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



"""
    Retrieve, Insert , update or delete a code Units.
"""
@api_view(['POST','GET'])
@permission_classes((IsAuthenticated, ))
def unit_api(request):

    """
    Retrieve or Insert a code Units.
    """
    
    try:
        unit = Unit.objects.all()
        user = request.user
    except Unit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UnitSerializer(unit,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serialize = UnitSerializer(data=request.data, many=isinstance(request.data,list))
        if serialize.is_valid(raise_exception=True):
            serialize.save(user_add = user)
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def unit_detail(request, pk):
  
    """
    Retrieve, update or delete a code Units.
    """
    try:
        
        unit = Unit.objects.get(pk=pk)
        user = request.user
    except Unit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UnitSerializer(unit)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UnitSerializer(unit, data=request.data)
        if serializer.is_valid():
            serializer.save(user_edit = user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        unit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



"""
    Retrieve, Insert , update or delete a code Items.
"""
@api_view(['POST','GET'])
@permission_classes((IsAuthenticated, ))
def item_api(request):

    """
    Retrieve or Insert a code Items.
    """
    
    try:
        item = Item.objects.all()
        user = request.user
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ItemSerializer(item,many=True)
        return Response({"item":serializer.data})
    
    elif request.method == 'POST':
        serialize = ItemSerializer(data=request.data, many=isinstance(request.data,list))
        if serialize.is_valid(raise_exception=True):
            serialize.save(user_add = user)
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def item_detail(request, pk):
  
    """
    Retrieve, update or delete a code Items.
    """
    try:
        
        item = Item.objects.get(pk=pk)
        user = request.user
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save(user_edit = user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



"""
    Retrieve, Insert , update or delete a code Stores.
"""
@api_view(['POST','GET'])
@permission_classes((IsAuthenticated, ))
def store_api(request):

    """
    Retrieve or Insert a code Stores.
    """
    
    try:
        store = Store.objects.all()
        user = request.user
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StoreSerializer(store,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serialize = StoreSerializer(data=request.data, many=isinstance(request.data,list))
        if serialize.is_valid(raise_exception=True):
            serialize.save(user_add = user)
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def store_detail(request, pk):
  
    """
    Retrieve, update or delete a code Stores.
    """
    try:
        
        store = Store.objects.get(pk=pk)
        user = request.user
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StoreSerializer(store)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save(user_edit = user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



"""
    Retrieve, Insert , update or delete a code Entrys.
"""
@api_view(['POST','GET'])
@permission_classes((IsAuthenticated, ))
def entry_api(request):

    """
    Retrieve or Insert a code entrys.
    """
    
    try:
        entry = Entry.objects.all()
        user = request.user
    except Entry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EntrySerializer(entry,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serialize = EntrySerializer(data=request.data)
        if serialize.is_valid(raise_exception=True) :
            serialize.save(user_add = user)
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def entry_detail(request, pk):
  
    """
    Retrieve, update or delete a code Entry.
    """
    try:
        
        entry = Entry.objects.get(pk=pk)
        user = request.user
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EntrySerializerDisplay(entry)
        return Response({"entry":serializer.data})

    elif request.method == 'PUT':
        serializer = EntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save(user_edit = user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE','POST'])
@permission_classes((IsAuthenticated, ))
def detail_entry_detail(request, pk):
  
    """
    Retrieve, update or delete or insert a code DetailEntry.
    """
    try:
        
        entry = EntryDetails.objects.filter(entry=pk)
    except EntryDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EntryDetailsDisplaySerializer(entry,many=True)

        return Response({"detailentry":serializer.data})
    
    elif request.method == 'POST':
        serialize = EntryDetailsSerializer(data=request.data, many=isinstance(request.data,list))
        if serialize.is_valid(raise_exception=True) :
            serialize.save(entry=Entry.objects.get(id=pk))
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = EntryDetailsSerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save(entry=Entry.objects.get(id=pk))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE','POST'])
@permission_classes((IsAuthenticated, ))
def account_entry_detail(request, pk):
  
    """
    Retrieve, update or delete or insert a code AccountEntry.
    """
    try:
        
        entry = AccountEntry.objects.filter(entry=pk)
        
    except AccountEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        qury=AccountEntry.objects.filter(entry=pk).aggregate(creditor=Sum(str('creditor')),debtor=Sum(str('debtor')))
        banlance = entry.annotate(credito=Sum(str('creditor')))
        serializer = AccountEntryDisplaySerializer(entry,many=True)
        return Response({"accountentry":serializer.data,"sumdebtor":qury})
    
    elif request.method == 'POST':
        serialize = AccountEntrySerializer(data=request.data, many=isinstance(request.data,list))
        if serialize.is_valid(raise_exception=True) :
            serialize.save(entry=Entry.objects.get(id=pk))
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = AccountEntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
def account_book(request):
  
    """
    Retrieve a code Account Book.
    """
    try:
        account = request.POST['account']
        fristdate = request.POST['fristdate']
        lastdate = request.POST['lastdate']
        currency = request.POST['currency']
        accountEntry = AccountEntry.objects.select_related('entry').filter(account=account)
        entry = accountEntry.filter(entry__date__range=(fristdate,lastdate)).filter(entry__currency=currency)
    except AccountEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = AccountEntrySerializer(entry,many=True)
        return Response(serializer.data)
    

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
def bill(request):
  
    """
    Retrieve a code Bill.
    """
    try:
        entry = request.POST['entry']
        entry1 = Entry.objects.filter(id=entry)
    except Entry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = EntrySerializer(entry1,many=True)
        return Response(serializer.data)
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
def trial_balance(request):
  
    """
    Retrieve a code AccountEntry.
    """
    try:
        currency = request.POST['currency']
        banlance = AccountEntry.objects.values('account__name','entry__currency__name').order_by('account__name').annotate(creditor=Sum(str('creditor')),debtor=Sum(str('debtor')))
    except AccountEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
      #  serializertrial = AccountEntrybalanceSerializer(entry2,many=True)
        serializer = AccountEntrySerializer(banlance,many=True)
    return Response(banlance)
  
