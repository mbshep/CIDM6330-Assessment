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

 6. I created models using my Domain Control diagrams. The final models are less complex than originally designed because I was trying to do too much (defining more of the system rather than just assessments and scheduling them)
 7. Ran makemigrations `code` py manage.py makemigrations
 8. then ran migrate `code` py manage.py migrate
 9. Start my redis listener in a separate terminal `code` py manage.py runworker assessments-add
 10. Now run tests `code` py manage.py test schdarch.tests.TestCommands

The tests copied from the Barky_Refactor_4 have been modified and implemented and run successfully in this project. I have ensured that at least one create, read, update and delete test work for the Assessment model. Similar tests should be easily implemented for the Sched and Assessor models with these tests as guides. 

I had trouble getting the edit test to run. It was calling update_from_domain() and throwing what you described as a null error meaning the item was empty. The update was being made based on the csv and WORKER terminal being updated. I thought maybe it was because the update_from_domain() included calling the save() method and therefore the item no longer existed. I switched to the to_domain() method to see if that made a difference and it did not. Therefore I did not call either of those methods and instead re-called the add method. This method worked. I had done some research to see that there is not a Django update() method - there is only the save() method and Django determines if it needs to do an insert or an update. With this knowledge I left the code that updated one or more fields directly in the domain object and then called the add method again. Based on the test outcome the update was successful.

I had trouble getting the Injector application to run. I did not ever install it using pip. I assume it would work if I did that. I chose to comment it out instead because I do not need or use the time field that we were using it for.

Ideally the Channels implementations would be used to send notifications or emails to interested parties anytime an assessment is updated.
