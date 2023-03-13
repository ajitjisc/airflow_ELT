import os
import time
from get_datax_enabled_institutions import get_datax_enabled_institutions

def check_file_updated_within_2_mins(file_path):
    if os.path.exists(file_path):
        mod_time = os.path.getmtime(file_path)
        current_time = time.time()
        if current_time - mod_time <= 120:
            return True
    return False

def check_report1():
    reports = ['report1.tsv']
    institutions = get_datax_enabled_institutions()

    for inst in institutions:
        inst_name = inst['name']
        inst_reports_path = os.path.join(inst_name, 'reports')
        if os.path.exists(inst_reports_path):
            for report in reports:
                file_path = os.path.join(inst_reports_path, report)
                if not check_file_updated_within_2_mins(file_path):
                    raise Exception(f"{file_path} has not been updated within 2 mins.")
        else:
            print(f"No reports found in {inst_name}.")


def check_report2():
    reports = ['report2.tsv']
    institutions = get_datax_enabled_institutions()

    for inst in institutions:
        inst_name = inst['name']
        inst_reports_path = os.path.join(inst_name, 'reports')
        if os.path.exists(inst_reports_path):
            for report in reports:
                file_path = os.path.join(inst_reports_path, report)
                if not check_file_updated_within_2_mins(file_path):
                    raise Exception(f"{file_path} has not been updated within 2 mins.")
        else:
            print(f"No reports found in {inst_name}.")


def check_report3():
    reports = ['report3.tsv']
    institutions = get_datax_enabled_institutions()

    for inst in institutions:
        inst_name = inst['name']
        inst_reports_path = os.path.join(inst_name, 'reports')
        if os.path.exists(inst_reports_path):
            for report in reports:
                file_path = os.path.join(inst_reports_path, report)
                if not check_file_updated_within_2_mins(file_path):
                    raise Exception(f"{file_path} has not been updated within 2 mins.")
        else:
            print(f"No reports found in {inst_name}.")



                
if __name__ == '__main__':
    check_report3()


