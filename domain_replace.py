#We can provide email adresses , the domain we want to be change and the domain we want it to be

def replace_domain(email,old_domain,new_domain):
    if "@" + "old_domain" in email:
        index=email.index("@"+old_domain)
        new_email=email[:index] + "@" + new_domain
        return new_email
    return email
a=replace_domain("sarthak@gmail.com","gmail.com","abesit.co.in")
print(a)
