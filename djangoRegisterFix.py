# From Codemy to fix a register problem in Django
# MultiValueDictKeyError at/register
# 'username'
def register(request):
    if request.method=='POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is in use')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                message.info(request, 'username already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, email=email,password=password)
                user.save()
                return redirect('login')
         else:
             messages.info(request, 'Password is not the same')

    else:
        return render(request, 'register.html')

