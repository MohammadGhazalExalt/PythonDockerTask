#!/bin/bash

ansible-playbook deploy-database.yaml
ansible-playbook deploy-app.yaml

