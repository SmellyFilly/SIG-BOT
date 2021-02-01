# SIG Chat bot

This chat bot is created for the exclusive use on the /SIG/ - Self Improvement General Discord server.
The bot is a community project where anyone can create a branch and work on any cool feature they want added to the bot.

This project is designed with beginners in mind, please feel free to contribute at any skill level. We will only be supportive and accommodating!

# Get started contributing!

Download git here: https://gitforwindows.org/

See how to use git here:
https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html#git-terminology
https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/

If you have any issues, use the tech channels on the server to ask questions!

To start working on the project, first you'll want to clone the repository.
`git clone https://github.com/SmellyFilly/SIG-BOT.git`

Then you need to initialise the clone as the local repository.
`git init`

Then add a remote repository.
`git remote add upstream git@github.com:SmellyFilly/SIG-BOT.git`

Then do some work on the local git. Once completed, create a branch for the context of what you're doing (bug fixing branch off master, creating a feature branch off develop).
`git checkout <branch name>`
`git pull upstream <branch name> && git push origin <branch name>`
`git checkout -b <new branch name (hotfix/feature)>`

That will check you're on the respective branch, pull new changes from that branch and push syncs it locally. Then a new branch is created.
From there, you will need to create a PR. This is when you push.
`git push -u origin <new banch name from before>`
Then go on github, go to your branch and click "Compare & Pull Request".

This will create a review on your code with the maintainers of the repository. Then if approved it will be merged into master/develop then into master!
