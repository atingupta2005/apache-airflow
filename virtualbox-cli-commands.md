```
vboxmanage list vms
VBoxManage controlvm master  poweroff
VBoxManage modifyvm "master" --natpf1 "http1,tcp,192.168.219.2,8080,192.168.219.2,8080"
VBoxManage startvm ubuservloc --type headless
```
