str=input("enter the sentense:")
lst=['does','do','is','are']
res=filter(lambda x:x.startswith(lst),str)
if res:
    print("interogative")
else:
    print("assertive")

    question=input("enter the question:")
    if question.endswith