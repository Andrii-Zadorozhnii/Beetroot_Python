def check_password(password):
    x = []
    z = []
    for i in password:
        x.append(i)
        if i.isdigit():
            z.append(i)
    c = ['!','@','#','$','%','*']
    # return 'Perfect password!'
    if len(z) >= 2:
        if any(char.isupper() for char in password):
            if any(char in password for char in c):
                if len(password) > 10:
                    return 'Perfect password!'
                else:
                    print('password is too short')
            else:
                print('password dont have !,@,#,$,%,* ')
        else:
            print('no uppercase letters')
    else:
        print("Easy peasy")

print(check_password('2PA%SSW%ORD%2'))

def get_domain_name(url):
    url_2 = url.replace("www.", '')
    url_3 = url_2.replace("http://", '')
    url_4 = url_3.replace("https://", '')
    print(url_4)
    return url_4

print(get_domain_name('https://youtube.com'))