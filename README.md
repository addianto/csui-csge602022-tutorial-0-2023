# Tutorial 0

Sample content of the README.md:

```
Name: Rickey Astley

StudentID: 2206123456

Class: PBP International

Hobby: Not giving up

Major: Software Design
```

## Lab Notes

The following subsections provide several notes related to the tutorial.

### Object-Relational Mapping (ORM)

TODO: Revise the following draft

Tutorial 1's instructions told you to write the following code in [`models.py`](./main/models.py):

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
```

The `Product` class you just wrote represents the *data model* that will be stored into a permanent data storage such as a database.
The class represents the structure of your data, while later the instantiated object represents a record (or, row) of the data in the data storage.
Since most of you are also taking Database course, you can view the model in Django is similar to a database table.
The attributes you declared in the model class are, more or less, going to be mapped into a database table as the columns/attributes of the table.

Django, by default, uses a database called SQLite that stores the scehma and the records as a file in the filesystem. If you look at the project directory, you may see a file with `.sqlite` extension. It is the SQLite database file.
Later in subsequent tutorials, you will use another database system called Postgres that is running as a separate program. As a program, the Postgres may run on your local development machine or even on a different computer such as a remote server.
Remember one of the task in Tutorial 0 that mentioned about setting up a Postgres database on Adaptable?
The database you set up on Adaptable can be used by your deployed application for storing data.

### Project Directory Structure

As per the instructions for [initialising a Django project](https://pbp-fasilkom-ui.github.io/ganjil-2024/en/docs/tutorial-0),
you need to create a new directory called `shopping_list` on your local development machine.
You can place this directory anywhere in your local filesystem.
However, for the sake of clarity, we recommend creating the new directory in your home directory.

If you are using a Windows operating system (OS), your home directory can be found at `C:\Users\<your Windows username>\`.
For Mac OS or Linux-based OS users, the home directory is typically located at `/home/<your OS username/`.

For instance, if you are using `cmd` (Command Prompt) on Windows,
you can create the `shopping_list` directory in your home directory with the following commands:

```batch
cd %USERPROFILE%
mkdir shopping_list
cd shopping_list
```

Similarly, if you are using `pwsh` (PowerShell) on Windows, use these commands:

```pwsh
cd $USERPROFILE
mkdir shopping_list
cd shopping_list
```

On Mac OS or Linux, the commands are similar to the previous examples:

```shell
cd $HOME
mkdir shopping_list
cd shopping_list
```

By the end of the tutorial, your `shopping_list` directory under the home directory should have a structure resembling the following directory tree:

```shell
<your home directory>/
  <some files>
  <some directories>/
  shopping_list/
    .gitignore
    .git/
    env/
    shopping_list/
      __init__.py
      asgi.py
      settings.py
      urls.py
      wsgi.py
    manage.py
    README.md
    requirements.txt
```

### Password-based Authentication

For those who want to be able to use password-based authentication while performing `git push`,
you can create a personal access token and use it as a password during `git push`.
Follow these steps to create the token:

1. Open GitHub.com.
2. Go to your account settings - Developer Settings.
3. Choose Personal access tokens - Tokens (classic).
4. Generate a new token (classic).
5. Give it a name, e.g. `PBP` or any name you prefer.
6. Set the expiration to a reasonable period or select 'No expiration'.
7. Enable all repo scopes.
8. Click "Generate token."
9. Copy the generated token to a secure location. DO NOT SHARE IT AND ENSURE THE TOKEN IS NOT STORED IN ANY GIT REPOSITORY!
10. Try performing `git push` from your local repository again, and use the token as the password.

Alternatively, you can follow the recommended authentication suggested by GitHub.
That is, by using SSH-based authentication. It is more secure and more aligned with the best practices in the industry.
However, if you are using Git on GitHub from a network that blocking SSH (e.g., Hotspot UI),
you will need to use HTTPS-based authentication (password/token-based authentication).

### Python Packages and `requirements.txt`

The tutorial's instructions guide you to install several Python packages using `pip` command.
First, you write the name of each package's name in a file named [`requirements.txt`](./requirements.txt).
Then, you can install them using the `pip` command.

If you compare the list of Python packages in the tutorial instructions with the one in this repository,
you will notice a difference.
In this version, each package is **pinned** to a specific version.
The purpose is to ensure that we use consistent versions of each package in both the **development environment** (i.e., your local development machine) and the **deployment environment**.
While it might occur rarely, it is possible for an environment to install different version of a package from the one running on your local development machine if you had not pinned the version.
In some cases, it might be beneficial if the new version fixed certain issues (e.g., bugfixes).
However, there are also risks of introducing new issues into the project if it turns out the new version is not compatible with the project.
Therefore, we usually specify the version of each package in [`requirements.txt`](./requirements.txt).

### Ignoring Files From Git

We use a [`.gitignore` file](./.gitignore) to instruct the Git repository to avoid tracking changes in certain files.
Generally, the rule of thumb for ignoring files from being tracked by Git is to exclude files that are:

- Environment-specific, such as Python's virtual environment (usually in folders named `env`, `venv`, or variations of them)
  or configuration files created by an IDE (for example: Visual Studio Code's `.vscode` directory).
- Produced by a compiler, such as `.class` files produced by the Java compiler (`javac`).
- User-generated data, such as uploaded files and folders during local testing.
- Sensitive information, such as access tokens, private key files, and plaintext password files.

To assist you in creating the initial [`.gitignore` file](./.gitignore) for your project,
you can refer to the collection of [`.gitignore` files available on GitHub](https://github.com/github/gitignore/).
