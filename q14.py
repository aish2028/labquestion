product={}

def add():
    product

while True:
    print("1.add 2.display 3.search 4.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        pid=input("enter the product id:")
        pname=input("enter the product name:")
        products[pid]=pname

    elif ch==2:
       if len(product)==0:
           pass
        else:
            for k,v in products:
                print(f"{k}:{v}")
    elif ch==3:
       pid=input("enter the product id:")
       if product
    else:
        break