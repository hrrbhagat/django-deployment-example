from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Topic,Webpage,AccessRecord,App_Users

# Create your views here.
def index(request):
    #return HttpResponse("Welcome to First Project Raghavendra!")
    webpages_list = App_Users.objects.order_by('user_name')
    date_dict = {'user_records':webpages_list}
    my_dict = {'insert_me':"Hello I am Raghavendra I will master this  in 2 months"}
    return render(request,'ProTwo/index.html',context=date_dict)


def help_fun(request):
    my_dict = {'help_fun':"I have created the help page"}
    return render(request,'ProTwo/help.html',context=my_dict)
