# SIG Chat bot

This chat bot is created for the exclusive use on the /SIG/ - Self Improvement General Discord server.
The bot is a community project where anyone can create a branch and work on any cool feature they want added to the bot.

This project is designed with beginners in mind, please feel free to contribute at any skill level. We will only be supportive and accommodating!

## Repository Details:

The entire project is coded in Python using the discord.py API. Bot tokens and api secrets are created and operated by the repository maintainers only.
When testing and developing please use your own API keys/secrets but then merge with the original place holder keys/secrets.

As this is a public and open source repository, please comment your code and ensure its readable. Uncommented code will be rejected.

Discord.py API reference: https://discordpy.readthedocs.io/en/latest/api.html

Discord API reference: https://discord.com/developers/docs/intro

SQLAlchemy ORM Documentation and Reference: https://docs.sqlalchemy.org/en/13/#sqlalchemy-orm

# Get started contributing!

Download git here: https://gitforwindows.org/

See how to use git here:
https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html#git-terminology
https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/

If you have any issues, use the tech channels on the server to ask questions!

To start working on the project, first you'll want to clone the repository.

```
git clone https://github.com/SmellyFilly/SIG-BOT.git
```

Then you need to initialise the clone as the local repository.

```
git init
```

Then add a remote repository.

```
git remote add upstream git@github.com:SmellyFilly/SIG-BOT.git
```

Create a branch for the context of what you're doing (bug fixing branch off master, creating a feature branch off develop).

Branch name example, creating a branch for a new extension: `feature/new-extension`

```
git checkout <branch name>
git pull upstream <branch name> && git push origin <branch name>
git checkout -b <new branch name (hotfix/feature)> <develop/master>
```

That will check you're on the respective branch, pull new changes from that branch and push syncs it locally. Then a new branch is created.
From there, do some work on the local git. Once completed, you will need to create a PR. This is when you push.

```
git add .
git commit -m "brief desc of changes"
git push -u origin <new banch name from before>
```

Then go on github, go to your branch and click "Compare & Pull Request".

This will create a review on your code with the maintainers of the repository. Then if approved it will be merged into master/develop then into master!

# Creating an Extension

To create an extension, you must first create the Cog Class.

```python
from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(CogName(bot))

```

From here, all your commands will be placed inside the class, using the decorator `@commands.command()`.
Before working on a feature please look through the other extensions to understand the structure of the code requried.

Refer to the discord.py API reference for more information on cogs/extensions (same thing but different).
