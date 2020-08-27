# SFIA-Project-2


Steps to run the program

On VM 1, you must install a few things to ensure that Jenkins will run everything properly.
The first thing is obviously Jenkins, without this a lot of the automated process becomes significantly less automated.
After that, you need to ensure that Ansible is installed so that you can run the Ansible playbook which ensures that the other machines have the appropriate software installed on them.
It's also important to install Pytest on VM 1. Since this is the only machine that will be running testing, I opted not to add it through Ansible, however that's a process that would be relatively easy to add should the need become apparent.