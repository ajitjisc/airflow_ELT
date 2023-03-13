
from get_datax_enabled_institutions import get_datax_enabled_institutions
from reports import generate_report1,generate_report2,generate_report3

import os

def check_attendance_plus_and_generate_reports():
    institutions = get_datax_enabled_institutions()
    for institution in institutions:
        reports_dir = os.path.join(institution['name'], 'reports')
        os.makedirs(reports_dir, exist_ok=True)
        if institution['function-attendance-plus-enabled']:
            generate_report3(os.path.join(reports_dir, 'report3.tsv'))
        generate_report1(os.path.join(reports_dir, 'report1.tsv'))
        generate_report2(os.path.join(reports_dir, 'report2.tsv'))

if __name__ == '__main__':
    data = check_attendance_plus_and_generate_reports()