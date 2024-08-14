# django-react-demo
Demo project for learning Django and React

## Django automatically creates required directory structure which we can use

[text](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)
for reference use above link

Steps -
Install Necessary Tools
Git: Download Git and install it on your machine.
VSCode: Download Visual Studio Code as your code editor.
Node.js & npm: Download Node.js (which includes npm) to manage React dependencies.
Python: Download Python for Django.
MySQL: Download MySQL and install it for your database

1) clone your repo:
git clone 
cd hackathon-project


2)Create a virtual environment:(in vscode)
python -m venv venv
source venv/bin/activate

3)Install Django:
pip install django

4)create new project:
django-admin startproject mysite


This will create a mysite directory in your current directory

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py


5)verify your Django project works:
python manage.py runserver


expected output:
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

August 08, 2024 - 15:50:53
Django version 5.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


6) create an app in your project(mysite):
python manage.py startapp polls(app name)

polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py


7)Write your first view:

in polls/views.py:

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


8) To access it in a browser, we need to map it to a URL - and for this we need to define a URL configuration, or “URLconf” for short. These URL configurations are defined inside each Django app, and they are Python files named urls.py.

To define a URLconf for the polls app, create a file polls/urls.py with the following content:

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]


Your app directory should now look like:

polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py



# Github steps to follow:

### 1. **Pull the Latest Changes**
Before you start working, ensure your local branch is up to date with the `main` (or `master`) branch from the remote repository.

```bash
git checkout main  # Switch to the main branch
git pull origin main  # Pull the latest changes
```

### 2. **Create a New Branch**
Create a new branch for the feature or fix you're working on. This keeps your work isolated from the `main` branch.

```bash
git checkout -b your-feature-branch
```

### 3. **Work on Your Code**
Make the necessary changes in your new branch. As you work, use `git status` to keep track of what has changed.

### 4. **Stage and Commit Your Changes**
Once you're happy with your changes, stage them and commit them with a meaningful message.

```bash
git add .
git commit -m "Describe what your changes are"
```

### 5. **Pull the Latest Changes Again**
Before merging, it's essential to ensure that your branch is up-to-date with any new changes that might have been pushed to `main`.

```bash
git checkout main  # Switch back to the main branch
git pull origin main  # Pull the latest changes
git checkout your-feature-branch  # Go back to your branch
git merge main  # Merge the latest main branch into your branch
```

Resolve any merge conflicts that arise, then commit the resolved changes.

### 6. **Push Your Branch**
Push your feature branch to the remote repository.

```bash
git push origin your-feature-branch
```

### 7. **Create a Pull Request (PR)**
- Go to the repository on GitHub.
- You should see an option to create a pull request for your branch. Click on it.
- Review the changes that will be merged, and make sure everything looks good.
- Add a descriptive title and comment about what your PR does, then create the pull request.

### 8. **Code Review and Merge**
- The pull request allows your teammates to review the code before it gets merged.
- If everything looks good, either you or someone else on your team can merge the pull request.
- After merging, make sure to delete your feature branch on both the remote repository and locally to keep the repo clean.

### 9. **Update Your Local `main` Branch**
After the pull request is merged, update your local `main` branch to reflect the changes.

```bash
git checkout main
git pull origin main
```

### Summary of Key Commands
- **Pull the latest changes:** `git pull origin main`
- **Create a branch:** `git checkout -b your-feature-branch`
- **Stage and commit changes:** `git add .` and `git commit -m "message"`
- **Merge main into your branch:** `git merge main`
- **Push your branch:** `git push origin your-feature-branch`
- **Create a pull request:** Through GitHub's web interface.

This workflow helps ensure that you don't accidentally overwrite existing code and allows for a smooth collaboration with your team.
