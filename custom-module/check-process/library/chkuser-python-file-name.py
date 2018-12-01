
#!/bin/python
def is_user_exists(username):
    try:
        import pwd
        return(username in [entry.pw_name for entry in pwd.getpwall()])
    except:
        module.fail_json(msg='Module pwd does not exists')
        

def main():
    module = AnsibleModule(
        argument_spec = dict(
            username = dict(required=True)
        )
    )   
    username = module.params.get('username')
    exists = is_user_exists(username)
    if exists:
        status = '%s user exists' % username
    else:
        status = '%s user does not exist' % username
    module.exit_json(changed=True, msg=str(status))

from ansible.module_utils.basic import *
main() 
