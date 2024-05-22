def elementAccess(complex_list,Custom):
    for element in complex_list:
        if isinstance(element,list): # this method is used to check type of element
            for i in element:
                print(i)
        elif isinstance(element,dict):
            for key,value in element.items():
                print(f"all dictionary type data in list : \n {key}:{value}\n")
                if isinstance(value,list):
                    for i in value:
                        print("value of ",key,"",i)
                if isinstance(value,dict):
                    for key,value in value.items():
                        print(f"dictionary type data : \n {key}:{value}\n")
                if isinstance(value,Custom):
                    value.display()
        elif isinstance(element,tuple):
            for i in element:
                print("tuple value in given list",i)
        else:
            print(element)
        