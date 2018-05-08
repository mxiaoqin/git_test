import os
import time

patch = os.path.dirname(os.path.realpath(__file__))
print(patch)

case_list = [

    'hello.py',
    'teacher.py',
    'student.py',
]


def run_case(patch, case_list):
    for i in range(0, len(case_list)):
        os.system('python ' + patch + '/testcase/' + case_list[i])
        time.sleep(1)


if __name__ == '__main__':
    print('start')
    print(patch)
    run_case(patch, case_list)
    print('end')
