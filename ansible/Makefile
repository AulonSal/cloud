# Install required ansible modules
# For the pacman and synchronize modules
ansible-install:
	ansible-galaxy collection install community.general

server-setup:
	ansible-playbook server_setup.yaml

steward:
	ansible-playbook steward.yaml
# ansible-playbook steward.yaml --ask-become-pass

