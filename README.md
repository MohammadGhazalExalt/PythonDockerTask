# PythonDockerTask

This repository is for a flask application that reads details about linux system and stores them in a database

1. On your Manager machine , first you will need to install **epel-release**:
```bash
sudo yum install epel-release
```

2. Now we need to install **ansible**:
```bash
sudo yum install ansible
```

3. Navigate to **ansible** directory in **/var/etc**:
```
cd /var/etc/ansible
```

4. In the hosts file, add two groups: **\[application\] and \[database\]** and add your machines IPs to them:
```
[application]
*IP ADDRESS*

[database]
*IP ADDRESS*
```

5. Add files under the directory **manager** in the repository to the **ansible** directory in your machine

6. Run the code inside deploy-machines.sh
```
sh deploy-machines.sh
```


