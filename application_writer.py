print("IF YOU WANT TO MAKE APPLICATION TO MANAGER GIVE DETAIL")
your_name = input("NAME: ")
your_address = input("ADDRESS:  ")
email = input("EMAIL: ")
phone_number = input("PHONE NUMBER: ")
manager_name = input("MANAGER NAME: \n\n\n")

print(
f"""{your_name}
{your_address}
{email}
{phone_number}
{manager_name}

Dear {manager_name},

I am writing to inform you that I am unable to attend work due to a severe illness. I have been diagnosed with [specific illness, if comfortable sharing] by my doctor and have been advised to take rest for [number of days] days, starting from [start date] to [end date].

I apologize for any inconvenience my absence may cause and assure you that I will make every effort to complete my pending tasks before I leave and will hand over any urgent matters to my colleagues. During my leave, I will be reachable via email ([your email address]) or phone ([your phone number]) should any urgent issues arise that require my attention.

Thank you for your understanding and support. I look forward to returning to work as soon as I am well.

Yours sincerely,

{your_name}
\nsoftware engineer
"""
)
