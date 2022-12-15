# DIY Shadow

My Raspi installation at home which can power on my gamer PC upon receiving a specific message on a MQTT queue.

## Requirements

- A Raspberry Pi on Raspbian with Python3 installed and SSH access configured
  (not password access, only PublicKey since the first part of this Ansible playbook will disable the first).
- Python3 and Ansible installed on the control node (the host).

## Configuration

- The `inventory.yml` file contains the list of machines that will be configured by Ansible upon deployment.
- Export the *MOSQUITTO_USER* and *MOSQUITTO_PASSWORD* variables in the environment.
- Export the *WAKER_PC_MAC_ADDR* variable in the environment.

## Deployment

You can deploy it directly to the Raspberry Pi using Ansible.
The `run.sh` script contains the needed command to download everything Ansible needs and deploy.
