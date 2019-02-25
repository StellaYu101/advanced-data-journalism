  # Git assignment quickstart

  - **Step 1**: Create a folder on your desktop. Call it whatever you want, but for the purposes of this example, we'll call it `YOUR-FOLDER`.

  - **Step 2**: Go to your Github account page. Open the respositories tab and click the big green "New" button. Create a repository with the same name as `YOUR-FOLDER`. After filling out the forms, you should see a page with some instructions that looks like this:

  <img width="991" alt="screen shot 2018-09-12 at 8 21 45 am" src="https://user-images.githubusercontent.com/947791/45427975-d79ad200-b665-11e8-8565-f901ee7c8880.png">

  Take special note of the circled bit.

  - **Step 3**: Open a terminal window

  - **Step 4**: Type the following commands:

```
cd Desktop
cd YOUR_FOLDER
git init
git remote add origin https://github.com/YOUR-NAME/YOUR-FOLDER (from the circled line above)
git push -u origin master
```

  - **Step 5**: Create a text document inside your folder and write your assignment.

  - **Step 6**: Check your assignment into your repository with the following commands. Note that you **MUST BE INSIDE YOUR REPOSITORY FOLDER** for this to work:

```
git add .
git commit -m 'My assignment'
git push origin master
```

That's it! Let me know if you have any questions.
