from get_institutions import generate_institutions


def get_datax_enabled_institutions():
    institutions = []
    
    for institution in generate_institutions():
        if institution["function-datax-enabled"]:
            institutions.append(institution)
    
    return institutions
if __name__ == '__main__':
    data= get_datax_enabled_institutions()
    print(data)