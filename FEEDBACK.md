## Feedback received from Invitae

**The Good**:
- Nice README, submission was well documented
- Included tests
- Definitely knows his way around Django, a plus for including tests

**The Concerns**:
- His loadtsvdata command didn't properly parse the variant data due to a Unicode error
- Tests didn't run due to conflicting tests module and package
- Concerns on command of Javascript, tough to evaluate front ends skills much from app. Disappointed that we had select something from a drop down, then still click a submit button.
- Questionable choice to use a form POST to redirect to the same page the form is on with a GET param added


## Personal Notes on Open Ended Takehome Assignment
- Unable to spend much time on entirety of project, probably 5-6 hours total. I only found out about assignment after the onsite interviews. I'm sure that made it appear less than "amazing" when compared to other candidates likely able to spend more hours. 
- In retrospect there were some less-than-optimal choices made regarding architecture, modeling, and functionality due to the time crunch. 
  - django-autocomplete-light was extremely helpful, but being that it was a POST request complicated what was intended to be a simple search flow. (The GET params added to the url were for ease of bookmarking/sharing.)
  - GenomicVariant had many fields that may have been better subclassed or combined. Not having much background in the field made it impossible to know all the terminology and relationships.
  - Basic Bootstrap is pretty bland, but it does allow for a quickly built, basic UI.
 
