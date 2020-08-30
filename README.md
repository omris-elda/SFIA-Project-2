### SFIA-Project-2
# D&D Character Generator

## Base Requirements
---
For this project we were tasked with creating an app with four services which can all communicate with each other, and to deploy it using Docker and a Jenkins pipeline, as well as a few other technologies.\
To fulfil these requirements, I decided to make a D&D character generator, that randomly assigns the user a race, class, and attribute points, as well as displaying the race/class related traits and adding attribute points where required.\
## Technologies Used
---
Ansible\
Docker\
Docker Compose\
Docker Swarm\
Docker Stack\
Flask\
Git / Github\
Jenkins\
Pytest\
Python\
## Architecture
---
The database that I used in this program was quite simple, with just three tables, and I created a fairly simple ERD to display the values that would be entered into each table and how they are going to be linked.\
<-- insert erd here --->
Initially I did not have the created models table, which meant that my tables were even simpler, with no relationships at all!\
<-- insert simple erd here -->
## Deployment
---
The deployment of my program was mostly done using a Jenkins pipeline. This pipeline has three main steps; build, test, and deploy.\
The build section of the pipeline ensures that the swarm VMs have the appropriate software installed, and that they're correctly connected to the swarm. It also builds the dDcker images from the Dockerfiles in the app folder, using Docker compose to streamline the process. These builds are then pushed to Docker Hub so that I can retrieve them at my convenience later.\
The testing section does exactly what you'd expect it to, it goes through all of the individual services and runs tests on them to ensure that they work as they should. Using Pytest I was able to get a minimum of 90% coverage with my testing, and much of the code that was missed was only missed because it wasn't actually used in the program, and was only there in case the client wished to expand upon the functionality of the application. These include (but are not limited to) the functions to lower attribute points, and the functions to view the attribute points.\
The deploy section is also fairly self-explanitory. It deploys the application using Docker stack, which will allow the application to be deployed over serveral different VMs, using the images that we pushed to Docker Hub earlier, so long as they are all connected to the same Docker swarm. This means that there is less chance of the whole program crashing, as if one node goes down Docker will automatically re-deploy the containers to other VMs.\
<-- CI pipeline goes here -->
## Steps to run the program
---
On VM 1, you must install a few things to ensure that Jenkins will run everything properly.
The first thing is obviously Jenkins, without this a lot of the automated process becomes significantly less automated.\
\
After that, you need to ensure that Ansible is installed so that you can run the Ansible playbook which ensures that the other machines have the appropriate software installed on them.\
It's also important to install Pytest on VM 1. Since this is the only machine that will be running testing, I opted not to add it through Ansible, however that's a process that would be relatively easy to add should the need become apparent.\
The Jenkins script will then run through the process of building, testing, and deploying the program, as explained above.\
## Testing
---

## Current Bugs
---
Currently the Nginx container doesn't always deploy to every single Swarm node, meaning that if I try to connect to the website through some of the nodes it won't always work. A way to fix this would be to have Nginx running as a separate service on a dedicated VM, so that that was always the entry point for the application. This is something that can be implemented in a later build.\
## Future Additions
---
In the future it'd be nice to add a function that allows you to build a full character sheet, including inventory. It'd also be nice to be able to upload pictures of your characters (should you so desire), and have images for the various races and classes. It'd also be beneficial to have a delete function so that you can delete the randomly generated character should you so desire, as well as making sure that there's no duplicates in the database, so that the database doesn't get clogged up.\
Another feature that would be a good addition is that with some classes/races, you get a +1 or +2 to some attributes, which are currently hard coded to be added to specific attributes, instead of randomly assigning them as it should be. This shouldn't be too difficult to solve, a simple rng would be able to fix this. I'd also like to assign attributes the correct way, which is to roll 4 d6 and ignore the lowest one, whereas at the moment I'm just rolling 3 and getting to total from there.
## Acknowledgements
---
CA for teaching me the skills required to create this project.
My cohort and instructors for their continued support.
## Author(s)
---
Ed Pricket (Coding, Design, Implementation)
DnD Beyond (Class and Race information)