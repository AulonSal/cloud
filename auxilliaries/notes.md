# Ansible Modules
- community.general.pacman
- community.general.synchronize wraps rsync, better than builtins.copy for dirs with a lot of files
- https://raymii.org/s/tutorials/Ansible_-_Only-do-something-if-another-action-changed.html
- https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html#selecting-or-skipping-tags-when-you-run-a-playbook
- filetree - it needs the dir to end with a / or else you get weirdo undefined behaviour, see code.

# Permissions
- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-centos-7
You don't need webserver's group for the python-webserver systemd service as uvicorn only supports a socket with permission 666
https://github.com/encode/uvicorn/pull/339
- How to test permissions
https://stackoverflow.com/questions/29244070/check-if-different-user-has-read-wrte-permissions-to-a-file-on-linux

# Uvicorn
- Does not create unix sockets if multiple workers.
https://github.com/encode/uvicorn/issues/428
Fine for now as the server only has one virtual core


