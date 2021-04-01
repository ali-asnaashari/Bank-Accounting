from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from Bank.settings import BASE_DIR
# Create your views here.
import requests
import json

#---------------------------------------------------------MAIN PAGE-------------------------------------------------------------

# WORKED
def system(request):
    return render(request,'system/system.html')

#---------------------------------------------------------SHOW ACCOUNT LIST-------------------------------------------------------------

# WORKED
# GET Method
def account_list(request):
    
    f = open(BASE_DIR + '\\token.txt', 'r')
    token = f.read()
    f.close()

    acc_list_url = 'http://176.9.164.222:2211/api/accounts/BankAccountListCreate'
    # print(token)
    resp = requests.get(acc_list_url, headers={'Authorization': 'JWT ' + token})

    if resp.status_code == 200:
        list_of_bank_accounts = json.loads(resp.text)
        return render(request,'system/account_list.html', {'lst_acc':list_of_bank_accounts})
        # print(list_of_bank_accounts)
    else:
        return render(request,'NotFound/404.html')

#---------------------------------------------------------CREATE ACCOUNT LIST-------------------------------------------------------------

# WORKED
# POST Method
def create_account_list(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        phoneNumber = request.POST['phoneNumber']
        nationalCode = request.POST['nationalCode']
        login_data = {"accountOwner":{'firstName': firstName, 'lastName': lastName,'phoneNumber': phoneNumber,'nationalCode': nationalCode}}
        login_url = 'http://176.9.164.222:2211/api/accounts/BankAccountListCreate'
        f = open(BASE_DIR + '\\token.txt', 'r')
        token = f.read()
        f.close()
        resp = requests.post(login_url, json=login_data,headers={'Authorization': 'JWT ' + token})

        if resp.status_code == 200 : # successful !!
            # list_of_bank_accounts = json.loads(resp.text)
            # return render(request,'system/create_account_list1.html', {'lst_acc':list_of_bank_accounts})
            return HttpResponse(resp.text)
        else:
            
            # return render(request,'NotFound/404.html')
            list_of_bank_accounts = json.loads(resp.text)
            return render(request,'system/create_accountP.html', {'lst_acc':list_of_bank_accounts})

    else:
        return render(request,'system/create_account_list.html')


#---------------------------------------------------------SIGN UP -------------------------------------------------------------

# WORKED 
# POST Method  
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        signup_url = 'http://176.9.164.222:2211/api/accounts/User/SignUp'
        signup_data = {'username': username, 'password': password}
        
        f = open(BASE_DIR + '\\token.txt', 'r')
        token = f.read()
        f.close()
        resp = requests.post(signup_url, signup_data,headers={'Authorization': 'JWT ' + token})

        if resp.status_code == 200 :
            json_resp = json.loads(resp.text)
            f = open(BASE_DIR + '\\token.txt', 'w')
            f.write(json_resp['token'])
            f.close()
            return render(request,'system/system.html')
        else:
            return HttpResponse(resp.text)
            # return render(request,'NotFound/404.html')
    else:
        return render(request,'system/signup.html')

#---------------------------------------------------------ACCOUNT LOG-------------------------------------------------------------

# WORKED
# POST Method
def account_log(request):
    if request.method == "POST":
        f = open(BASE_DIR + '\\token.txt', 'r')
        token = f.read()
        f.close()
        # print(token)
        log_list_url = 'http://176.9.164.222:2211/api/accounts/GetBankAccountLogs'
        accountNumber = request.POST['accountNumber']
        log_data = {'accountNumber':accountNumber}
        resp = requests.post(log_list_url,log_data, headers={'Authorization': 'JWT ' + token})

        if resp.status_code == 200:
            list_of_bank_accounts = json.loads(resp.text)
            return render(request,'system/account_logsP.html', {'lst_acc':list_of_bank_accounts})
            # return HttpResponse(resp.text)       
            
        else:
            # return HttpResponse(resp.text)
            return render(request,'NotFound/404.html')

    else:
        return render(request,'system/BankAccountLogs.html')

#---------------------------------------------------------ACCOUNT 0WNER-------------------------------------------------------------

# WORKED
# POST Method
def account_owener(request):
    if request.method == "POST":
        f = open(BASE_DIR + '\\token.txt', 'r')
        token = f.read()
        f.close()
        # print(token)
        owner_url = 'http://176.9.164.222:2211/api/accounts/AddAccountToAccountOwner'
        nationalCode = request.POST['nationalCode']
        owner_data = {'nationalCode':nationalCode}
        resp = requests.post(owner_url,json = owner_data, headers={'Authorization': 'JWT ' + token})

        if resp.status_code == 200:
            list_of_bank_accounts = json.loads(resp.text)
            return render(request,'system/account_ownerP.html', {'lst_acc':list_of_bank_accounts})
            # return HttpResponse(resp.text)
        else:
            #  return HttpResponse(resp.text)
            return render(request,'NotFound/404.html')

    else:
        return render(request,'system/AccountOwner.html')

#---------------------------------------------------------CLOSE ACCOUNT-------------------------------------------------------------

# WORKED
# POST Method
def close(request):
    if request.method == "POST":
        f = open(BASE_DIR + '\\token.txt', 'r')
        token = f.read()
        f.close()
        # print(token)
        close_url = 'http://176.9.164.222:2211/api/accounts/CloseAccount'
        accountNumber = request.POST['accountNumber']
        close_data = {'accountNumber':accountNumber}
        resp = requests.post(close_url,json=close_data, headers={'Authorization': 'JWT ' + token})

        if resp.status_code == 200:
            # json_resp = json.loads(resp.text)
            return HttpResponse(resp.text)
        else:
            return HttpResponse(resp.text)
            # return render(request,'NotFound/404.html')

    else:
        return render(request,'system/close.html')

#----------------------------------------------------------BLOCK ACCOUNT-------------------------------------------------------------

# WORKED
# POST Method
def block(request):
    if request.method == "POST":
        f = open(BASE_DIR + '\\token.txt', 'r')
        token = f.read()
        f.close()
        # print(token)
        block_url = 'http://176.9.164.222:2211/api/accounts/BlockAccount'
        accountNumber = request.POST['accountNumber']
        block_data = {'accountNumber':accountNumber}
        resp = requests.post(block_url,block_data, headers={'Authorization': 'JWT ' + token})

        if resp.status_code == 200:
            # json_resp = json.loads(resp.text)
            # return render(request,'system/system.html')
            return HttpResponse(resp.text)
        else:
            return render(request,'NotFound/404.html')

    else:
        return render(request,'system/block.html')

#----------------------------------------------------------ACCOUNT RETRIVE-------------------------------------------------------------

# GET Method
def retrive_account(request):

    if request.method == 'POST':
        retrive_url = 'http://176.9.164.222:2211/api/accounts/BankAccountRetrieve/'
        f = open(BASE_DIR + '\\token.txt', 'r')
        token = f.read()
        f.close()
        retrive_data = {'accountNumber':request.POST['accountNumber']}
        retrive_url = retrive_url + retrive_data['accountNumber']
        resp = requests.get(retrive_url, headers={'Authorization': 'JWT ' + token})

        if resp.status_code == 200:
            list_of_bank_accounts = json.loads(resp.text)
            return render(request,'system/retriveP.html', {'lst_acc':list_of_bank_accounts})
            # return HttpResponse(resp.text)
        else:
            # return HttpResponse(resp.text)
            return render(request,'NotFound/404.html')

    return render(request,'system/retrive_account.html')
        

# ----------------------------------------------------------ACCOUNT OWNER RETRIVE-------------------------------------------------------------

# GET Method
def retrive_owner(request):

    if request.method == 'POST':
        retrive_owner_url = 'http://176.9.164.222:2211/api/accounts/AccountOwnerRetrieve/'
        f = open(BASE_DIR + '\\token.txt', 'r')
        token = f.read()
        f.close()
        retrive_data = {'nationalCode':request.POST['nationalCode']}
        retrive_owner_url = retrive_owner_url + retrive_data['nationalCode']
        resp = requests.get(retrive_owner_url, headers={'Authorization': 'JWT ' + token})

        if resp.status_code == 200:
            list_of_bank_accounts = json.loads(resp.text)
            return render(request,'system/retrive_owP.html', {'lst_acc':list_of_bank_accounts})
            # return HttpResponse(resp.text)
        else:
            # return HttpResponse(resp.text)
            return render(request,'NotFound/404.html')

    return render(request,'system/retrive_owner.html')
    

# ----------------------------------------------------------CREATE TRANSACTION LIST-------------------------------------------------------------

# WORKED
# POST Method
def transaction(request):

    if request.method == "POST":
        fromAccount = request.POST['fromAccount']
        toAccount = request.POST['toAccount']
        amount = request.POST['amount']
        definition = request.POST['definition']
        cash = request.POST['cash']
        transaction_data = {'fromAccount': fromAccount, 'toAccount': toAccount,'amount': amount,'definition': definition,'cash': cash}
        transaction_url = 'http://176.9.164.222:2211/api/transaction/TransactionListCreate'
        f = open(BASE_DIR + '\\token.txt', 'r')
        token = f.read()
        f.close()
        resp = requests.post(transaction_url, json = transaction_data,headers={'Authorization': 'JWT ' + token})

        if resp.status_code == 200 : # successful !!

            return HttpResponse(resp.text)
            # return render(request,'NotFound/404.html')

        else:
            list_of_bank_accounts = json.loads(resp.text)
            return render(request,'system/transaction_post.html', {'lst_acc':list_of_bank_accounts})
            # return HttpResponse(resp.text)
        
    else:
        return render(request,'system/TransactionList.html')

# ----------------------------------------------------------TRANSACTION LIST CATCH-------------------------------------------------------------

# GET Method
# WORKED
def transaction_get(request):
    f = open(BASE_DIR + '\\token.txt', 'r')
    token = f.read()
    f.close()
    # print(token)
    trans_get_url = 'http://176.9.164.222:2211/api/transaction/TransactionListCreate'
    resp = requests.get(trans_get_url, headers={'Authorization': 'JWT ' + token})

    if resp.status_code == 200:
        list_of_bank_accounts = json.loads(resp.text)
        return render(request,'system/transaction_get.html', {'lst_acc':list_of_bank_accounts})
        # return HttpResponse(resp.text)
    else:
        return render(request,'NotFound/404.html')