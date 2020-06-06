files_permissions = {'helloworld.exe': ('R', 'X'), 'pinglog': ('W', 'R'), 'nya': 'R', 'goodluck': ('X', 'W', 'R')}
operations_with_files = {'read': ('nya', 'pinglog'), 'write': ('helloworld.exe', 'pinglog'), 'execute': 'nya'}


def clean_dict(d):
    return {k: v if not isinstance(v, str) else (v,) for k, v in d.items()}


def check_access(file,permission_list, permission):
    if permission in permission_list:
        print(file, permission, 'Ok')
    else:
        print(file, permission, 'Access denied')


def file_operation(files_dict, operations_dict):

    files_dict = clean_dict(files_dict)
    operations_dict = clean_dict(operations_dict)
    print(files_dict)
    print(operations_dict)
    for elem in operations_dict:
        if elem == 'read':
            permission = 'R'
        elif elem == 'write':
            permission = 'W'
        else:
            permission = 'X'

        [check_access(x, files_dict[x], permission) for x in operations_dict[elem]]


file_operation(files_permissions, operations_with_files)
