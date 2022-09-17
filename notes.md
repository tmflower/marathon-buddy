To do:

Current issues:
-Working on daily miles form and displaying correctly in my training plan
-Adding to DB something is wrong. days.weeks is supposed to access weeks.id as foreign key, but it seems to have just added a new id...THIS IS PROBABLY BECAUSE YOU DID session['curr_week'] + 1 AND NEVER UNDID IT WHEN SWITCHING TO PLAN!
-From training plan to weekly-view, current week is correct but it reverts to week 1 when adding miles
-I believe these are all fixed

Next issues:
-Change daily miles and update daily miles to WTForms
-Make sure update is not adding new Week/Day (need to access id for these, instead of num)
-Add login link (temporary)
-Set default values for default plan

Functionality:

        -Add functionality to mark off miles as completed & subtract from miles remaining: need event to click {day.mileage_target} object; then subtract this from that # and/or add to {day.miles_completed}...what makes sense here?
                -also need to link these miles completed so they are reflected in {week.miles_completed} and {week.mileage_target} and {total}
                -would be nice to offer a way to not just click complete or not, but to adjust the number of miles for a partially completed distance

        -Add ability of user to change details of plan (num weeks, miles any given week or day)

        -Add default values for weekly miles (can do in WTFORMS?)

        -Add simple math checking (do your daily miles add up to weekly? Do your total miles add up to 26.2?)

        -Add a default 16-week plan (use the one I'm using)...how does this work? Where do the defaults live? Maybe I use a seed file and somehow import that when they choose it?


UI/UX:

        -Sketch design mock-up for each page

        -Add css styling
        
        -Add visual progress tracker thingy

        -Create a demo login

        -Add celebrations for milestones completed (badges, confetti, etc.)

