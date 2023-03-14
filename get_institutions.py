def generate_institutions():
    institutions = []
    
    for i in range(1, 6):
        function_datax_enabled = True
        function_attendance_plus_enabled = True
        if i == 3:
            function_datax_enabled = False
        if i == 2:
            function_attendance_plus_enabled = False
        institution = {
            "name": f"institution_{i}",
            "function-datax-enabled": function_datax_enabled,
            "function-alma-enabled": None,
            "function-campusm-enabled": None,
            "function-curriculum-analytics-enabled": True,
            "function-dataexport-enabled": None,
            "function-attendance-plus-enabled": function_attendance_plus_enabled

        }
        institutions.append(institution)
    
    return institutions


if __name__ == '__main__':
    data= generate_institutions()
    print(data)