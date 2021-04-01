from django.shortcuts import render,redirect
from django.contrib import messages
from Bank.settings import BASE_DIR
# Create your views here.
import requests
import json

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        login_data = {'username': username, 'password': password}
        login_url = 'http://176.9.164.222:2211/api/Login'
        resp = requests.post(login_url, login_data)

        if resp.status_code == 200 : # successful !!
            json_resp = json.loads(resp.text)
            f = open(BASE_DIR + '\\token.txt', 'w')
            f.write(json_resp['token'])
            f.close()
            # return redirect('system') 
            return render(request,'system/system.html')


        else:
            return render(request,'NotFound/404.html')

    else:
        return render(request,'login/login.html')















