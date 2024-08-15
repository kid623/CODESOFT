names=[]
contact_numbers=[]
emails_id=[]
num=int(input("Enter the how many numbers of contact that you need to be save: "))
for phone in range(num):
    name=input("name: ")
    contact_number=int(input("contact number: "))
    email_id=input("email id: ")
    names.append(name)
    contact_numbers.append(contact_number)
    emails_id.append(email_id)
print("\nName\t\tContact Number\t\tEmail id\n")
for phone in range(num):
    print("{}\t\t{}\t\t{}".format(names[phone], contact_numbers[phone], emails_id[phone]))
