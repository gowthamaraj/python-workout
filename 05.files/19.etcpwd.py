'''
 In this exercise, write a function, passwd_to_dict, that reads from a Unix-style
“password file,” commonly stored as /etc/passwd, and returns a dict based on it. If
you don’t have access to such a file, you can download one that I’ve uploaded at
http://mng.bz/2XXg
'''

def passwd_to_dict(filename):
    users = {}
    with open(filename) as file:
        for line in file:
            if not line.startswith(('#','\n')):
                data = line.split(':')
                users[data[0]] = int(data[2])
    return users

print(passwd_to_dict('05.files\passwd.txt'))