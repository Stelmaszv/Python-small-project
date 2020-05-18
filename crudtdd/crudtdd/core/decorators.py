from django.shortcuts import redirect
def login_required(func):
    def wrapper(*args, **kwargs):
        print('fqef')
        value = func(*args, **kwargs)
        if args[1].user.is_anonymous:
            print(args[1])
            return redirect('auth/accounts/login/')
        return value
    return wrapper