To do:

Current issues:
-THOUGHT: Are you spending too much time trying to provide options to edit, etc.? Should you just move forward with "create plan and use plan" functionality, knowing that you can build more on top of it...or build alternative using React???? What if this app looks like:
        -You can build a custom plan from scratch
        -You can use a prebuilt 16-week starter plan
        -You can track your weekly miles
        -You get recognition for meeting milestones along the way
        -You can delete your plan when finished
        And that's it for now! Later on, we can...
        -Edit custom plan
        -Edit starter plan
        -Create and save multiple plans
        -Align to calendar dates
        -Get weekly prompts/reminders/kudos
        -Share progress with others
-Consider allowing edit by specific day only...generating weekly data in form to edit is proving challenging
-Make sure **update** is not adding new Week/Day (need to access id for these, instead of num)
-Improve UI of training plan!!! (look at container spacing...too much L/R padding or margin?)


Next issues:
-TODO: if a new user logs in and clicks "see my training plan," they need to be redirected to set up a plan
-weekly view shows 'miles completed' and 'miles remaining' but there's no script for calculating/updating this
-edit miles route needs fixing; also need to add option to edit num_weeks??? (may need to force delete/create new plan)
-Control of view based on auth (welcome screen, login/logout btns, ...?) including navbar links and 'Do it' button
-Add more options to navbar(for logged in users)
-change input type back to integer (floats look messy & confusing; also unnecessary)
-UI markup for completed miles (currently just changes text to red)
-Provide option for user to clear plan and start over



Resolved (I think) :
-navbar styling
-landing page button styling
-Working on daily miles form and displaying correctly in my training plan
-Add login link (temporary)
-From training plan to weekly-view, current week is correct but it reverts to week 1 when adding miles
-Adding to DB something is wrong. days.weeks is supposed to access weeks.id as foreign key, but it seems to have just added a new id...THIS IS PROBABLY BECAUSE YOU DID session['curr_week'] + 1 AND NEVER UNDID IT WHEN SWITCHING TO PLAN!
-change password input type to "password" in wtforms so it isn't visible when typing
-Welcome page styling
-When logged in as new user, "This is week X" of daily-miles-form shows week 1 for every week and keeps adding new blank form (doesn't stop when reaches final week). However, DB seems to be accurate (for weeks only...nothing showing up for their days)
-Set default values for default plan (finish this)
-when using starter plan, daily miles not showing in weekly view...curr-week variable not available...may just need to add code from setup plan to fix this

Functionality:

        -Add functionality to mark off miles as completed & subtract from miles remaining: need event to click {day.mileage_target} object; then subtract this from that # and/or add to {day.miles_completed}...what makes sense here?
                -also need to link these miles completed so they are reflected in {week.miles_completed} and {week.mileage_target} and {total}
                -would be nice to offer a way to not just click complete or not, but to adjust the number of miles for a partially completed distance

        -Add ability of user to change details of plan (num weeks, miles any given week or day)

        -Add simple math checking (do your daily miles add up to weekly? Do your total miles add up to 26.2?)

        -May want to use SelectField for numMiles, etc. ... however, these will automatically convert to strings, so will need to use coerce function to force them to be integers (i.e. coerce=int goes as 2nd argument...see the docs)

        -Change 'daily miles' and 'update daily miles' to WTForms
        ---- Proving to be very difficult! Leaving as is for now because it works...follow up later


UI/UX:

        -Sketch design mock-up for each page

        -Add css styling
        
        -Add visual progress tracker thingy

        -Create a demo login

        -Add celebrations for milestones completed (badges, confetti, etc.)

        -Bonus: integrate API calls for motivational quotes/images


Attributions:

photo on homepage:

Photo by <a href="https://unsplash.com/@amutiomi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Miguel A Amutio</a> on <a href="https://unsplash.com/s/photos/marathon?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
  
  

