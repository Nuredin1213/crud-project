from django.shortcuts import render,redirect
from.forms import CreateUserForm,LoginForm,createRecordFORM,UpdateRecordFORM
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from.models import Record




#home page
def home(request):
    return render(request,'index.html')



#register page
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created successfully!')
                  #ew also save to user database registerd hone malet new 
            return redirect('my-login') #successmessage login lay load mareg
        # bizu gize redirect stareg page dispaly yileyal yaw info silemnlik message info redirect yderegal message login page lay display mareg

    # else:
    return render(request,'register.html',{'form':form})


# log in page

def my_login(request):
    form = LoginForm()
    if request.method == 'POST': # just authentication purpose not adding to database
        form=LoginForm(request,data=request.POST) #ye loginform behavior new
        if form.is_valid(): #under this check the authenticate if fullfilled redirect to the neccssery page
            username=request.POST.get('username')
            password = request.POST.get('password')
            user =authenticate(request,username=username,password=password) # we create for authentication purpose User object
            if user is not None:
                auth.login(request,user) # authenticate honoal wedemifelegew page lemegbat biku new
                messages.success(request,'you have logged in!')
                return redirect('dashboard') #redirect ykebelewal since the user authenticated(nav bar displaye yileyal b/c user alread yauthenticated)
    else:
      return render(request,'my-login.html',{'form':form})
    
    
   # user logout 
    
def my_logout(request):# this myadergewn yegeletsnew linku yet enasgebaw lelaneger new
    auth.logout(request) # auth endetefa maswetat by redirect
    messages.success(request,'logout success!')
    return redirect('my-login')


#dashboard
@login_required(login_url='my-login') # authenticated yehone
def dashboard(request):#actullly login sibal redirect ygebal
    records = Record.objects.all() # ke database yewsdal kagegne(manupulate)in this case case the record gained by forms and saved in database
    return render(request,'dashboard.html',{'records':records})
    

#create record
@login_required(login_url='my-login') # under dashboard new yemfelgew (be link kalhone ayseram) login yalut bcha yemyagegnut access new jjust / mnamin bileh url siletsafk access ataregewm
def create_record(request): # we create or add record to database....dash borad ke database new ywesdal
    form = createRecordFORM()
    if request.method == 'POST':
        form = createRecordFORM(request.POST)  #  here yalkeyenew b/c author is not attribute of form but to the model 
        if form.is_valid():
            instance =    form.save(commit=False) # ( here for wede model object tekeyroal) 100 save kemaregachn befit forignkey value set enaregalen defaula endaywesed cascade
            instance.author =request.user  #  w/c user yemilewn ezih decide taregaleh (tere is user sice it is under login)
            instance.save()    # instane is object of the model so it has attribute author
         # we use this since record egna be database silemanfetrew any time for simola erasu endifetrew
            messages.success(request,'your record was created!')
            return redirect('dashboard')  #yefeteratn dash table lay add hona yagegnatal (mangnawm sew eyegeba add mareg ychlal)(evry time url stera change kale yekyeral since link starts form url then view fun.....)
#    we can since under here the user is authenticated
    
    return render(request,'create-record.html',{'form':form}) # we add this path as link in dashboard

# update record
@login_required(login_url='my-login')
def update_record(request,pk): #linku schanu need form w/c has info then update replace
    record = Record.objects.get(id=pk) #first using the id the specific record new miagegnut
    form =UpdateRecordFORM(instance=record) #simply we editing the record ye record inf yeyaze so that replace lemadreg (update mtaregewn merteh mareg) edit argeh post req tlkaleh
    if request.method=='POST':
        form =UpdateRecordFORM(request.POST,instance=record)
        # here we update (except the id) with info submitted by user
        if form.is_valid():
            form.save()      #  record endegena save tderegalech with the new update(post.request yza)
            messages.success(request,'Your record is updated!')
            return redirect('dashboard') # in the dash we see info updated (url daynamic id mostly with link with proper id )



    return render(request,'update-record.html',{'form':form})
#     we give the page(infown with the specific id endeyaze) update siteyikku with spacific id

#   read/view a singular record
@login_required(login_url='my-login')
def singular_record(request,pk):# zmbleh yehone path record bemymir display yemyareg yemneftrw page
    record =Record.objects.get(id=pk) # we identifi the record  the right id mgnet easy(link stader the proper id chemreh)
    return render(request,'view-record.html',{'record':record})  #  link snareg tikiklegna yemfelegewn silemnset perfect yseralid



@login_required(login_url='my-login')
def delete_record(request,pk): # how we use the id wanaw neger
    record =Record.objects.get(id=pk)
    record.delete()
    messages.success(request,'Your record was deleted!')
    return redirect('dashboard') # delete  hono enagegnewalen










# Create your views here.
