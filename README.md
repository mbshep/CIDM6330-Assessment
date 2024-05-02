# CIDM6330 Assessment

 Assessment Scheduling Project

 I started with the code from the Barky Refactor 4

 I needed to change bookmarks to assessments and add scheduling the assessments.

 1. I created a virtual environment `code` py -m venv mbsloc
 2. Activated the virtual environment `code` source ./mbsloc/Scripts/activate
 3. Installed requirements `code` pip install -r requirements.txt
    - I had to stop Norton from stopping pip doing it's job - I had to exclude the pip process
    - I also installed redis `code` pip install channels-redis
 4. Created project assess_sched and apps schdling, schdapi and schdarch
 5. Copied code from djbarky to these apps one file at a time. Changed djbarky to assess_sched

- Project is called assess_sched
- Apps are called
  - assess_sched
  - schdapi
  - schdarch
  - schdling - I don't think this is used at all

 6. I created models using my Domain Control diagrams. The final models are less complex than originally designed because I was trying to do too much (defining more of the system rather than just one or two things)
 7. Ran makemigrations `code` py manage.py makemigrations
 8. then ran migrate `code` py manage.py migrate
 9. Start my redis listener in a separate terminal `code` ./manage.py runworker assessments-add
 10. Now try to run tests `code` ./manage.py test stdarch.tests.TestCommands
