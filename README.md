# Machine-Learning-Project

# Software and Account Requirement
1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


                                                                                                                                                                                                  creating conda environment
                                                                                                                                                                                                                                                                    conda create -p nenv -y                                                                                                                                                                                                                                                                                                                                                                                        
pip install -r requirements.txt

pip install Flask

To  ADD files to git
...

git add

git add <filename>


note : to ignore file or folder from git we can write name of file/folder in .gitignore file

to check the git status
...
git status

To create version/commit all changes by git
...

git commit -m "message"
...
to send changes/version to github 
...



git push origin main
...

to check remote url
...
git remote -v
...


To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = saritha.jce@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression4590-app


BUILD DOCKER IMAGE
......
docker build -t <image_name>:<tagname> .d
....

>Note: Image name for docker must be lowercase

To list docker image
...

docker images
...

Run docker image
...
docker run -p 5000:5000 -e PORT=5000 
To check running container in docker
...
docker ps
...

To stop docker container
....

docker stop <container_id>

....
python setup.py

install ipykernel
....
pip ipykernel
...

....
yaml

install pyyaml

...

Data Drift:
When your dataset stats gets change we call it as data drift

If no difference two  dataset it means there is no data drift

if there is huge difference between datatets it is called there is data drift

library used is
 evidently

 pip install evidently

