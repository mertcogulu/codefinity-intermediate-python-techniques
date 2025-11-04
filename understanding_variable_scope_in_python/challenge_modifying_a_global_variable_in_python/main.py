global_var = 10

def modify_global():
    global global_var
    global_var += 5

modify_global()
print("Modified global variable:", global_var)
