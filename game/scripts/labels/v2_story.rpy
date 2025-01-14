label v2_working_late:
    show oliver
    oliver @ smile "[player_name]! Did I catch you before you wrapped up work for the day?"
    player smile "No, I haven't wrapped up work yet! What can I help you with?"
    oliver "So, you know that new client, Stacy & Lucy's?"
    player "Yep - the bridal boutique chain?"
    oliver "That's the one! I just got off of the phone with them earlier, and they're wondering if it'd be possible for you and the rest of the team to shoot for a closer completion date?"
    player surprised "A closer date?"
    player worry "I mean - "
    player "What do they have in mind? We have them slated to be finished next week."
    oliver @ neutral "So - "
    oliver "and this is going to sound a bit crazy - "
    oliver " - they need their e-commerce system completed within the next two days."
    player surprised "T... TWO days?"
    oliver "Yeah, they were pretty insistent on the phone. The only thing that's left is user authentication. Do you think you can work something out?"
    player pout "Um..."

    menu:
        "I'm pretty sure this will take more than two days.":
            player "I'm not so sure that's possible, Oliver. We have other projects that we have to make sure we complete on time."
            oliver "Hey, I totally understand. It's just that Brian says all they need is some kind of authentication setup completed. That shouldn't take you more than two days, right?"
            player neutral "I mean... do they want something custom built, or are we using an existing service like Auth0?"
            oliver "Let me check my notes here... Yep - it says they'd like something custom. But we've rolled something like that out before, right?"
            oliver "Last year, Brian knocked something like that out in 3 days. I bet you could if you pushed!"
            player "Well..."

            menu:
                "(I'm still not sure about this. We should talk to the client a bit more.)":
                    player "Can we inform the client of the pros and cons of their decision for custom authentication? I don't think that we should just say yes without talking about this more."
                    oliver "I spent about an hour on the phone with them this morning. I'm pretty sure that they won't budge."
                    oliver "Maybe you could get this done if you pushed a bit? I've been staying late to finish up with clients quite a bit this week - if you and the team do that, I bet you could get Stacy & Lucy's e-commerce setup completed in time!"
                    oliver "I can even talk you up to Iris if you get this finished on time. I bet she'll love the fact that you pulled the team through this and made a client really happy."

                    menu:
                        "I think we need to consult with Goro about this first.":
                            player "I think that we need to consult with Goro about this first. He's our team lead, and would understand what our commitments are looking like the best."

                            show goro at left with moveinleft
                            goro @ smile "What's this that Goro will know how to do best?"
                            oliver "Goro! Just the person we wanted to see!"
                            "You step aside a bit and let the two of them converse, paying attention closely."
                            "Goro offers to hop on a call along with Oliver to give a technical perspective on the project, and work out a timeline and some technical solutions that are more realistic based on the timeline that the client has asked for."
                            "By the time the two of them are done speaking, they've booked a meeting with the client for tomorrow morning. Oliver seems satisfied with this outcome, and says his goodbyes, excited to have some backup."
                            player smile "Thanks for the help, Goro! I wasn't sure what the right thing to do in that situation was."
                            goro "Don't worry, you definitely did the right thing. It's best to not make split-second decisions and commitments on development projects, especially when we have other clients in line to get their projects done, and when your decision affects the whole team."
                            goro "You should always come to a senior developer just like you did to get a second opinion when you're unsure of a commitment you're being asked to make."
                            player "Thanks! I'll make note of that."
                            "You've earned 20 renown for your responsible decision-making."
                            $ player_stats.change_stats(RENOWN, 20)

                        "Maybe I could stay a little late. Okay.":
                            call v2_working_late_sad_path from _call_v2_working_late_sad_path

                "(Am I just a slow developer? If Brian could do it back then, I probably could too! I can do this.)":
                    call v2_working_late_sad_path from _call_v2_working_late_sad_path_1

        "Sure. I've been getting more comfortable in my duties here! I can probably work something out.":
            call v2_working_late_sad_path from _call_v2_working_late_sad_path_2
    return

label v2_working_late_sad_path:
    oliver @ laugh "That's the spirit! You're a great developer. I'm sure you can get this done in no time!"
    player laugh "Yeah! This can't be that hard, can it?"
    oliver @ smile "Just let me know if you have any questions. I'll shoot you the information on the project when [missing text?]"
    "You sit down at your desk, and take a look at the JIRA logs for the project. Everything seems to be just as Oliver describes."
    "Suddenly, Oliver sends you a ticket number for the change. Once you open it, you suddenly lose your confidence."
    "You request the authentication ticket that Oliver mentioned Brian completing a few years ago. It doesn't help - there are almost no comments in his code."
    "Even if there were, the project is done in a completely different language and framework that you don't know yet."
    player worry "Jeez... how am I supposed to get this done in two days? Now that I think about it, I don't know the first thing about building a custom authentication system."
    "You spend almost the entirety of the first day looking at videos and StackOverflow posts to even find out where to begin rolling out your own authentication system."
    "Every comment on every forum disagrees with the others, citing their own way of writing an authentication system that's supposedly best."
    "You look up at the clock and notice that it's 6PM. Exhausted, you decide to take a break."

    show goro with moveinleft
    goro "[player_name]? What are you doing here? It's 6PM, you should probably be packing up."
    player pout "Hi Goro. I can't - I promised that I'd work to get the Stacy & Lucy's project finished in time."
    goro "But that's due a week from now?"
    player "Well, not since I talked to Oliver earlier, and he said that S & L insisted that it was super important for us to get it done within the next two days."
    goro "Two days? [player_name], I don't think that's possible."
    player neutral "I'm beginning to get that now... but I already promised I'd get this done. What should I do?"
    goro "I'll talk to Oliver. What will probably happen is that I'll hop on a call with him and the client and help him explain that we won't be able to do what they're asking within this shorter period of time."
    goro "If they'd like to to get their project done in two days, we're going to have to cut a lot of corners, and they need to understand that."
    player "I see."
    goro "Next time, I'd like you to reach out to me whenever a big commitment change like this is requested."
    goro "This decision doesn't just affect you, but the entire team, and all of our client projects that are further ahead in the pipeline."
    goro "Other clients that have been waiting longer than S & L might get their projects completed late if we put all of our time and resources into one account without having meetings to work it into our schedule."
    player "I'm sorry, I didn't think about that."
    goro "It's okay. For now, you might want to get home. Tomorrow, just continue with the other tasks we have in the pipeline for this week."
    "You lose 10 Renown for not discussing your decision with your team lead, and 15 Energy for a stressful 7 hours of searching the web for answers."
    $ player_stats.change_stats(RENOWN, -10)
    $ player_stats.change_stats(ENERGY, -15)
    return

label v2_help_from_friends:
    show mala
    mala "*Grumble grumble*"
    player smile "Hey Mala! How's your day been?"
    mala "Hello, [player_name]. I wish my day were going better."
    player neutral "Did something happen? You look pretty upset."
    mala @ angry "Ugh, I am! It's this bug. I've set everything in this React component up correctly, and it's still not working."
    player "I see. About how long have you been working on it?"
    mala "For around two hours. I've checked and re-checked my code and looked into similar tickets we've completed in the past, and I just can't figure out what's wrong."
    player "Is there some way that I can help?"
    mala @ neutral "(Sigh) I'm really not sure."
    player "(Wow - I guess even mid-level developers get stuck on programming problems and bugs just like I do.)"
    player pout"(I really hate to see Mala so frustrated. There's got to be something that I can do...)"

    menu:    
        "Ask for Mala to explain the problem from the beginning and take notes.":
            player "I'm sorry to hear that you're having a hard time. Could you tell me all about the problem step by step?"
            player "I can maybe even take some notes?"
            mala "Hm... Maybe that's not such a bad idea. You can be my rubber duck!"
            player surprised "I'm sorry, your what?"
            mala @ smile "A rubber duck! I left mine at home, but it'd be great if you could stand in for it."
            player "Sorry, but what do bath toys have to do with programming?"
            mala "Rubber Duck Debugging is when a developer slowly goes over their code, line-by-line from the beginning, and explains it."
            mala "Explaining the code aloud like this can help with finding an error that the developer may not have noticed at first."
            mala "Normally, this is done with a little rubber duck or object that some developers keep on their desk. When there's no duck, a coworker will usually do the job just fine."
            player smile "Haha, that sounds fun! I'd be glad to stand in for your duck."
            "Mala begins to explain her code line by line. You nod and listen politely."
            "She's halfway through explaining her code when she suddenly stops."
            mala @ neutral "So, this next line is here because... um... "
            player neutral "Hm?"
            mala "Y'know, I'm not really sure what this line does, now that I think about it. When did I write this here?"
            player "Did you leave any comments or notes anywhere about it?"
            mala "No - I really need to comment my code out more often. Then we wouldn't be in this situation! I'll try to delete the line."
            mala "..."
            mala "Okay! So we've got good news and we've got bad news."
            player "Should we start with the good news?"
            mala "Sure. The good news is, the bug that I was dealing with earlier is gone!"
            player "That's great! And the bad news?"
            mala "The bad news is, we have a NEW bug. "
            player smile "Uh - That's progress, right?"
            mala @ smile "It definitely is! Another good thing is that I have an idea of how to solve this bug - a lot more of an idea than how to solve the last one!"
            mala "Thanks for being my rubber duck. I'm not sure that I would have been able to come up with a solution if I didn't get another set of eyes on it!"
            player "That's no problem! Who knows? Maybe I'll give Rubber Duck Debugging a try in the future too."
            mala "I'd be honored to be your duck!"
            "You gain 5 Renown for being a helpful rubber duck."
            $ player_stats.change_stats(RENOWN, 5)
    
        "Request help from a manager.":
            player neutral "She seems a bit deep into her work now. I probably shouldn't disturb her."
            player "Maybe I can ask for help for her! Annika told me that I should always ask for help when I'm stuck on a problem. "
            player "I'll go grab a manager for her so she doesn't have to stop what she's doing."
            hide mala

            show goro
            goro "..."
            player smile "Hey Goro! "
            goro "Hi [player_name]. Can I help you with anything?"
            player neutral "Actually, it's not help for me, but for Mala!"
            goro "Mala? What's going on?"
            player "She's stuck on this bug, and has been for about two hours. She can't figure out why her React component isn't firing off GET requests."
            goro "..."
            player "Goro? Do you not know what's wrong either?"
            goro "It's not that so much as it's the fact that you came to me about someone else's problem."
            player "What do you mean?"
            goro "I know that you're probably intending to help your coworker, but we're all adults here."
            goro "Mala is a very smart, capable developer. She knows to ask for help when she needs it. Sometimes we just have to crack at a problem for a while."
            goro "More importantly, if you went to a manager that maybe didn't have a good relationship with Mala, reporting this sort of thing could get her in trouble."
            goro "Not only that, but it can make her think that you don't think that she's capable of doing her job."
            player pout "Oh no! That's the last thing I'd want her to think! I learn so, so much from her."
            goro @ smile "I understand that. Just try to be a bit more aware in the future."
            player "I understand."
            player "(Oh my gosh. This is so embarrassing!)"
            "You lose 10 Renown."
            $ player_stats.change_stats(RENOWN, -10)
    return

label v2_eta:
    show goro
    goro "Hi [player_name] - how's that ticket for the GoGoGames account coming?"
    player "I actually haven't gotten to work on it yet; I'm still finishing up that ticket on the town hall website. Is that okay?"
    goro "Sure! I'm glad that you're getting that done as well. I just wanted to know if you've gotten a chance to look at the ticket yet?"
    goro "I just wanted to make sure that it was something that you're comfortable with."
    player "Sure! I've never worked with Flask before, but I've worked with MVC frameworks in the past. It's definitely doable."
    goro "Great! "
    goro "That said, do you think that you can give me a time estimate?"
    player "A time estimate?"
    goro "Yep! I have a call with that client later today, so I figured I'd give them an estimate on when the backend of their project will be complete."
    player "Hmm... Well..."
    player "(I'm pretty sure that this project can be completed in a day or two; All they want is a website with routes, and we'll expand on the backend functionalities later.)"
    player "(So in truth, their set up should be pretty quick, once I grasp the basics of Flask.)"
    player "(But on the other hand, I have other tickets I need to work on. What should I do?)"

    menu:    
        "Be ambitious - I should be able to finish in 2 days!":
            player "Hm... well, from what I remember about the ticket, it doesn't seem too hard. "
            player smile "I bet I can knock this out in two days!"
            goro "..."
            goro @ laugh "Hahaha! Bold, aren't you?"
            player "Sure! I'm pretty sure that I can handle this. I'll just have to stay a little late for a day or two."
            player "But it's only a day or two!"
            goro @ neutral "Ambition can definitely be good. But in all seriousness, just know that you shouldn't make a habit of this sort of thing."
            goro "Your work-life balance is really important, and if you don't take care of yourself, you'll burn out and not produce the best work that you can."
            goro "Between you and me, it's sometimes better to give yourself a few extra days beyond what you actually think it'll take to complete a project."
            goro "Like you said, you never know if you'll hit some snags while working on your project. It also leaves room for other development emergencies on other projects if they come."
            goro "Like I said, it's awesome that you want to prove yourself here. But are you sure you can handle your other assignments?"
            player "You have my word! I'm going to knock this ticket out of the park."
            goro "Okay then! In that case I'll see you tomorrow. I need to get home. Good luck!"
            player "Thanks Goro. See ya later!"
            player "..."
            player neutral "(Sigh). Okay. Let's get started."
            "You gain 15 renown for completing your project early! But lose 20 Energy as a result of pushing yourself."
            $ player_stats.change_stats(RENOWN, 15)
            $ player_stats.change_stats(ENERGY, -20)
    
        "Be conservative - We should tell them I need a week, just to be safe.":
            player "Hm... well, from what I remember about the ticket, it doesn't seem too hard. "
            player "But I want to make sure that all of my other tickets for this week get completed. I could also run into a bug or two while I'm working on it!"
            goro @ smile "Playing it safe, I see. Not a bad idea."
            goro "Between you and me, it's sometimes better to give yourself a few extra days beyond what you actually think it'll take to complete a project."
            goro "Like you said, you never know if you'll hit some snags while working on your project. It also leaves room for other development emergencies on other projects if they come."
            player smile "Right! This way, I feel like I'll be ready for anything that comes up."
            goro "Rock on. I'll give the client the update. Thanks [player_name]."
            "You gain 10 Energy knowing you'll have plenty of breathing room to complete all your duties this week."
            $ player_stats.change_stats(ENERGY, 10)
    return

label v2_motormouth:
    player "Phew - I've really been on a roll today! It's 3PM, and I've already finished all of my tickets. I'm super thirsty!"
    player "I think I see Mike from marketing over at the water cooler. I should say hi!"
    player smile "Hi Mike! What's new with you?"
    mike "[player_name]! Not much - how was your weekend?"
    "The two of you converse politely for a while about non-work related topics. It feels great to keep things casual!"
    "You're so relaxed, in fact, that you gain 10 Energy!"
    $ player_stats.change_stats(ENERGY, 10)
    "You take a look at the clock and notice you've been standing around for 10 minutes."
    "You suddenly remember an office rumor you heard in passing – Mike is probably the nicest guy in the office, but he's really, really... “chatty”."
    "What was that nickname they gave him? Something about cars?"
    motormouth_mike "So anyway - have you been watching Star Girl Galactica?"
    player laugh "(Gasp)! I love Star Girl Galactica! It's my favorite show! But didn't that show come out in the early 2000s?"
    motormouth_mike "No way - you don't know about the remake? They remade the show with modern effects and CGI!"
    motormouth_mike "Who's your favorite character?!"
    "You can't believe your ears right now! You want to learn more, but you also want to get back to work."
    "BUT, talking with Mike seems to be doing good things for your Energy. Should you stay and talk about Star Girl Galactica?"

    menu:    
        "A few more minutes won't hurt.":
            player smile "I heard there was a new game, but I thought it was just a new version of the 2003 game with better graphics!"
            motormouth_mike "Nope - this is a totally new game based on the new TV series! It's a 3D Open World game."
            player surprised "No way! Are they going to bring back that one item that gives you invincibility?"
            "The two of you talk a bit longer and exchange war stories on your struggles with the original game."
            "You have so much fun guessing what features are going to be in the new game that you gain another 10 Energy."
            "You look up at the clock and notice another 10 minutes has gone by."
            motormouth_mike "So what's super cool is that if you watch the trailer for the new game, they use that new Quinn C. Larkson song, From the Ground Up."
            player "What?! You like Quinn C. Larkson too?"
            motormouth_mike "Who doesn't? What's your favorite song? Mine is Cruising for A Musing!"
            "The two of you even like some of the same music? The coincidences don't stop!"
            $ player_stats.change_stats(ENERGY, 20)
            "But you've been chatting with Mike for a while now. It's so much fun, but maybe you should get back to work?"
            "Or maybe you should keep the ball rolling? You haven't felt this relaxed in some time (maybe you should get out more?)."
            "What will you do?"

            menu:
                "A few more minutes won't hurt.":
                    player smile "Hm... I'd have to say my favorite song is probably Never Not Favored, but I also really love Chasing That Feeling!"
                    show iris
                    iris "I'm more of a Scratching the Surface kind of gal myself."
                    player surprised "Iris!"
                    motormouth_mike "M-Ms. Benson! Good morning!"
                    iris angry "It's afternoon at this point. I've been watching the two of you talk for, oh... 30 minutes now."
                    iris "Mike, don't you have work to do? The big presentation for Walter Co. Construction is due tomorrow."
                    motormouth_mike "Sure do! That's my cue - later [player_name]!"
                    player neutral sweat "Bye Mike. Whelp, I better get going, too -"
                    iris "Not so fast. What are you doing? "
                    iris "Do we have a “Loquacious [player_name]” to match Motormouth Mike now?"
                    player -sweat "Mike's always hanging out at the cooler, so I figured it would be okay to take a bit of a break..."
                    iris "A break is fine, but if you stand around for too long, it'll begin to look like you haven't done much work."
                    iris "Think about it - Mike's been at this company for 5 years. He shouldn't be doing it, but at least he has tenure here. But a brand new junior?"
                    iris "It's not a good look. Do you understand?"
                    player "Yes..."
                    iris "Good. Get back to work."
                    "You gained 30 Energy, but lost it all, and an additional 10 Energy for your trouble."
                    $ player_stats.change_stats(ENERGY, -30)
                    $ player_stats.change_stats(ENERGY, -10)
            
                "I should get back to work":
                    player smile "Sorry Motormou - I mean, Mike. I'm a big Quinn C. Larkson fan, but I have a few projects that I have to get back to."
                    motormouth_mike "No problem dude! I'll catch you at the water cooler later. Go home and watch the trailer so we can geek out about it next time!"
                    player "Will do!"
                    "Total Energy gained 30 points."
    
        "I should get back to work":
            player smile "Sorry Motormou - I mean, Mike. I love video games as much as I love Star Girl Galactica, but I have a few projects that I have to get back to."
            motormouth_mike "No problem dude! I'll catch you at the water cooler later. Go home and watch it and we can chat about it!"
            player "Will do!"
            "Total Energy gained 10 points."
    return

label v2_message:
    show darius
    darius "[player_name]! Do you have a moment?"
    player "I do! What's going on?"
    darius "I could use a little bit of help with this React bug? I've been stuck on it all morning."
    player "Sure! I'm a junior too, but I'll do the best that I can."
    player "..."
    player surprised "Oh! "
    darius @ confused "Do you know how to fix it?"
    player neutral "Not entirely, but this is something that Goro and I ran into yesterday!"
    player "We could try to debug it ourselves but he and I were at it for about 2 hours."
    darius @ neutral "That's no good! The Product Team has been asking for this for a while."
    player "I'll just shoot him a quick message."
    player "Hm... it seems like he's in a meeting."
    darius "Oh - should we wait?"
    player "Well..."

    menu:
        "Shoot him a quick message":
            player "I mean... it's a QUICK message. This is time-sensitive, right?"
            darius "Definitely!"
            player "Let me just shoot him something really quick."
            scene bg company1_breakroom with blinds
            "After sending out a message, you and Darius head to the break room for some snacks."
            scene bg company1_center with blinds
            "By the time you return, Goro is waiting at your desk."
            "... he doesn't look happy."

            show goro
            player "Hi Goro!"
            player "..."
            player "What's wrong?"
            goro "Did you know that I was in a meeting when you messaged?"
            player worry "Yes... sorry about that. I saw on the profile of your TeamChat that you were in the middle of one."
            player "Did I interrupt something?"
            goro "..."
            goro "I wasn't just in the middle of a meeting."
            goro "I was presenting my screen."
            player surprised "Oh! "
            player worry "So you mean... everyone saw my message?"
            goro "Not only did they all see your message, but I was presenting to our board members."
            player "Board members?"
            goro "The people that fund our company. Basically, the people on top."
            player pout "..."
            goro "[player_name], when you see that someone is in a meeting, you shouldn't send a message."
            goro "Wait until the meeting is over in the future, okay?"
    
        "Wait until the meeting is finished":
            player "No... we should probably wait."
            player "He can't message back during a MEETING, right?"
            player "We'll just end up needing to wait until he's done, regardless."
            darius "True, true. We also don't know if we're interrupting anything important..."
            scene bg company1_breakroom with blinds
            "Instead of sending the message, you and Darius head to the break room for some snacks."
            scene bg company1_center with blinds
            "By the time you return, Goro is at his desk, typing away."
            "You go over what you need his help with. The two of you call over Darius and explain the solution to the bug that you found."
            "Once you and Darius prepare to leave, Goro stops you."

            show goro
            goro "Hey! Talk to me for a second."
            goro "Darius told me that you two thought about contacting me. "
            goro @ smile "I'm really, really glad you didn't."
            player smile "No problem! Was your presentation important?"
            goro @ neutral "I wasn't just in the middle of a meeting."
            goro "I was presenting my screen."
            player surprised "Oh! "
            player "So you mean... everyone would have seen my message?"
            goro "Not only would they all have seen your message, but I was presenting to our board members."
            player "Board members?"
            goro "The people that fund our company. Basically, the people on top."
            player neutral "Whoa! That would have been... INCREDIBLY embarrassing."
            goro "Tell me about it! For you and me both!"
            goro "Always remember When you see that someone is in a meeting, you shouldn't send a message."
            goro "Do exactly as you did earlier and just wait until after things are over."
            goro "You'll never know what you're interrupting until it's too late."
            "You gain 10 Renown for your patience."
            $ player_stats.change_stats(RENOWN, 10)
    return

label v2_css:
    player smile "Bye everyone! It's about that time of day - I'm about to pack up and head home."

    show goro
    goro "Hold on there for a second, [player_name]."
    goro "Can you do me a favor before you go?"
    player "Sure Goro! What's up?"
    goro "It's about ticket number 4497. "
    goro "You did a great job on it! There's just a small problem with some of the CSS on the homepage."
    goro "Can you take a look at it please?"
    player "Sure! I'll do that now before I leave."

    scene bg company1_lydia_cubicle with dissolve
    player neutral "..."
    player "Okay, so it looks like there are some CSS classes that are clashing with each other on the homepage."
    player "I'm a bit worried, because one of the classes that is being used is used in a handful of other places."
    player "I could always use some inline CSS for a really quick fix, but I know that's generally kind of frowned-upon..."
    player "I could also stay a little later and work on a legitimate fix."

    menu:   
        "Quickly write out some inline CSS":
            player "It's pretty late... and I'm not sure when Mom or Dad will be home to feed Mint."
            player "I think I'm going to just add a little bit of inline CSS to fix this."
            "You're a busy developer - sometimes it doesn't hurt to cut corners."

            if renpy.random.random() < 0.5:
                "... but sometimes it DOES. WILL this become a problem later?"
                "Who knows. Either way, you gain 10 Energy for being able to get home on time."
                $ player_stats.change_stats(ENERGY, 10)
            else:
                player "It's pretty late... and I'm not sure when Mom or Dad will be home to feed Mint."
                player "I think I'm going to just add a little bit of inline CSS to fix this."
                "You're a busy developer - sometimes it doesn't hurt to cut corners."
                "... but sometimes it DOES."
                goro "Hey! How's the ticket coming?"
                player "Ah! Goro. You spooked me. I thought you left for the day?"
                goro "Turns out I had a ticket of my own that I needed to hotfix. Did you finish up?"
                player "Um... yep! All done!"
                goro "Cool! What did you end up doing to come to a solution?"
                player "(Oh jeez, he's going to find out...)"
                goro "Hoooold on slugger - inline CSS?"
                goro "This is quick, but not always best practice."
                player "I figured it would be fine... it's getting pretty late."
                goro "Right, but I asked you just to take a look at your ticket."
                goro "It's okay to just get an idea of what's causing the problem and then return to it in the morning."
                goro "I'd rather have you properly spend time on a solution than throw in some inline CSS."
                goro "What if this problem re-appears in another page? Will we just keep copy-pasting the same few lines of CSS?"
                player pout "(Sigh) You're right."
                goro "It appears that you know what's causing the problem, based on your solution. You just need to come up with one that's a little more long-term than inline CSS."
                goro "Why don't you head home for the day."
                player neutral "Right. I'll see you in the morning."
                "You pack up your things, embarrassed to have been caught coming up with a quick and dirty fix."
                "You lose 5 Renown for your inline solution."
                $ player_stats.change_stats(RENOWN, -5)
   
        "Spend some time fixing one of the conflicting classes":
            player pout "(Sigh) No point in kicking the can down the road..."
            player "There's a chance that it'll be someone else's problem one day - or maybe even mine."
            player "So I should probably do things right the first time."
            player smile "I'll give Mom or Dad a call to make sure that Mint is fed and get started on this."
            "It pays to do things the right way! But no good deed goes unpunished."
            "You gain 10 Renown for doing the right thing. But lose 5 Energy for working late."
            $ player_stats.change_stats(RENOWN, 10)
            $ player_stats.change_stats(ENERGY, -5)
    return

label v2_thick:
    player pout "Ugh... it's 5PM and this is nowhere close to being done!"

    show darius
    darius @ smile "Girl, you look STRESSED. What's going on?"
    player "It's this dumb ticket."
    player neutral "Remember the Canyon Building Company's ticket? The one where we're building out a CRM for them?"
    darius @ neutral "Right, right - we agreed that that one was a 4. "
    darius "By the way... I hope I don't sound too clueless, but what's a CRM? Everyone's been talking about it so I've been too afraid to ask."
    player "Don't worry - I didn't know what the heck it was up until four days ago!"
    player "It stands for “Customer Relationship Manager”. "
    player "It's just a piece of software that allows you to keep track of things about a company's customers."
    player "You can do things like log all of their contact information, what point of the onboarding process they're in, records of past sales, and a lot more, depending on the software."
    player "That sort of thing."
    darius "Aaaah, gotcha. So what's going on with the CRM?"
    player "We all agreed during backlog grooming that fixing this bug would take about four days to complete."
    player "But it's been FIVE days, and it looks like I'm barely halfway done. "
    player "I've asked Goro, Mike, and Mala for help dozens of times already."
    player "On one hand, I feel like something is just wrong with me and I'm being too slow with the ticket."
    player "Like... Maybe I'm a bad developer."
    player "But maybe I'm not? Maybe something is wrong here?"
    darius "That sounds really stressful. Either way, you're going to have to do SOMETHING... You're a day past your deadline."
    darius "The way I see it, you can either push through this and try your hardest to get it done soon,"
    darius "or bring this up with Goro or Iris."
    player "Um... maybe Goro. Iris scares me."
    darius "She scares all of us. "
    darius "No matter what, you're NOT a bad developer. Don't say that about yourself, okay?"
    darius "I've worked with you a few months now, and I feel like you're always doing your best to learn something new."
    player smile "Thanks Darius. That means a lot."

    hide darius with moveoutright
    player neutral "Hm... So what AM I going to do about this?"
    player "Maybe I SHOULD talk to Goro? Because this ticket is pretty hard. I don't know if it's normal for juniors to be able to do this much."
    player "On the other hand, I could definitely just stay a little later... I bet if I did that, I could have the ticket done by tomorrow evening."
    
    menu:
        "Talk to Goro about the ticket's difficulty.":
            player "No... I probably should talk to Goro about this."
            player "I've never, ever spent longer than three or four days on a ticket."
            player "They could be just trusting me with more responsibility, but maybe something else is going on?"

            show goro
            goro "Hey, newbie. What's going on? You look tired."
            player pout "Thanks."
            goro @ smile "Hey, I didn't mean it that way! Is it about ticket 4522?"
            player neutral "Yeah, the Canyon Building Company account."
            player "I've been working at this bug for the last five days... and I've been making progress, but it just feels like I've got a lot more to go."
            player "Do you mind taking a look at it?"
            goro @ neutral "Sure! Let's see here."
            goro "... "
            goro "Hm."
            goro "I thought the function the last ticket added was just breaking one component?"
            player "Nope. Each time I make a change to it to fix one component, another one breaks."
            goro "Gotcha. It's a good thing you came to me - it seems like the scope of this ticket has grown."
            player "What do you mean?"
            goro "Sometimes, a ticket looks like only one thing is broken. But it turns out an entire system needs to be re-written."
            goro "When that happens, we don't just go, “Whelp, that's your problem, since you accepted the ticket.”"
            goro "It means we all need to re-group and either break this task into multiple tickets that all have their own points,"
            goro "Or re-point YOUR ticket."
            goro "Remember, the pointing system is supposed to give an idea of how difficult a task will be."
            goro "We pointed this at a 3, but by the looks of it, this is an 8-pointer."
            player "An 8-POINTER?!"
            goro "Yep. We can't expect you to do that on your own..."
            goro "Or, we can, but we have to give you more time than just five days."
            player "Jeez, I'm glad I said something!"
            player "What should I do now, then?"
            goro "Go ahead and stop working on this ticket and pick up another one."
            goro "I'll take a look at this and see how we can break things up. We'll discuss this during tomorrow's standup."
            player smile "Thanks Goro! That's a huge relief..."
            goro "Don't relax just yet! We've still got a lot of work here to do. "
            goro @ smile "But at least you don't have to do it all by yourself."
            "You gain 10 Energy once you realize you won't need to handle that monster of a ticket on your own!"
            $ player_stats.change_stats(ENERGY, 10)

        "Push through until it's done.":
            player pout "(Sigh)"
            player "I think if I stay a bit late for a day or so, I may be able to finish this."
            player "I didn't sign up to become a developer to give up when things get hard."
            player neutral "Besides, I don't want everyone to think that I'm a quitter."
            "You stay for a few HOURS after work. "
            "As you watch the sun disappear behind the buildings closest to your office, you feel yourself getting tired."
            "It's nearly 8PM, and even the janitor is preparing to lock up for the day. "

            play sound 'audio/sfx/social_media_notification.wav'
            show goro
            "You suddenly get a message from Goro in TeamChat."
            goro "Hey newbie. What's got you up so late?"
            goro "I saw that your TeamChat status was set to “Online” while I was double-checking some of my own work, so I thought I'd shoot you a message."
            player "Hey Goro."
            player "I'm working on ticket 4522."
            goro "The Canyon Building Company account, right?"
            goro "I was going to ask you about that. Have you been putting a dent in it?"
            player "About that... I wasn't going to say anything, because I should be done tomorrow, but I'm still at the office right now, working on it."
            goro "You're WHAT? [player_name], it's almost 8PM. It's not safe to be alone in the office that late."
            goro "Why didn't you ask for help??"
            player "To be honest, it just seemed like such a “junior” thing to do..."
            goro "But you ARE a junior."
            goro "What's the problem? Can you push up what you've done so far and start on your way home?"
            goro "I should have reviewed it by the time that you get back."
            goro "Regardless, I don't want you in that huge building on your own. We don't have any security on our floor, and there could be weirdos walking around."
            player "Okay. I'll start on my way back."

            scene bg bedroom with fadehold
            pause 2.0
            scene bg laptop_screen night with blinds
            play sound 'audio/sfx/social_media_notification.wav'
            show goro
            goro "So I think I'm seeing what the problem is."
            goro "I thought the function the last ticket added was just breaking one component?"
            player "Nope. Each time I make a change to it to fix one component, another one breaks."
            player "So far, I've fixed about five of them, manually. "
            goro "How many more are there left to fix?"
            player "Around twelve."
            goro "[player_name]! You've got to flag one of us when something like this happens."
            goro "It seems like the scope of this ticket has grown."
            player "What do you mean?"
            goro "Sometimes, a ticket looks like only one thing is broken. But it turns out an entire system needs to be re-written."
            goro "When that happens, we don't just go, “Whelp, that's your problem, since you accepted the ticket.”"
            goro "It means we all need to re-group and either break this task into multiple tickets that all have their own points,"
            goro "Or re-point YOUR ticket."
            goro "Remember, the pointing system is supposed to give an idea of how difficult a task will be."
            goro "We pointed this at a 3, but by the looks of it, this is an 8-pointer."
            player surprised "An 8-POINTER?!"
            goro "Yep. We can't expect you to do that on your own..."
            goro "Or, we can, but we have to give you more time than just five days."
            player worry "Jeez... What should I do now, then?"
            goro "Go ahead and stop working on this ticket and pick up another one."
            goro "Get some dinner, do something fun, sleep, whatever you want."
            goro "Just give this ticket a break."
            goro "I'll take a look at this and see how we can break things up. We'll discuss this during tomorrow's standup."
            player pout "Gotcha. Thanks Goro... sorry for making you worry."
            goro "It's fine. Just promise you won't do something like this again, okay? Ask for help when you need it."
            "You lose 15 Energy for staying in the office so late."
            $ player_stats.change_stats(ENERGY, -15)
    return

label v2_success:
    show mala
    mala "Hey [player_name]? Can I talk to you for a sec?"
    player "Sure! What's up?"
    mala "I think I might have messed up. Like, REALLY messed up..."
    player "What's going on? I'm sure it can't be THAT bad."
    mala "Well, I was working on the Braze Salon's account."
    mala "They wanted an interactive map that marked where their shop's location is."
    player "Well that's not too hard, right? That should be as simple as adding a Schmoogle Map to their website."
    mala "Right. It WAS that simple. But I also made a simple (but serious) mistake."
    mala "I think that I may have posted our API key to a public repo by accident."
    player "API key? What's that?"
    mala "Not all API's are free to use."
    mala "Sending lots of CRUD requests to an API can take a lot of power, and the people that created the API will need to be able to pay for hosting something with so many requests."
    mala "Even if an API isn't a paid one, if I make thousands of requests and crash an API that lots of other people depend on, that's a problem."
    mala "So to hold everyone using API's accountable for the number of requests they make, each person is given an API key."
    mala "Our company had to get an API key made for the Braze Salon to be able to use Schmoogle's mapping services. "
    mala "And... I think I just posted it."
    player surprised "Posted it?! You mean you saved it in a code repository?"
    player worry "A... PRIVATE repository, right?"
    mala "I wish it was!"
    player "Oh jeez... that IS a big deal. "
    player "You've taken it down already though, right?"
    mala "I have. I took it down as soon as possible. But I'm just kind of freaked out."
    mala "Schmoogle charges money for every 1,000 CRUD requests to their API, and we negotiated $100,000 in free credit for the Braze Salon."
    mala "If someone on the internet got ahold of that API key...  "
    mala "That's a TON of money on the line that the company will have to reimburse..."
    mala "What should I do?"

    menu:
        "It was a mistake. It's okay to make mistakes.":
            player neutral "Well... have you gotten any TeamChat messages about this?"
            mala "No, nothing so far."
            player "If that's the case, maybe you're being a little paranoid?"
            player "You accidentally posted the key, but then you took it down immediately. No harm done, right?"
            mala "I GUESS so..."
            player "Let's go grab some lunch. Maybe that'll take your mind off of things."
            "Later that afternoon..."
            player "Phew! I'm full! I think I can probably knock out this ticket before heading home for the day."

            play sound 'audio/sfx/social_media_notification.wav'
            player "Hm... What's this? Iris sent out an email?"
            player "It's flagged as 'URGENT'. Better read it so she doesn't have to talk to me about it in person."
            player "Or maybe she won't just talk to me - it looks like this has our whole department CC'd on it!"
            show iris
            iris "To whom it may concern,"
            iris "We've recently had an... incident. I would like to take this as as an opportunity to remind you all that mistakes are natural."
            iris "Mistakes are a part of developing a good product or rendering a good service. They help us gow and remind us that we're human."
            iris "What is NOT 'natural' and 'normal' and 'good' is making a mistake (an incredibly risky one, at that) and not saying anything to anyone."
            iris "This morning, an employee (It is not important who), posted a Schmoogle maps API key into a public repo."
            iris "The API key was taken down quickly, and the company, with around six figures of Schmoogle credit, did not lose any money."
            iris "What DID happen is that Schmoogle immediately sent out an email to the client themselves, warning them that one of their bots detected a Schmoogle key publicly published."
            iris "For the uninformed, my use of the term 'bot' refers to software that Schmoogle has that scans their search engine listings faster than any human being can."
            iris "They were fast enough that out of Schmoogle's millions of users, a bot was able to find the API key within what seems to be minutes of the key's posting."
            iris "But people with bad intentions have bots of their own. Some people create bots for the sole purpose of being able to steal API keys specifically."
            iris "The client could have lost a LOT of money because of this."
            iris "They were told to take it off of the internet quickly, and were warned what the consequences would've been if it had been found."
            iris "As you can imagine... this was not a good look for our company."
            iris "Had we been notified of this issue, we could've address it – possibly before our client even saw the email."
            iris "We would have the appearance of a company that makes mistakes, but ultimately keeps them under control."
            iris "Now, our senior developers are in a meeting, doing their best not to lose this client. Our client feels blind-sided. Betrayed."
            iris "Do not be like... our 'anonymous employee'. Do not withhold information that could harm yourself or your team."
            iris "If any of you have any general questions about this incident and what our next-steps are, please feel free to send me an email or a TeamChat message."
            player "Oh no... Mala..."
            "You didn't see Mala for another hour. She was too busy sitting in Iris's office being lectured."
            "Thankfully, she wasn't put on a PIP (a disciplinary Performance Improvement Plan that was usually the next step to being fired), but, at least for a while, Iris wouldn't view her in a favorable light."
            "You couldn't help but feel guilty, having advised her that the whole situation would blow over."
            "You lose 10 Renown. Mala says it's fine, but you can tell that she's a little upset with you too."
            $ player_stats.change_stats(RENOWN, -10)

        "Should we tell someone about this?":
            player "I don't know if NOT telling someone is a good idea."
            player "There's nothing that you can do about having posted the key, but my gut tells me that you should tell someone on the team."
            mala sweat "(Sigh)... You're right, you're right."
            mala "I just... don't want to have to tell IRIS of all people..."
            player "Yeah. You couldn't pay me enough to want to do that."
            player "But that's the good thing about telling someone on your own terms, right?"
            player "You can tell Goro, and GORO can tell Iris. They seem to have a pretty good relationship."
            player "Somehow."
            mala -sweat "I think you're right."
            mala "That feels a lot better than letting things sit. I'll go tell him now, and maybe we can grab lunch together when I come back?"
            player "Definitely - I've been wanting to try that Thai place down the street from the office for a week!"
            "20 minutes pass before Mala returns."
            player "You look like you're in a good mood! Everything okay?"
            mala "I don't know if I'd say I'm in a 'good mood', but I'm definitely relieved!"
            mala "Goro was worried, but he took things pretty well, considering what just happened."
            mala "He told me he didn't have too much time to explain because he and the other seniors would act quickly,"
            mala "but basically, we dodged a huge bullet. And I may have dodged putting my job at risk."
            player relieved "Jeez!"
            player neutral "What would have happened if we didn't say anything?"
            mala "Well, Goro told me that he's done something similar once with another service."
            mala "He said that the service immediately sent out an email to him, warning him that one of their bots detected a key publicly published."
            player "A 'bot'?"
            mala "Basically, 'bot' refers to software that scans web page listings faster than any human being can."
            mala "Schmoogle is basically the biggest tech company in the world, and probably has millions of bots combing their search engine at any time."
            mala "Because the repo is on a webpage, they were able to find it."
            mala "And they were fast enough that out of Schmoogle's millions of users, a bot was able to find the API key within what looks like minutes of me posting the key online."
            player smile "Awesome! That's good, right?!"
            mala sweat "..."
            player "Ok!"
            player pout "Or not!"
            player neutral "Tell me why that's not good?"
            mala -sweat "People with bad intentions have bots of their own. Some people create bots for the sole purpose of being able to steal API keys specifically."
            mala "The client could have lost a LOT of money because of this."
            mala "Goro said that since the company in question usually emails you if they find a key, they would have emailed the CLIENT first,"
            mala "since they're the owner of the Schmoogle account that made the key."
            player "I see. And that would have looked pretty bad on us..."
            mala "Exactly. That would have made us look incompetent if it didn't at least seem like we knew about a key being posted."
            mala "So he had to send off an email to them really quickly and go have a meeting with Iris to inform her of what was going on."
            mala "He says the client is super nice and that if we tell them first, it will PROBABLY be okay."
            mala "He even says that he's not going to tell Iris who did it!"
            player "Really?! Wow! I thought that would be a part of the process?"
            mala "He says pointing fingers is bad for team morale."
            mala "Buuut, he says if things do go sideways and the client is super mad that he may have to let Iris know."
            player "..."
            player "Let's not think about that now."
            mala @ smile "Yeah."
            mala "So. Thai food?"
            player laugh "Thai food!"
            "You both go down the street for a delicious lunch. The Thai food was just as good as people around the office have been saying."
            "Mala tells you that she told Goro that you were the one that pointed out that she should say something instead of keeping things to herself."
            "He said to thank you on his behalf."
            "You gain 10 Renown for your good advice and responsible thinking."
            $ player_stats.change_stats(RENOWN, 10)
    return

label v2_competent:
    show goro
    goro "[player_name]! How's ticket #999 going?"
    player "I'd say it's going well, but I haven't gotten started on it yet!"
    goro "No problem - do you remember what this one is for?"
    player "To be honest with you, my brain was a little fried this morning during our meeting. I was going to read through the ticket again."
    goro "Want me to spare you a bit of time?"
    player smile "I won't say no to that!"
    goro @ smile "Cool! Basically, Juan's going to be out for a few months."
    player surprised "What? The mid-level developer, right? Is everything okay?"
    goro "Everything's fine - really good, actually!"
    goro "But he and his partner just adopted their first child, and he wants to take off a few months to be available at home for that."
    player smile "So that's why I haven't seen him around - good for them!"
    goro @ neutral "We tried to get as much information out of him about the things that he's written as we could before he left. Things were going fine for a few days,"
    goro "But we all forgot that Juan was working on a pretty important function."
    goro "It does quite a few things, but no one knows exactly how it works."
    goro "One of the things it does is destroy duplicate records in our project's database. The client has a blog with a comments system,"
    goro "so basically, if a duplicate comment is created for whatever reason, the function get's rid of it."
    goro "But now, users are starting to see more and more duplicates."
    goro "That definitely means we have an issue with duplicates being made, sure, but that's a whole other ticket."
    goro "For now, we need someone to go into his function and figure out why duplicates aren't being created."
    player surprised "Woah... I agreed to doing that?"
    goro "You really need to pay more attention during meetings. (laugh)"
    goro "But yes, that's correct. Does that sound like something you can do? Have you done something like this before?"
    player smile "To be honest, I haven't, but I'll do my best!"
    goro @ laugh "Awesome! You know to come grab me if you need a bit of help."
    hide goro with moveoutright

    player neutral "Okay... so."
    player "I'll need to figure out how this function works, so I can fix it."
    player "The ticket says that the function is called background_jobs(), and what document it's in."
    player "Where should I start?"

    default v2_competent_choices_visited = set()

    menu v2_competent_choices:
        set v2_competent_choices_visited

        "Use Universal Search to find other places that the function is used":
            player neutral "A good place to start would probably be to run a Universal Search!"
            player "Using this, I can search every single document in our repo. Which also lets me see all of the places that background_jobs() is being run."
            player sweat "Okay... so this is used in a TON of places."
            player -sweat "But, I think with a bit of looking, I can find examples of people using the function."
            player "That way, I can get an idea of what situations it's meant to be used in. This will give me a clue as to how the function is supposed to be used."
            jump v2_competent_choices

        "Look at tests for the function":
            player neutral "Hm... I should probably check all of the tests for this function."
            player "Usually, tests have descriptive blocks of code that explain exactly what a test is meant to be checking for."
            player "The texts can give me a hint as to what the function is meant to do."
            player "Plus, I can run all of the tests for the function and pay close attention to the tests that are failing."
            player "This can tell me where I'm meant to start to get them fixed! And I can be more certain things are working right when all of the tests pass."
            jump v2_competent_choices

        "Call the function in the console and play around with it a bit":
            player neutral "If I want to see how a function is meant to work, I can always play with it in the console!"
            player "Most languages have a console of some sort where I can write code and it will execute immediately."
            player "Since this project's backend is Ruby on Rails, I'll mess around and use the function in the Rails console in a few different ways."
            player "I can test a few different arguments and situations with this function, and maybe it'll help me find out where it's breaking."
            player "Then once I re-write the function, I can manually test it here in the console as well!"
            jump v2_competent_choices

        "Ask the developer who created the function":
            player neutral "Normally this would be a good option..."
            player pout "If the developer who created the function was actually here! Juan is on paternity leave, remember? (sigh)"
            jump v2_competent_choices

        "I think I have all of the information I need" if len(v2_competent_choices_visited) > 2:
            pass

    player relieved "Alright! I think that's enough information gathered for now."
    player neutral "Time to get started chasing this bug!"
    "You work for the next hour or so on the bug. You were able to use all of your usual methods to diagnose the issue with the function, and all of the duplicates are being deleted!"
    "The rest of the function has returned to working normally as well."
    "Though there's still one more piece of the puzzle missing... Why were the duplicates being created in the first place?"
    "You call over Goro after pushing up your code to have a face-to-face code review."

    show goro
    player "...and that's how I got to where I am now."
    player "So what do you think? Does this all look right to you?"
    goro @ smile "Yep, it looks pretty solid to me! Great job."
    goro "You'll just need to remove any unnecessary comments, and you're ready to go."
    player smile "Thanks!"
    player neutral "By the way, did we ever figure out what was going on with what's creating the duplicates in the first place?"
    goro "We sure did!"
    goro "Get this - the problem was on the frontend the whole time!"
    goro "Basically, the app would send off a post request, and users would be prompted with a loading screen that would request that they wait while their progress was saved."
    goro "But people kept on tapping that dang submit button."
    goro "So we were getting multiple requests sent off."
    player "It's always the little things!"
    goro "Yep. Good ol' PEBCAK."
    player @ surprised "What?"
    goro @ smile "Don't worry about it."
    goro "Wanna grab lunch?"
    player "You know I do!"
    "Great detective skills! You earn 5 Renown for your function sleuthing."
    $ player_stats.change_stats(RENOWN, 5)
    return

label v2_automate:
    show goro
    goro "So, do you remember what we scheduled this meeting for?"
    player "Not exactly... can you explain one more time?"
    goro "No problem; So, every meeting, we have 'minutes' - it's just a log that keeps track of the things that we talked about."
    goro "We rotate who keeps minutes for the week. It was me this week, but we're going to have you do it next week."
    goro "I know it sucks, but we have to kind of... MANUALLY copy and paste these minutes from our minutes document into this spreadsheet software."
    player "But... WHY? There are a LOT of minutes here - it feels like it's going to take forever."
    goro "Yeah. (sideways face)"
    goro "It usually takes me a good 45 minutes to complete this... and that's when I'm feeling focused. Otherwise it takes me a little over an hour."
    goro "To answer your question, there isn't really a why to it, either. It's an inefficient system, unfortunately."
    goro "Plenty of other teams don't do this, but it's something that management wants us to do to make sure that we're spending our time well."
    goro "Maybe we can do something about it at some point. But for now, minutes! Let's get into how to set this thing up."
    "The two of you sit together for about 30 minutes walking through the intricacies of setting up meeting minutes using the team's complicated spreadsheet."
    "Finally, Goro leaves you to your work."
    hide goro with moveoutright

    player "Jeez... I guess it's time to get started."
    player "I know that Goro says this is the way that things have always been done, but there's got to be a faster way."
    player "Hm... maybe I can just automate the process with something like Python?"
    player "I remember scrolling through Youtube and seeing a video from freeCodeCamp about automating Excel spreadsheets using Python."
    player "Maybe I could do the same thing?"
    player "But... Goro just spent all that time explaining how to do our minutes. I'm sure there's a REASON no one has automated things up until this point."
    player "And I've never automated anything before. What should I do?"

    menu:
        "Do things the long way, automate some other time.":
            player "Hm... Maybe I should automate this some other time."
            player "Goro just spent all of this time showing me how to do things the way they've always been done. Maybe he did that for a reason?"
            player "And maybe there's a reason no one has automated this yet in the first place?"
            player "Maybe it'll even be ideal for me to do this the long way once or twice and take some notes so I can best know how to automate this in the future."
            player "Oh well... I'd better get started."
            "On one hand, you're happy you played things safe."
            "But what Goro taught you barely scratched the surface of how long doing the minutes manually would actually take you."
            "It took Goro around an hour to do it as someone experienced with the process."
            "It took you a little over two."
            "You took plenty of notes to learn how to automate the process next time, but for now, you've lost 10 Energy thanks to this long, boring work."
            $ player_stats.change_stats(ENERGY, -10)

        "Spend some time automating the minutes process.":
            player "Hm... I really can't shake the idea that this process can be automated."
            player "First, I could start by making a copy of the original and second spreadsheet in case I mess things up."
            player "Then, I could start by doing just one or two rows of data."
            player "I could make a list of all of the tasks that have to be performed to get those done... like transferring a list item from the text document to row one, column one of the second spreadsheet."
            player "Once there's a line break "
            player "I could make a list of those actions, program them out, turn that list into code, and do that until the process is done..."
            "Before you know it, you're in your IDE, hard at work on your automation project."
            "You're glad you make a copy of the needed spreadsheets before you start because the first few runs of the script, you mess up a few things."
            "Your initial version of the script works well enough, transferring many of the necessary bits of information to their corresponding rows and columns in the main document."
            "But as you run your script, you realize you're missing a few test cases. Like how minute entries for Fridays have one or two more meetings in them than Wednesdays."
            "So you write some code for those scenarios too."
            "Before you know it, it's been two hours, and Goro returns."
            goro "Hey! Banging your head on the wall just yet?"
            player "Hold on. Oooone sec..."
            player smile "Aaaaaand... done! Take a look at this!"
            goro "..."
            goro @ laugh "No way!"
            goro "Did you automate transferring our minutes over to the spreadsheet?"
            player "I sure did!"
            player "It's not 100\% perfect - there's one or two fields in the spreadsheet that we need to fill out manually, but this covers about 80\% of the work."
            goro "About how long does it take you now?"
            player "I'd have to say about... 10 minutes, since the script takes about 10 seconds to run, and the rest of the time covers the manual parts."
            goro "Great job, newbie!"
            goro "I guess that's the beauty of people that enter this field from nontraditional backgrounds."
            goro "You all see things a way that some of us that have been doing this for a long time don't."
            goro "Great work!"
            goro @ smile "I think this deserves lunch on me."
            goro "Well... not ME, but the company credit card. You in?"
            player @ laugh "Definitely!"
            "Thanks to your bright idea, you've gained 10 Renown."
            $ player_stats.change_stats(RENOWN, 10)
    return

label v2_demo:
    scene bg company1_boardroom with fadehold
    show darius at right
    show goro at left
    darius "...and that's about it for what I got done yesterday."
    darius "Today, I mainly just want to finish up with the fixes for the Farraday account's schema."
    goro "Great - thanks for the update Darius."
    goro "It looks like Darius was our last update for today's stand-up."
    goro "Have a great day, everyone!"

    scene bg company1_center with blinds
    show mala
    player "Hey, Mala! Could I ask you a question really quick?"
    mala "Sure! How can I help, fishie?" # Ed: Is fishie a nickname for the player? If so, Fishie would be better.
    player "I didn't want to interrupt the stand-up since Goro said he needed to get to his next meeting,"
    player "but could you clarify what I'm supposed to be doing on that database ticket that Iris assigned me?"
    mala "Oh yeah - the one for the sales team?"
    player "Yeah! From what I understand, I'm supposed to be cleaning out some data...?"
    mala "Pretty much - basically, ConsultMe has a sales team."
    mala "They're in charge of getting the clients that the marketing team draws in for us to purchase our services."
    mala "To make that easy for them, we have a few demo websites and apps for them to show our potential clients during meetings."
    player @ surprised "Demo websites? Are these real, functioning applications?"
    mala "Yep! We have demos for eCommerce apps, landing pages, blogs - you name it!"
    player "That's pretty smart... are they interactive?"
    mala @ smile "They are! Basically, customers can go in and play with the apps during a call with a representative, and see how they work."
    mala "All of those apps need fake data in order to give the most realistic experience to our customers."
    mala "That data can get really messy when someone, say, goes into a blog app and changes the titles of posts,"
    mala "or creates sample products on our eCommerce storefronts with placeholder images and text."
    mala "So, we built this cool dashboard where salespeople can just click a button, and it generates all new records of comments and posts for the blog apps,"
    mala "products and descriptions for the eCommerce apps – that sort of thing."
    mala "The problem is that each time they generate new data, we kind of just... HIDE the old data?"
    player "Hide it? Wait..."
    player "So you mean we don't delete it?"
    mala "Nope. We're creating something like 30 new records per demo."
    mala "As you can imagine, that begins to flood the sales demo database pretty badly."
    player "So you're saying you need someone to go in and write a script to delete that data?"
    mala "I talked with Goro, and we have a ticket written up to automate the process for our next sprint."
    mala "You and Darius will actually be working on it! (HAPPY)"
    mala "But for now, we want you to go in and delete the data manually."
    mala "Darius has done that before and knows how the process works. We just want you to get accustomed to the schema since you'll be writing the script to delete the data before the next sprint."
    player "Got it! So I just need to go into the demo database and delete the old data?"
    mala "Exactly! Just delete any data that's more than two weeks old. Data that old isn't really useful to the sales team anymore."
    player "Cool! That sounds easy enough. What kind of database is it?"
    mala "We set up a Postgres database. If you check out the onboarding document we sent you when you got here, you'll find the command you need to access it."
    mala "You just need to MAKE SURE that you play with the data in staging first before you start deleting anything."
    player "I've been meaning to ask about that for a while now - what is staging?"
    mala "So we have a few different databases and development environments we set up for our clients:"
    mala "First is your local database, which is just a version of the database that exists on your computer."
    mala "When you modify it or any of the data inside of it, those changes are only happening on YOUR machine - that is to say, locally."
    mala "Next, there's your prod environment – prod is short for “production”."
    mala "This is the data that actually gets accessed by our apps and websites when they're live and displayed publicly."
    mala "Finally, we have staging. Staging is “live” in the sense that it isn't only on your computer, but it can't be accessed by people outside of the company."
    mala "It basically allows us to play around with data and features and see how they'd actually look in production. So it's kind of an in-between."
    mala "All of these databases usually have different seeds. Staging usually has WAY more data than production."
    mala "Whenever we need to make changes to a prod database -"
    mala "- which the sales demo database is - "
    mala "we typically make it to the staging database first."
    mala "This is because we set our staging database up so that it refreshes all of the seeds once a week automatically, or with a simple command if we mess something up."
    mala "So you can make as many mistakes as you'd like while you get the hang of things. (HAPPY)"
    player "Okay - that was a lot of information, but I think I got all of that!"
    player "I guess all that's left to do is start!"
    mala @ smile "That's what I love about you fishie - you've got so much energy!"
    mala "Just remember -"
    mala " - and I CANNOT stress this enough - "
    mala "experiment with your queries and delete commands in staging BEFORE trying them out in our production environment, okay?"
    mala "And don't forget that you can always ping me if you need any help!"
    player "Gotcha!"

    scene bg company1_lydia_cubicle with blinds
    "Back at your desk, you take a look at Postgres's documentation to get an idea of how to perform basic queries."
    "You believe you've got the hang of searching for specific records, and decide to try your hand at deleting records."
    player "This isn't so bad!"
    player "I haven't written SQL in some time - I forgot how fun it is. (HAPPY)"
    player "So, Mala said that I should get started with deleting all of the posts from the blogging engine sales demo."
    player "If I do this then..."
    player "Alright! I managed to delete the three specific records that I wanted."
    player "Let's see if I can delete a few more..."
    player "... Awesome! That takes care of the whole table! Looks like only blog comments from the last 7 days are in the comments table."
    player "I wonder..."
    player "Maybe I can write one BIG query?"
    player "One that can take care of all of the data from every table in the demo database?"
    player "It would use the same logic as my last query..." # Ed: In the following lines it says that the player spends the next 15 minutes writing the logic for the long SQL query. Maybe it would be better to say something like "The logic for that would be similar, but would need some tweaking..."
    player "Then I'd be finished early for the day! Mint is two weeks overdue for a bath and I do NOT want to do that after commuting home today."
    "You spend the next 15 minutes writing up the logic for one long SQL query that can take care of all of the database tables at once."
    "You check and double check your logic, and find examples of others online doing the same thing."
    "Finally, with your script finished, you're ready to run your command."
    player "Okay... here goes nothing."
    player "..."
    play sound 'audio/sfx/keyboard_typing.wav'
    "You wait."
    "And wait."
    "And wait some more."
    "It's beginning to get quite boring."
    player pout "Jeez... this is taking FOREVER."
    player "Did I do something wrong? I remember Goro saying that larger queries can take a while to run, but this is ridiculous..."
    player "Maybe I should just abort the script and see if my command is even working?"
    "You stop the script and check a few of the databases that you included in your query."
    player neutral "Hmmm... Is there something wrong with my query?"
    player sweat "It looks like I dropped the entirety of each of the tables the script touched so far."
    player "It took so long because I basically told it to delete the records I called on one-by-one instead of all at once, then to drop the whole table when it finished..."
    player -sweat "Oh well."
    player "At least I can just re-run our seeds like Mala said - "

    play sound 'audio/sfx/office_ambient.wav'
    salesperson1 "What the heck? What's wrong with my demo?"
    player surprised "... Huh?"

    scene bg company1_center with blinds
    "You peek your head out of your cubicle"
    salesperson2 "Yours too? I thought I was going crazy - I can't get into the blog demo."
    salesperson3 "I can't get into the eCommerce demo either. What's going on here?"
    player pout "What the..."

    scene bg company1_lydia_cubicle with blinds
    "You rush back to your computer and start to panic. Were you really deleting data from staging this whole time?"
    show mala
    mala "[player_name]... have you already started deleting the data?"
    player neutral "Yes..."
    mala sweat "O-okay... And you've been deleting from STAGING, right?"
    mala "NOT from production?"
    player sweat "..."
    show iris at right with moveinright
    iris "[player_name]."
    player "I-Iris!"
    iris "..."
    iris "Come with me."
    iris "Now, please."

    scene bg company1_breakroom with blinds
    "The next 10 minutes feel like hours."
    "Iris is incredibly upset with you. Goro seems more disappointed than anything."
    "That stings worse."
    show iris at left
    show goro at right
    iris @ angry "Do you understand what you've done?"
    iris @ disgust "We've had to cancel 70\% of our demos over the next couple of days while we get all of this figured out."
    goro @ disgust "Mala said that she reminded you to check the data in staging. Is that true?"
    player worry "Yes..."
    goro "Oh [player_name]..."
    iris "This could lose the company quite a bit of money."
    iris "It's possible that we still close on all of our potential clients."
    iris "But it's also possible that just as many of them will be snatched up by other consulting companies while we're trying to fix this."
    iris "You somehow managed not only to drop entire tables from our demo database, but to also drop tables with the same name in our cluster of databases."
    player "What do you mean, exactly?"
    goro "We had other blogs built for clients that were live."
    goro "You didn't just drop a few crucial databases for demos DURING some of our sales demos, but for a few of our clients as well."
    goro "Take the comments table - we have several blogs that we host databases for and regularly update."
    goro "You dropped a few of their comments tables as well."
    player pout "..."
    goro "Thankfully, just about all of the tables that you dropped have backups. But the clients that noticed aren't happy."
    player "I'm really, really sorry."
    iris "That's not enough, [player_name]."
    iris "You need to be more careful. You've acknowledged that you were reminded of what was at stake."
    iris "You're a junior, but we would like you to grow within this role. It's been a few months."
    iris @ disgust "I expected better. Perhaps we should be more... stringent with our hiring practices."
    iris "I'm afraid I'll need to put you on a PIP."
    player "A... pip? What's that?"
    goro "Iris. That's a bit HARSH don't you think?"
    goro "[player_name]'s performance has been great for a junior - "
    iris "This isn't up for debate, Goro."
    hide iris with moveoutleft

    player pout "But what does a PIP mean?"
    show goro neutral
    goro "A PIP stands for Performance Improvement Plan."
    goro "It means that for the next few months, you'll be... under review."
    goro "Basically, if you don't improve, you'll be terminated."
    player "I can lose my job?!"
    player "What do I do?"
    goro "Nothing is set in stone, but you'll need to work extra hard to show Iris that this was just a mistake that won't be repeated."
    goro "I bet that, if you can get plenty of tickets completed and make a good name for yourself in the office,"
    goro "you can show Iris that she's making a mistake."
    player "I'll do whatever it takes. Really."
    goro "I know you will."
    goro "How about this? We have some presentations coming up for a few clients. Why don't you volunteer to run them?"
    player "Presentations? What do those entail?"
    goro "When we finish up a project for a client, we usually present the work that we've just completed."
    goro "We walk them through the features that we've built them, and answer any of the questions that they may have."
    goro "Normally we allow the mid-level developers to run these. But I think if you took the reins here, it'd really show Iris how responsible you are."
    player "Okay. I think I can do that. I presented a lot in college. This can't be too different, right?"
    goro "We have one per week for the next three weeks - tomorrow is the official start of the new sprint, and their dates will be announced."
    goro "Volunteer to do them then."
    player "Okay..."
    goro "..."
    goro "I know that Iris seems harsh, but she means well."
    goro "I'll try to talk to her."
    goro "I know this has been kind of a disaster, but..."
    goro "Just about every junior makes some kind of huge mistake at their first job. I'm not really sure why she's this upset."
    show goro smile
    goro "I'll coach you before your first presentation. I know this is something that you can do."
    goro "Just do your absolute best in the meantime, okay?"
    player "... Okay."

    scene bg company1_reception with blinds
    player "This is a disaster..."
    player "How am I going to fix this? Maybe I'm just not cut out for this."
    show maria with moveinright
    maria "Not cut out for what?"
    player "Oh."
    player "Hey Maria."
    maria "What's got you so upset honey? You're usually so peppy..."
    "You explain the day's events to Maria. She cringes harder and harder with every new piece of information."
    maria "Ouch... "
    maria "I can see why you're stressed."
    player "I feel like I blew it. I finally got my dream job, and now people will never see me the same again."
    maria "..."
    maria @ smile "Want to see something cool?"
    player "Sure. Anything to take my mind off of the dumpster fire that was today."
    "Maria invites you behind your desk."
    "She surprises you by opening up... a terminal?"
    player "What...?"
    player "Is that..."
    maria @ smile "A calculator! I made it myself!"
    player "You're programming!"
    player "Since when?!"
    maria "Before you showed up, I used to watch the developers walk in and out of the building, all excited about their projects."
    maria "Everything that everyone was working on sounded so interesting. It didn't feel like anything I'd be able to do."
    maria "It took meeting you, someone who managed to go off the beaten path and teach themselves to program."
    maria "That pep talk you gave me on your first day really inspired me. I've been teaching myself to program during some of our slow periods ever since!"
    player smile "Wow... this is amazing Maria."
    maria "You make a difference here. You bring so much positivity and kindness to this office. And I know this because you made a difference for me."
    maria "Things will turn around - I just know it!"
    player "Thanks Maria."
    player "What's this over here in this window? It kind of looks like some kind of alien script."
    maria "Oh that!"
    maria "I was looking around the freeCodeCamp forums like you recommended, and someone was talking about something called regex."
    maria "It looks weird and complicated, but I've started messing around with it, and it isn't too bad."
    player "Really? But it looks hard!"
    maria "I've seen some really complicated pieces of regex, but even the really small ones are pretty useful."
    maria "One user was talking about how they're the only person at their job that knows how to use it. They said they get a lot of praise from their coworkers!"
    maria "If I've learned anything from some of my past positions, it's that learning to do the stuff that people can't stand doing will make you an attractive employee."
    player "Oh!"
    player "So you're saying if I learn some regex, you think I'll be able to help the team and make myself irreplaceable?"
    maria "Well, no one's REALLY irreplaceable,"
    maria "But it'll be hard to replace you if you focus on learning powerful skills!"
    maria @ laugh "Just make sure that you don't let it get in the way of your assignments. I've made that mistake before, too."
    player "Thanks Maria. For all of this."
    player "This was the pep-talk I needed."
    maria @ smile "You've got this!"
    maria "Don't hesitate to come grab me for lunch if you need a sympathetic ear or another pep-talk, alright love?"
    player "Thanks! And you can come to me for any programming questions you have!"
    maria "Deal."
    return

label v2_redemption:
    scene bg company1_center with fadehold
    play sound 'audio/sfx/office_ambient.wav'
    show mala
    mala "Goro, can you come over here for a second? I can't get this to work."
    show goro at left with moveinleft
    goro "I'm comin', I'm comin'."
    show oliver at right with moveinright
    oliver "Just a moment, Goro."
    oliver "After you've finished with Mala, I need to consult with you on this email - the client is calling again, and I can only put them off for so long." # Ed: Is Oliver writing back because the client called earlier? It's a bit unclear. Maybe it can be changed to something more general like "... - the client is reaching out again, and I can only put them off for so long."
    oliver "I want to make sure I'm telling them the right thing."
    goro "Sure thing. Darius can help you with that while I'm busy."
    hide goro with moveoutleft
    show darius at left with moveinleft
    darius "Gimme just a second - once I get this query written, I'll be right with you, Oliver."
    oliver "Thanks, Darius."
    "When you arrive at the office, the entire team seems frantic."
    player "Oliver, what's going on here?"
    oliver "Hey [player_name]. We're in kind of a code red situation here."
    oliver "Mala was about to join you on a lunch break and received an email from the Zachery Clondike account."
    oliver "Apparently Kyle, one of our mid-level devs, left for the rest of the week before pushing up his work for a client's website."
    oliver "He was in a rush to make his flight, and the client's site is due today."
    player "Can't we just get IT to get into his computer and push it from there?"
    play sound 'audio/sfx/office_phone_ring.mp3'

    oliver "Ugh - just a moment. I need to go prepare my notes on how I'm going to tell them that we may not meet the deadline."
    hide oliver with moveoutright
    mala "Not possible, small fry. Darius says he saw him leave WITH his laptop the day he started his vacation."
    mala "We checked his desk and couldn't find it anywhere."
    darius "I'm almost certain I saw him working on it earlier that day, too. He was just about done."
    mala "Kyle will sometimes go an entire sprint without pushing up his code. I remind him to do it constantly in case a situation like this comes up."
    darius "Mala, real quick - can you help me out with the UI?"
    mala "Sure thing - sorry [player_name], gotta go."
    hide darius
    hide mala
    player sweat "W-wait! How can I help? What else needs to be done?"

    show goro at left with moveinleft
    goro "There's lots to do. It's going to be all hands on deck cleaning this situation up."
    goro "This client makes and maintains several smaller pieces of software, and needs new landing pages and website built pretty often."
    goro "Occasionally, they even contract us to fix bugs on a product of theirs, or help getting a new piece of software over the finish line when they're short on developers."
    goro "They're a huge company, and have been a client of ours for a long time."
    goro "We've been putting off finishing this particular app for a while, which has delayed its launch quite a bit."
    show iris at right with moveinright
    iris "If we lose this client, a lot of money will go with them."
    player "Ah! H-hey, Iris. (SWEAT)"
    iris sweat "... We cannot afford to have them terminate our services."
    show iris -sweat
    player "(Is Iris actually... NERVOUS?)"
    player "(This must be serious.)"
    player @ smile "How can I help?"
    player "Maybe I should start with something that will take the longest or make the most amount of impact?"
    goro "Well, the product is a CRM, so it's pretty complex."
    player "CRM?"
    goro "A customer relationship management app."
    goro "It's used by companies that have sales departments."
    goro "There's quite a bit of detail work that needs to get done."
    goro "For one, the client wants the phone numbers to render in a specific format."
    goro "They need to have a parenthesis around the first three digits, a space after the parenthesis, then the next three digits."
    goro "Finally, the numbers need another space, a hyphen, one more space, and the last four digits."
    iris @ disgust "We could do something like that with regex..."
    goro "But Kyle was the only one here that knew how to use it."
    player "Regex? I've been studying regex."
    iris "Really? Can you fix this?"
    player "I definitely can! Give me a moment."
    play sound 'audio/sfx/keyboard_typing.wav'
    player "..."
    player "There!"
    goro @ smile "Huh - that works!"
    goro "Good job [player_name]."
    player "What's next?"
    goro "Well, we have a few more tasks:"
    goro "We need to limit characters on a ton of different fields,"
    goro "and run a check in the backend to make sure that URLs entered by the user are valid. It saves the sales agents time when they can send them to clients knowing they work properly."
    player @ surprised "Seriously?"
    player @ laugh "Regex can handle all of that too!"

    scene bg company1_center dusk with dissolve 
    "One by one, you tackle the issue tickets that Oliver is submitting almost as soon as they come in."
    "Before you know it, the project is in a functioning state again."
    show oliver
    oliver "Phew!"
    oliver "I think that we did it, everyone."
    oliver "It isn't perfect, but products rarely are on launch."
    player "Is it good enough to be released to the client?"
    oliver "It definitely is! The minimum requirements have been met."
    oliver "That's more than enough to return to the client with."
    oliver "Kyle gets back from his vacation next week, and we can get in all the extra features he finished before leaving."
    show darius at right
    darius "Ugh - I'm so TIRED."
    show mala laugh at left
    mala "Yeah... that was exciting and everything, but..."
    mala sweat "I never want to be excited under these circumstances again."
    hide mala
    show goro at left
    goro @ laugh "You and me both. Great job, team!"
    goro @ smile "I think some special thanks are in order for [player_name] as well."
    darius @ laugh "Seriously! I obviously need to learn some regex myself!"
    hide oliver
    hide darius
    hide goro
    "Everyone grabs their things and begins filing out of the office to get some well-earned rest at home."
    "Just as you're about to leave yourself, Iris calls out to you."
    show iris
    iris "[player_name]. Just a moment."
    player "(Oh no... I thought I actually did WELL today? Did I mess something up?)"
    player "Y-yes?"
    iris "..."
    iris @ smile "Good job today."
    iris "You surpassed my expectations."
    player "..."
    player smile "(Iris... SMILED at me!)"
    player "I'm glad that I could help!"
    iris "Perhaps I was a bit harsh implying that it was a bad decision to hire you."
    iris "Could you meet me in my office tomorrow morning?"
    iris @ smile "I'd like to have a word with you."
    player "O-oh! Sure thing."
    iris "Hurry home and get some rest."
    player "Will do."
    "You gain 20 Renown for saving the day with your regex skills."
    $ player_stats.change_stats(RENOWN, 20)
    return

label v2_paying_it_forward_p1:
    scene bg company1_boardroom with fadehold
    play sound 'audio/sfx/knocking.mp3'
    show iris
    player "U-um Iris? I'm here."
    player "You said that you wanted to see me?"
    iris "..."
    player pout "(Oh no... have I managed to upset her somehow between yesterday and today?)"
    iris "[player_name]... can you tell me about your previous position?"
    player "My... previous position?"
    player "You mean before I became a developer at ConsultMe?"
    iris "Yes."
    player "Well... I used to be a tutor."
    player "I tutored students from elementary to high school, basically."
    player @ smile "The elementary students were probably my favorite, though!"
    iris "I see. Did you like your work?"
    player "..."
    player @ smile "I did. I even miss it sometimes."
    iris @ confused "Oh? Why is that?"
    player "For a lot of the other tutors, it was just a job."
    player "But for me, I saw it as a really special invitation into a pretty personal part of my students' lives."
    player "I wasn't always the best student myself when I was in school. But I had a teacher that really, really believed in me."
    player "I needed money after college, so when I saw a job posting for the position, I realized that this could be a chance for me to have a similar role in the lives of other students."
    iris "Interesting."
    iris "Did you ever have a student that was... PARTICULARLY hard to teach?"
    player "Sure! But that was never a reason for me to quit."
    player "Those students needed me the most. There was one student that I remember the most clearly."
    player "He had a learning disability. I've had students in the past with learning disabilities, but this student had a few."
    player "His dyslexia and ADHD seemed to give him the most trouble."
    player "When he first came to the tutoring center, he was nearly failing his grade."
    player "He was really afraid that he'd need to repeat a year. He always brought up his mom, and how he didn't want her to worry about him."
    iris "..."
    player "What I loved most about tutoring is that I could give my students this sense of power."
    player "They'd come in, completely believing they were powerless against math, or writing, or social studies. But once we were done, they'd proudly show me their good grades."
    player "With this student, I was particularly determined – I used to struggle with my ADHD, too."
    iris "You have a diagnosis?"
    player "Yep! Mom and Dad found out when I was 10."
    player smile sweat "I really, really used to struggle paying attention in class and getting my schoolwork done. My grades were pretty bad, just like my student's."
    iris "... how did you overcome it?"
    player -sweat "Well, ADHD never really goes away, but I was able to cope and make things work for myself thanks to that teacher I mentioned earlier."
    player "She taught me how there are many, many ways to learn, and that all I had to do was find the way that worked best for ME."
    player "Some of my students were great at memorizing from long pieces of text."
    player "Others weren't great at retaining written information, but did really well when they were given videos."
    player "Sometimes those only helped a little, so I'd find games to teach what they needed to know."
    player "For my student, it meant using a combination of those things."
    iris "..."
    iris @ smile "And did you ever find anything that worked for Isaac?"
    player @ smile "We did!"
    player @ laugh "It was so cute, watching his expressions change each tutoring visit, from bringing in D's, to C's, to eventually B's and A's."
    player @ smile "I'll never forget the day he came with his first A, telling me how proud his mother would be..."
    player "..."
    player "... how did you now his name?"
    iris "..."
    iris "I feel guilty sometimes."
    iris "I got so, so close to not believing in him myself."
    iris "I'd just started my job here at ConsultMe. It was my first position as a manager, and I was adjusting to having much longer hours than I did as a senior developer."
    iris "I felt like I was being pulled in every direction. I had less time to spend with him, in the beginning."
    iris "That's probably when his grades started dropping."
    iris "He needed help, but at the same time, the company was just getting started. ConsultMe needed me too."
    iris "So I did the last thing I could think of: I placed him into tutoring after school."
    iris "I was a single parent at the end of her rope. All I could do is trust the tutors at the tutoring center."
    iris "..."
    iris @ smile "... Thank you for believing in my son, even when I fought to find a reason to."
    player "Wait... YOU'RE Isaac's mom?!"
    player "But you're the one that interviewed me!"
    player "So that means you knew -"
    iris "Knew who you were since day one? Correct."
    iris "We had some pretty tough candidates come through to fill this position."
    iris "Still, you beat out at least 3 other developers, all with some form of schooling under their belt."
    iris "It was down to you and one other developer. Your skills and technical interview scores almost matched."
    iris "... I'm not one for nepotism, but I knew that I had to choose you for the role."
    iris "I'd already seen what you were capable of when you put your mind to something."
    iris @ smile "It took some convincing, but as you know, we chose you for the role."
    player "I guess this makes sense in hindsight."
    player smile sweat "I feel like I bombed our interpersonal interview. I was so nervous!"
    iris "You were nervous during your technical interview, true."
    iris "But then I remembered how Isaac would come back to the car, beaming about the “nice teacher lady” that helped him each day. (SMILE)"
    iris "I listened outside of the door for a few sessions to hear you work your “magic”, as he called it. So I knew what you REALLY sounded like when you were confident in what you were doing."
    iris @ disgust "Honestly, your eagerness is impressive, but you got sloppy."
    player "(Aaaaand we're back to normal Iris.)"
    player pout -sweat "..."
    iris @ smile "... It reminds me of myself when I was a junior."
    iris "I can finally take my leave without worrying too much." # Ed: Maybe "move on" instead of "take my leave"?
    player @ surprised "... take your leave? Are you quitting ConsultMe?"
    iris "Yes. I've been extended an offer that I can't refuse."
    iris "I put in my two weeks this morning."
    player "(But... we were just beginning to connect. And now she's leaving?)"
    iris "Of course... we don't HAVE to stop working together. If you'd like to come along."
    player "What? With you? To your new company?"
    iris "Correct. I'll be co-managing with an old colleague of mine."
    iris "I've been telling her all about you. She's interested in interviewing you for a junior DevOps position at her company, Spaghetti Code."
    player "Devops? But I don't know anything about DevOps..."
    player "A-and wait just a minute - I thought I was on a PIP?!"
    iris "There was no PIP."
    iris "I just needed you to tighten up the quality of your work."
    iris "Honestly, do you really think I'd be offering you an opportunity to come with me to a new company if I thought you needed to be on a PIP?"
    iris "My colleague is also aware of your junior status. She initially informed me that they were looking to fill they position themselves. But she said she'd trust my judgment on anyone that I'd like to come along."
    iris "If you're interested, I've created a few mock DevOps tickets for you to make sure you understand the basics."
    iris "You're more than welcome to say no, of course..."
    player "..."
    player "I-I'm not so sure I won't disappoint you again..."
    iris "I don't like giving compliments too often, because I believe they lose their meaning,"
    iris "but you're a great developer, [player_name]. You've done great things so far."
    iris "If I've learned anything about you, it's that when you believe you -"
    iris "- or someone else - "
    iris "can learn something, you do it. Look how far you've gotten? You taught yourself how to program."
    iris "You can do this."
    iris "Come to my office again once those tickets are completed, and we'll move on to the next steps."
    return

label v2_paying_it_forward_p2:
    scene bg company1_boardroom with fadehold
    show iris
    iris "..."
    player "I-I've completed the DevOps tickets."
    iris "... so I've noticed."
    iris "Shall I give my colleague a call?"
    player "I think I'd like that."
    scene bg company1_lydia_cubicle with fadehold
    "That week, you have three rigorous interviews with Spaghetti Code."
    "With bated breath, you wait for the email from your recruiter, informing you whether you received the position or not."
    scene bg living_room with fadehold
    "When you receive the offer letter, your parents couldn't be more proud. You play it cool, just like Iris instructed, requesting a day to think on the offer, despite barely being able to contain your excitement."
    scene bg company1_lydia_cubicle with fadehold
    "The next morning, you sign, and put in your 2 weeks notice at ConsultMe."
    scene bg company1_center with fadehold
    "The whole team is saddened by seeing the two of you go, but Goro is sure to tell you how proud he is."
    scene bg company1_reception with fadehold
    "You realize as you leave ConsultMe, passing its front desk for the final time, that you haven't seen Maria in a while."
    "Perhaps she's off to greener pastures as well."
    scene bg bedroom with fadehold
    "The next 3 weeks crawl by, as you alternate between studying for your new position, and taking a much-needed break."
    return

# start of home stories
label v2_email:
    player "Phew - I'm so glad to be home!"
    player "I got a lot done today. But now that I think about it, I don't think that I got to check any of my emails. I should probably do that before I relax."
    player "Meeting invite... "
    player "Office birthday party..."
    player "Hm... an email from the payroll department? What's this about?"
    player "“To whom it may concern,"
    player "“Our payroll system has experienced a privacy breach at 10:27AM today. To ensure your private information is safe, please click the link below to reset the password to your payroll account."
    player "We deeply apologize for the inconvenience.”"
    player @ pout "Wow! That'd really stink if someone got a hold of my password! What should I do?"

    $ found_problem = False
    menu mysterious_email_choices:    
        "Re-create my password":
            player "I'd better quickly re-set my password before my data is compromised! It looks like they'll need me to log in first."
            player "..."
            player "Strange... The site just keeps loading. Did I do something wrong? Maybe I should refresh."
            player "..."
            player "Oh! I just got an email from our Security Department. Maybe this can wait. I'd better open it."
            player "“Good evening,"
            player "You have failed a routine ConsultMe phishing test. Please email your supervisor no later than 11AM tomorrow to schedule a mandatory security training.”"
            player "What? Phishing? What is that? And why do I need to report for additional training?"
            player "I should look this up."
            player "Okay, here we go - Phishing"
            player "“The fraudulent practice of sending emails pretending to be from reputable companies in order to trick individuals into revealing personal information, such as passwords, credit card numbers, and other private information.”"
            player "Oh no... this means that if this was a real phishing attempt, I would have given away company information. Who knows what a cyber attacker could have done with my data?"
            player "I've got to be more careful in the future. Giving away that kind of information could probably lead me to losing my job, or even compromising my financial information."
            player "But how do I tell a phishing email from a real email? Maybe I should look that up too."
            player "..."
            player "Interesting - it says here that phishing can be detected in a few ways. You can check the sender to ensure that the extension on their email matches the company's professional email."
            player "You can also check the presence and quality of a company logo, and, most importantly, not click any links or attachments in the email unless you're sure of where they're coming from. "
            player "On most computers, you can hover your mouse over the link, and your computer should tell you where they lead to in a tiny window."
            player "I guess I've got to face the music tomorrow. Iris is not going to be happy about this..."
            "You lose 10 Renown. You should be more careful!"
            $ player_stats.change_stats(RENOWN, -10)
    
        "Check the sender's email":
            player "Come to think of it, did this really come from the payroll department? I just ran into Ryan from Payroll during lunch, and he didn't say anything about this."
            player "..."
            player @ surprised "(Gasp!) ryanwebster@ajflke.net... Weird - This isn't a ConsultMe Consulting company email! Ryan Webster does work for the Payroll department, but the end of his email should be @goodvibes.com."
            player "But what does that mean? Should I still go ahead and re-create my password?"
            $ found_problem = True
            jump mysterious_email_choices

        "Inspect the logo":
            player "Before I re-create my password, I should probably make sure that this email has our company branding."
            player "..."
            player "“CompanyNamme”? An email from our company wouldn't have our company name misspelled... And this logo is so small that I almost missed it!"
            player "Plus it's all blurry and pixellated. The logo on all of our other company emails is usually colorful and crisp-looking. It's almost like someone took a screenshot of the logo and used it here."
            player "Hm... should I still re-create my password?"
            $ found_problem = True
            jump mysterious_email_choices

        "Check the domain name":
            player "Like the email says, there's a hyperlink to reset my password. But where does it go?"
            player "I should probably hover over the link before clicking it. It's not good to follow links without knowing where they lead."
            player "..."
            player "Weird! Our company URL is ConsultMe.com, so our reset link should be something like ConsultMe.com/password-reset. This link leads me to company.name.co/pssword-reset."
            player "The links look the same, but they definitely aren't - this link has dots in-between the words in the title of our company."
            player "That feels pretty sneaky!"
            $ found_problem = True
            jump mysterious_email_choices

        "Something's not right here..." if found_problem:
            player "Something's not right here. Now that I think about it, I remember our security specialist telling me about a report button in my email software when I first started. I'll report this email to the Security Department."
            player "..."
            player @ surprised "Oh! Another email? And it's from the Security Department! I'd better open it."
            player "“Congratulations! You've passed a routine ConsultMe phishing test. Your vigilance is appreciated and helps keep our company safe from cyber attacks and security vulnerabilities.”"
            player "Phishing? What's that? Are they talking about the password reset email?"
            player "I'd better look this up."
            player "..."
            player "Here it is; Phishing - “The fraudulent practice of sending emails pretending to be from reputable companies in order to trick individuals into revealing personal information, such as passwords, credit card numbers, and other private information.”"
            player "Oh! So ConsultMe must perform these to make sure that we're staying on our toes about our company's private information! I'm glad I listened to my gut!"
            player "Interesting - it says here that phishing can be discovered in a few ways. You can check the sender to ensure that the extension on their email matches the company's professional email."
            player "You can also check the presence and quality of a company logo, and, most importantly, not click any links or attachments in the email unless you're sure of where they're coming from. "
            player "On most computers, you can hover your mouse over the link, and your computer should tell you where they lead to in a tiny window."
            "You've gained 10 Renown for your sharp eye."
            $ player_stats.change_stats(RENOWN, 10)
    return

label v2_venting:
    player "(Sigh)"
    show mint
    mint "Meow!"
    player "Hi Mint. Am I ever glad to see you! I had a rough day at work today."
    mint "Meow?"
    player "A client complained to Iris today that I didn't complete a task the way that they asked."
    player "They told me that they wanted a custom API built for their project, even though I told them it was a bad idea. It would take the team an extra week if we did it that way instead of just using a public API. "
    player "It would cost them less money, too."
    player "I told the client this, and now we're 3 days into the project and they're demanding that we finish faster."
    player @ worry "I'm just so frustrated..."
    hide mint
    mom "[player_name]! [player_name], what's wrong honey? Are you upset about something?"
    player "(Hm... I am upset. And talking to Mom usually makes me feel better.)"
    player "(I could also post about this on my favorite web development forum. I see people complaining about their jobs there all the time.)"
    player "(I could call Annika too, and see if she has any advice.)"

    menu:
        "Vent to Mom":
            player "Yeah! I'll talk to Mom. She's a great listener, and super supportive. I'll talk to her about it."
            mom "Hi [player_name]! You sounded upset when you were talking to Mint. Did she get into your cookies again?"
            player "Haha! No, but that sounds like something Mint would do!"
            player "I just had a rough day at work. "
            mom "Want to talk about it sweetheart?"
            player "Well, there's this client that wants a custom service added to their website and building it from scratch is going to take around a week."
            mom "I see. So you can't program one?"
            player "I can. It's just that things would go much faster if they used an API, and -"
            mom "An API? What's that?"
            player "!"
            player "Uuuuhh... So, an API stands for “Application Programming Interface”."
            mom "Oh... I see. So it's like a website?"
            player "No, not quite. I mean... websites use them, but..."
            "You and Mom go back and forth like this for a while, and after an hour of trying to explain API's and CRUD requests to her, you decide to call it a night, more frustrated than you were when you got home."
            "It turns out that sharing stories about work requires a certain level of knowledge about what you do to talk about it."
            "Posting to one of your favorite development forums would have accomplished this, but what if someone from your job or even one of your clients saw it?"
            "You sigh. You probably should have called up Annika. She's a developer, but you also know her personally, and there'd be very little risk that what happened at work would be shared outside of just the two of you."
            "You lose 15 Energy thanks to the headache you developed while trying to explain HTTP error codes."
            $ player_stats.change_stats(ENERGY, -15)

        "Vent to Annika":
            player "I think I'll talk to Annika. She's one of my only friends that completely understands the work I do. I'll talk to her about this."
            window hide
            show smartphone at truecenter
            play sound "<to 2.0>audio/sfx/phone_ring.wav"
            play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
            pause 2.0
            hide smartphone

            show annika
            pause 1.0
            annika "Hey accountability buddy! What's up?"
            player "Hey Annika. Do you have a second?"
            player "I've just had the roughest day today."
            annika "Oh no! What was it? Having problems with a coworker?"
            player "No, more like problems with a client! We had this client that wants a custom service added to their website and building it from scratch is going to take around a week."
            player "Is there an API that can do that for you...?"
            player "That's what I said! But get this..."
            "You and Annika talk about what's happening at your job, and she understands completely. She's having a similar problem with one of the Project Managers on her team."
            "You feel much better after having talked to her, and eventually, you hang up the phone feeling a sense of relief."
            player "I'm so glad I got to talk to Annika about what was wrong. It's nice to talk to a fellow programmer about problems at work."
            player "I love Mom, but I have a feeling that she wouldn't've understood what I was talking about if I got into even a little bit of detail."
            player "I'm glad I cooled my head and spoke to Annika instead of going to the internet too! Annika told me about a friend of hers that did that, and one of her managers found her complaining on a popular forum! "
            player "The thought of Iris finding out I complained about a customer sounds scary..."
            "You gain 10 Energy from venting to your friend. You feel much better!"
            $ player_stats.change_stats(ENERGY, 10)

        "Vent Online":
            player "Right, I'll just solve this the way I solve all my other problems - bringing them to the internet! The users on my favorite web dev forum will understand how I feel."
            "You post in one of your favorite, popular web development forums. "
            "Users definitely are understanding; Some even offer tips on how to work with clients like that in the future."
            "All is going well until one of the users checks your post history, and doesn't guess your exact company, but makes a close guess at another consulting company only a few miles away from yours."
            "You start to sweat. What if they guess right? What if they know the client?"
            "You begin to wonder if even the CLIENT could find you on this public forum?"
            "You think to yourself that if you just talked to Annika, a developer that you know personally, this could have been much better."
            "You wouldn't have to be as worried about your identity on the internet being discovered, or a client seeing you vent."
            "You quickly delete the post, hoping that only a handful of people saw it. "
            "You lost 10 Energy out of stress."
            $ player_stats.change_stats(ENERGY, -10)
    return

label v2_running_late:
    player "..."
    show mint
    mint "Mew!"
    player "Ngggh..."
    player "Meow!"
    player "Ugh... What IS it Mint?"
    player "5 more minutes..."
    mint "Mew?"
    player "..."
    player @ surprised "Oh my gosh!"
    player "Mint, is that really what time it is? I'm running late!"
    player "The office opens around 8AM, and I'm typically encouraged to arrive between then and 10AM."
    player "Right now, it's 9:20AM!"
    player "I've got to get ready!"
    "You quickly get dressed, grab your laptop bag, and an apple from the kitchen."
    player "Okay, that's everything..."
    player "It takes around 20 minutes for the bus to get to work, and maybe 20 minutes to walk there."
    player "I could probably make it if I run!"
    mint "... mew?"
    player @ pout "Mint, don't look at me like that..."
    player "I want to make a good first impression my first few months at my first job. I shouldn't be getting there late! "
    player "I could maybe make it if I rush!"
    player "I mean... what else can I really do other than that?"
    hide mint

    menu:
        "Run to the bus stop. You can probably make it!":
            if renpy.random.random() < 0.3:
                player "Okay... okay, I'm going to go for it! I'm sure that I can make it. "
                player "Like I said, I don't want to make a bad impression."
                player "This will be a little more stressful, but I can do it!"
                "You run to the bus stop, making it there in your projected 10 minutes, and just as the bus is arriving!"
                "The bus takes about as long as it usually does to get to the office."
                "You forgot to account for just how long it takes to get to your department from the bus stop and the building's entrance,"
                "But a few more minutes doesn't quite hurt you."
                "You make it in at 10:35AM. You can hear the chatter of the team inside of the break room."
                "It seems that Jenna, the office assistant, has surprised everyone with donuts again."
                "You listen for a moment, sighing with relief when you hear Iris's voice as well."
                "You use this distraction to sneak to your desk, un-noticed."
                "You don't want to make a habit of this. You made it on time, but at what cost?"
                "You lose 5 Energy for your mad dash to the office."
                $ player_stats.change_stats(ENERGY, -5)
            else:
                player "Okay... okay, I'm going to go for it! I'm sure that I can make it. "
                player "Like I said, I don't want to make a bad impression."
                player "This will be a little more stressful, but I can do it!"
                "You run to the bus stop, making it there in your projected 10 minutes!"
                "However, there's a factor that you didn't plan for - the bus is 20 minutes late getting there."
                "You ask the driver what was going on when he arrives. He explains that there were two traffic jams on the highway to your neighborhood."
                "To make things worse, the bus also catches a flat halfway to your job."
                scene bg company1_center with fadehold
                "By the time you arrive at work, it is 12:00PM. Iris does not seem pleased."
                show iris
                iris "Nice to see you actually show up."
                player "*Pant*... *Pant...*"
                player "I'm... *Pant*... Sorry!"
                player "The bus took a lot longer than usual... a-and then the tire... *Pant*..."
                player "As soon as the bus got here, I ran all the way to our sector of the building and the stairs."
                player "It was much faster than the elevator."
                iris "And yet... you're still late."
                player "I'm sorry..."
                iris "You should have messaged me or someone on the team. Can you tell me why that wasn't the first thing that you did?"
                player "(Well, you're super scary, for one!)"
                player "I just thought that it would make everyone upset, and make them lose respect for me, maybe?"
                iris "So you think that wasting half of the day trying to GET to the office was a good use of your time?"
                iris "Did you have your work laptop with you?"
                player "Yes..."
                iris "(Sigh) Then you also could have just worked from home."
                player "I could have WHAT?"
                iris "I usually recommend juniors come into the office as much as possible. It's good to be around your team quite a bit in the beginning."
                iris "I feel that juniors learn more this way."
                iris "But from time to time, when conditions call for it, I'm more than okay with you working from home."
                player "S-so... I didn't have to panic for almost 2 hours?"
                iris "Exactly."
                iris "Get to your desk, please. You've got quite a bit of work to catch up on."
                "You lose 15 Renown for being very, very late."
                $ player_stats.change_stats(RENOWN, -15)
    
        "Message someone in your TeamChat and tell the team you're running late.":
            player "Well... I don't want to be late, but at this rate, I probably will be."
            player "What if the bus is late and isn't there yet by the time I get to the bus stop?"
            player "And even then, what if something stops us on the road on the way to the office?"
            player "Or, now that I think about it - I hadn't even thought of how much time it'll take to get to our department!"
            player "Come to think of it, I noticed that the elevator was receiving maintenance on the way out yesterday."
            player "Our department is on the 5th floor! Can I really rush up the stairs in just a few minutes?"
            player "..."
            player "Okay. I guess I'll just message Goro over TeamChat and let him know I'll be running a bit late."
            player "..."
            player "..."
            player "... Oh! He's replied."
            player "“Sorry to hear that we won't be seeing you in the office this morning like we usually do.”"
            player "“Our office assistant, Irene, even surprised us with donuts today!”"
            player "Dang! I love donuts. I bet there won't be any more by the time I get there."
            player "..."
            player "... WHAT? Is he serious?"
            player "“How long will it take you to get here? 30 minutes? An hour?”"
            player "“Why don't we just make things easy and you can work from home this morning? If you want to come in after lunch, that's fine with the team.”"
            player "Mint... did you hear that?! I can work from home before I go in this afternoon!"
            mint "Meow!"
            player "I can stay HERE , with you! I can work, right here in my room, or the couch, or on the balcony if I wanted!"
            player "This is so, so cool... "
            player "Okay! I may as well make a better breakfast than an apple since I'll be staying home! Come on, Mint!"
            "You gain 5 Energy from being able to work in a familiar, comfortable environment."
            $ player_stats.change_stats(ENERGY, 5)
    return

label v2_family_business:
    mom "Welcome home sweetheart!"
    player "Hi Mom! Is dinner almost ready?"
    mom "Almost - but get this:"
    mom "I got a call from your cousin earlier. I've been talking to your aunt about how well you've been doing at your job,"
    mom "and she spoke to your cousin about it."
    mom "Well, your cousin started learning Python, and decided that she wants to become a software developer, too!"
    player "Wow! Isn't she only a teenager?"
    mom "Yes! She says that she wants to get a head start on her future."
    mom "Can you give her a call later tonight?"
    player "Sure! I remember when I was trying to make that decision, too."
    player "I'll talk over all of her options with her."

    scene bg bedroom with fadehold
    "Later that evening..."
    show smartphone at truecenter
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    pause 2.0
    hide smartphone

    show josephine smile
    pause 1.0
    josephine "... Hello?"
    player smile "Hey Josie! How are you doing?"
    josephine "Hello Cousin [player_name]. I am well." # Ed: Is cousin a title here? Maybe a cultural thing?
    josephine "I heard about your success in acquiring a job in your desired field. Congratulations." # Ed: This seems overly formal for family, but maybe it's Josie's character trait?
    player "Hey, thanks! It was a long road, but totally worth it."
    player "I'm calling because Mom says that you want to do the same thing?"
    josephine "Yes."
    josephine "Last year, I completed my senior year of high school, and –"
    player "What?! You finished? HIGH school?"
    player "I thought you were only 15?"
    josephine "16, actually."
    josephine "I decided to take a gap year. To travel, y'know?"
    player "R-right..."
    player "Jeez, I heard that you were a genius, but this is too cool!"
    player @ laugh "I'm so proud of you."
    josephine blush "Thanks. It's not THAT big of a deal..."
    josephine -blush "You say that you're impressed, but I'm impressed by YOU."
    josephine "Momma spoke about how you made a plan and pursued your future. Even though you lacked formal training."
    josephine "So I decided to start learning Python. I didn't realize it would be this interesting!"
    josephine "While building small projects has been fun, I'm not sure where to start as far as doing this stuff professionally."
    player "A profession? A-Aren't you a little... YOUNG to be thinking about employment?"
    josephine "It's never too early to start working on your future! I wanna be a powerful working professional one day, and an early start is right here in my 5-year plan."
    josephine "I WILL be 18 by the time I'm done, so I'll be able to work." # Ed: If Josie is 16, then she'll be 18 in 2 years, not 5. Unless she started her 5 year plan earlier? Maybe it'd be better to say that she'll be over 18 by the time she's done, so she can work?
    josephine "Anyway, I know college is an option, but I've also read that I can learn a lot of this stuff on my own?"
    josephine "Which brings me to the biggest question I want  answered: Which path should I take?"
    josephine "My mother and father want to discuss financing and time commitments." # Ed: Do Josie's parents want to discuss financing and a timeline because they expect her to go to college? Or because they want to help her with her 5 year plan and are supportive of that? Maybe it would be better to say something like "My parents want me to explore my options, and find out how much time and money will be involved."
    player "Are they aware of your... um... “5 year plan”?"
    josephine "..."
    josephine blush "Momma and Vati want me to be happy."
    josephine "They are phenomenal parents. They have always supported my pursuits, even when they do not understand."
    josephine "I want THEM to be happy."
    josephine "I want them to be proud of me."
    player smile "Well, how about we go over what your options are, and we can talk about which one sounds best for you?"
    josephine -blush "Thanks, Cousin [player_name]! You're the best."
    josephine "What are my options?"

    default v2_family_business_choices_visited = set()

    menu v2_family_business_choices:
        set v2_family_business_choices_visited

        "Computer science degree":
            josephine "Oh right! Vati told me all about college, and even found one nearby I might be able to go to if I go this route."
            player "Yep! From what I understand, there's a four-year degree that you can get in computer science."
            josephine "Why don't colleges just call it a programming degree?"
            player "Well, that's because it's not SPECIFICALLY a programming degree."
            player "Programming is definitely a part of the curriculum, but computer science is kind of an all-encompassing degree."
            player "You learn about the history of computers, how they and programming languages work on a deep level, and a lot of other stuff."
            player "It also involves a lot of math."
            josephine "Ew."
            josephine "I'm GOOD at math and everything..."
            josephine "But I still hate it."
            player "I'm not a fan of advanced mathematics either!"
            player "But it can be really useful in certain jobs within this field."
            player "Thankfully, most of them don't require any math at all, really."
            player "Plus, if you have a college degree, you can negotiate a much, much higher starting salary than I could!"
            josephine "Alright... and how much would a computer science degree cost?"
            player "That depends heavily on where you're going to school, and what country you're in."
            player "In the US, for example, some community colleges are fairly affordable with government assistance."
            player "But state and private universities might get really expensive."
            josephine "I see... so I could learn a lot, and a degree will help me get a higher salary in the beginning of my career,"
            josephine "but it could be very expensive."
            player "That's right. It's a lot to think about!"
            player "Something else that's cool to consider, though, is that some jobs will pay for you to go to college."
            josephine "... That doesn't make any sense. I can go to college AFTER getting hired? Isn't a college degree what will help me get hired in the first place?"
            player "It sounds silly, but sometimes companies need you to learn something specific. They'll pay for college classes so you can learn that specific thing well."
            player "And sometimes companies will pay for your whole degree! It's a way of investing in their employees."
            josephine "I see... so it may be possible for me to learn to program on my own, get a job, then attend college for free?"
            josephine "Which will help me negotiate higher pay in future positions?"
            player "That's right! It's another route that you can take instead of going straight into college."
            jump v2_family_business_choices

        "Software engineering associate's degree":
            josephine "... Isn't this just a computer science degree?"
            player "Not quite!"
            player "In a software engineer associate's degree, or a web development associate's degree, you study the specific skills you need for those positions."
            josephine "Gotcha. How long does it take?"
            player "An associate's degree is usually only 2 years! So you can finish a lot faster."
            player "Associate's degrees are usually more affordable, too."
            josephine "Hm... that fits right into my 5 year plan~"
            player "You and that 5 year plan again... (SWEAT)"
            jump v2_family_business_choices

        "Self-teaching":
            josephine "So... Mother says that you taught YOURSELF how to program?"
            josephine "What's THAT like?"
            player "It was a lot of hard work!"
            player "Though, to be fair, however you learn programming, it's going to be a lot of hard work..."
            player "But self-teaching worked best for me."
            player "I had a part-time job at the time because I needed to pay my bills, but also needed time to study."
            player "I found this awesome online community that with lots of people to help me out. It has lessons on almost anything you can think of that involves programming."
            player "The best part is that it's free!"
            josephine "That sounds pretty cool! What was hard about it?"
            player "Definitely having the discipline to keep on studying."
            player "There were so many times that I wanted to quit. And nothing was stopping me."
            player "What helped was keeping my goal in mind, and spending time with other people who were on the same path as me."
            player "The users on the forums I hung out in were really helpful about staying motivated. And I made a lot of cool friends!"
            josephine "Wow... so what's the name of this resource?"
            player "I learned to code on freecodecamp.org!" # Ed: Would it be better to use the name freeCodeCamp here rather than the URL?
            josephine "I'm writing this down. I may need to spend a bit of time there tonight."
            player "I think that's a GREAT idea! It's a good thing to do, even if you end up going with a different option to learn."
            player "They have so many different lessons there, so you can get a good idea of what kind of programming you'd like to learn for work."
            player "That's another great thing about freeCodeCamp - one of the hardest parts of teaching yourself to program, aside from self-motivation, is not knowing what to study."
            player "It's super easy to lose a few weeks or months on languages or technologies that aren't right for the kind of work you want to do."
            player "freeCodeCamp actually has entire tracks and learning paths carved out for you so you know exactly what to study."
            player "And, if you ever decide you want to go the self-taught route and aren't sure about what to focus on, you can always give me a call."
            josephine "Thanks [player_name] - that's so sweet!"
            player "What is family for? I'm so proud of you for thinking about your future!"
            jump v2_family_business_choices

        "That's about it!" if len(v2_family_business_choices_visited) > 1:
            pass

    player "So did that help at all?"
    josephine "It definitely did! I think I have a better idea of what some of my options are."
    josephine "Mom and I are going to have a lot to talk about. Graduation is only a few weeks away!"
    player "Oh jeez! It seems like we talked at the perfect time, then."
    josephine "Thanks again [player_name]. This is all really, really scary."
    josephine "It almost doesn't seem real that I'm about to start making decisions for my future."
    josephine "Especially programming. It's new and exciting, but I'm not sure if I'm ready to do this on a professional level."
    player @ laugh "Haha!"
    josephine "..."
    josephine "What's so funny? I'm spilling my guts to you here."
    player "It's just so funny."
    player "Because I said the SAME THING when I first started learning!"
    josephine "Really?"
    player "Yep! And it's just a little silly to think that I'm telling you what someone else told me."
    player "And that one day, you'll probably be telling a newbie the same things, because they'll feel the same way."
    player "But as long as we keep lifting while we climb, we'll all be okay."
    player "I'll be here supporting you, whatever you decide to do."
    josephine "... Thanks [player_name]."
    player "No problem!"
    "You're so proud of your cousin! You gain 5 Energy from the nostalgia you experience from talking to a potential new developer."
    $ player_stats.change_stats(ENERGY, 5)
    return

label v2_fresssh:
    player "I'm home everyone!"
    player "Now that I'm back, I can check my favorite Greddit group, the LearnProgramming forum!"
    scene bg bedroom with blinds
    show mint
    mint "Meow?"
    hide mint
    player "People like to help each other out with programming problems that they have."
    player "Sometimes, they even post articles and news about updates in programming languages or other new, cutting-edge technologies!"
    player "Hm... what's this?"
    player "Users Surfer90210 and BroDoYouBingBong are talking about some technologies I've never heard of?"
    player "Hm... I see..."
    player "According to BroDoYouBingBong, all developers should know how to use BingBong at least a little..."
    player "And Surfer90210 is talking about a new framework called Fresssh. Why so many S's?"
    player "Looking them up, both of these seem so cool. Maybe those two are right, and these technologies are the future..."
    player "Plus, I can tell Goro all about them, and maybe we can start using them!"
    player "On the other hand, I heard Goro talking about how on our next project, we're going to be using something called Material UI."
    player smile "Maybe I need to learn something like that so I can really help out the team."

    menu:
        "Learn about BingBong technology and Fresssh.":
            player "Okay,"
            player "So it seems that a lot of people can't seem to agree if BingBong is going to be a big deal or not..."
            player "But Fresssh seems pretty cool! Following this tutorial, I managed to make a tiny application."
            player "I bet we can find lots of places to use this at work."
            player "I should message Goro and tell him about what I learned!"

            scene bg laptop_screen night with blinds
            play sound 'audio/sfx/social_media_notification.wav'
            show goro smile
            goro "Hey [player_name]! Staying at the office a bit late?"
            player "No, I just got back home!"
            player "So I was on this forum that I really like, and I read about some users talking about BingBong, as well as this new framework..."
            "You send over pictures of the small webpage that you made using Fresssh."
            "You also explain how you think that it and BingBong could be really useful to the team."
            goro "That's really cool that you're doing research during your free time."
            goro "It's definitely something that good developers do."
            goro "Unfortunately... I don't think that these technologies will be really useful to us."
            player "Aw man, really? Why?"
            goro "For one, Fresssh, even though it seems pretty cool, is super new. "
            goro "Like, it's fully-released version came out about 6 months ago."
            player @ surprised "Six MONTHS ago?"
            goro "Yes. Which means that there's barely any documentation on it."
            "You do a quick Schmoogle search and sure enough, the only documentation you can find on Fresssh is on the official documentation page and Fresssh's Youtube channel."
            goro "What happens if you need to debug something? What if there are some bugs that even the developers of the framework haven't figured out or noticed yet?"
            goro "There doesn't seem to be any communities surrounding this online yet either."
            goro "Companies tend to pick frameworks that have been around for at least a little while for these reasons."
            player "I see..."
            goro "Similarly, BingBong hasn't been adopted by many major companies either."
            goro "We could certainly use it, but there are far, far fewer BingBong developers than, say, Ruby on Rails developers."
            goro "If the client ever needs help in the future to fix a bug in the system we built, and we're not the ones to do it, how will they find people that can do it?"
            goro "Does that make sense?"
            player "It does. I'm sorry!"
            goro "No need. This is a learning experience."
            goro "Just understand that in the future, as you develop your skills as a junior, you'll generally want to stick with popular technologies."
            goro "Once you've gained your footing in this field, you should feel free to venture off the beaten path. The sky will be your limit!"
            goro "But for now, we need you down on the earth with us, okay?"
            player "Okay. I understand..."
            "You lose 10 Energy from the realization that after studying these two frameworks, you won't be able to use them any time soon."
            $ player_stats.change_stats(ENERGY, -10)
    
        "Learn a little bit about Material UI.":
            player "Okay..."
            player "So according to my search results, Material UI is something called a component library."
            player "It's got lots of pre-built visual components like slide carousels and navbars."
            player "So I guess we're going to be using this on our next project's frontend!"
            player "It'll probably make building a frontend even faster, not having to do anything from scratch!"
            "You spend a little bit of time on a Material UI tutorial, and before you know it, you've whipped up a little mockup."
            player "Using this at work will be pretty straightforward."
            player "I should message Goro and tell him about what I learned!"

            scene bg laptop_screen night with blinds
            play sound 'audio/sfx/social_media_notification.wav'
            show goro smile
            goro "Hey [player_name]! Staying at the office a bit late?"
            player "No, I just got back home!"
            player "I looked up Material UI. It looks like a lot of fun!"
            player "I even did a tutorial, and made something really quick!"
            goro "Really?"
            goro "That's great! That's the kind of enthusiasm we like to see."
            goro "No one on the team has ever used it yet. I'd love it if you could give a minor presentation on what you've learned!"
            player "I'd be glad to!"
            goro "Great. Keep this up, and you'll always be an asset to the team."
            "You gain 10 Renown for thinking ahead."
            $ player_stats.change_stats(RENOWN, 10)
    return

# start hackerspace stories
label v2_old_friend:
    player "This place is as busy as always!"
    player "I wonder if that “Moms Who Code” group finished their Hackathon project? I should go see!"
    greg "[player_name]? [player_name], is that you?"
    player "Oh my gosh, Greg! I haven't seen you since high school!"
    player "How have you been?"
    greg "I've been great, how about you? It's crazy to meet you here in HackerSpace!"
    greg "Are you a programmer too?"
    player "I am! I actually just landed my first software development job! I'm a junior developer at ConsultMe."
    greg "ConsultMe? Man, I love that place! I've heard awesome things about their company culture."
    player "Yeah, I still can't believe I landed the position sometimes! Where do you work?"
    greg "Um... well, I used to work at DevCo LLC, but I don't work there anymore. I'm currently looking for work."
    player "Oh jeez, I'm sorry to hear that!"
    greg "It's okay. Stuff happens, y'know?"
    greg "It's been ages since I've seen you though - let me grab us some coffee and we can sit down and catch up!"
    player "That super nice of you, thanks! I'll wait here for you."

    show layla with moveinleft
    layla "Did I just overhear that guy tell you that he's looking for work?"
    player "Yeah, that's Greg. We used to go to high school together."
    layla "Isn't ConsultMe hiring? You may want to think about referring him!"
    layla "You'll get more out of it than just helping a friend get a job."
    player "What do you mean?"
    layla "Most companies have incentives to get existing employees to refer developers that they know to help them find new hires."
    layla "Hiring developers is expensive and time-consuming, so when you bring a good candidate to your company, usually you can get paid for it!"
    layla "I referred a developer that I knew from a gardening club that I'm in, and once they got hired, my company gave me about $3,000! Just for giving them my colleague's information!"
    player "Wow! That's a LOT of money for just passing information on. Do you think I should refer Greg?"
    layla "Maybe! You should talk to him about it. I've got to run and meet up with a client in one of the meeting rooms here, but I thought I'd drop by and say hello. "
    layla "Good luck!"
    hide layla with moveoutright

    scene bg hacker_space with blinds
    greg "Hey! Sorry for the wait. These developers love their coffee, so the line was super long!"
    player "Always! Lots of people in my office can't start their day without it."
    player "So, Greg..."

    menu:
        "Would you like me to refer you to a position at my company?":
            player "I've been thinking, and ConsultMe has another junior position open right now. Would you like me to refer you to it?"
            greg "What? No way, you'd do that for me [player_name]?"
            player "Of course, you're my old friend! I'd be glad to put in a good word with our team lead, Goro."
            greg "You'd be doing me a huge favor, thank you! The job market has been a little rough, so being able to get my foot in the door would be great!"
            player "Awesome! I'll send in my referral email first thing in the morning."

            $ calendar.next_weekday()
            scene bg company1_center with fadehold
            "Some time later..."
            show iris
            iris "So. Would you mind explaining yourself?"
            player "(It's so early... is Iris already mad at me?)"
            player "Hi Iris. What am I explaining?"
            iris "We had an interview scheduled for your friend... Greg, was it?"
            player "Oh right, Greg! How did it go?"
            iris "Great. If you think showing up 15 minutes late to your first interview with a very loose tie and mis-matched socks is good, then great. Really great!"
            player "Oh jeez... did he at least interview well?"
            iris "I've never been called “dude” so many times in my life by one person."
            iris "When we asked him about noteworthy skills, he explained, in GREAT detail, how he ate 30 pieces of pizza on a dare once in college."
            iris @ disgust "He also likes drinking Ranch with his pizza."
            player "I see."
            player "Wait."
            player "You mean... PUTTING ranch ON his pizza, right?"
            iris "I know what I said."
            player "..."
            iris "The next time that you think about referring someone to the company... do spend a bit more time vetting them before sending in their resume, please."
            "You lost 15 renown for your shifty friend's behavior."
            $ player_stats.change_stats(RENOWN, -15)

        "If you don't mind me asking, why are you looking for a job?":
            player "If you don't mind me asking, why are you currently looking for a job?"
            greg "Weeeell, it's kind of a long story."
            player "I've got time! What's going on?"
            greg "Well, maybe it's not that long... you see, I got put on a PIP."
            player "Oh no - that stands for Personal Improvement Plan, right?"
            player "Don't you get those when you're not performing in some way at work?"
            greg "Sometimes, yes. In my case, I was performing pretty well - or at least, I think so."
            greg "My problem was that I was late to work. A lot. I missed a lot of meetings, and it was starting to affect my work."
            player "Wow - was your commute too long? I know sometimes in the mornings, my commute can take me an hour on a day with really bad traffic."
            greg "Not quite... I uh... worked from home."
            greg "Heheh..."
            player "(Hm... come to think of it, Greg was always kind of a slacker in high school.)"
            player "(He'd sleep in class, and turn in assignments late. I'm not super surprised that he got put on a PIP)."
            player "So you got fired?"
            greg "Actually, I quit before I could get fired so it wouldn't reflect poorly on me when I interview with other places."
            greg "But for the time being, that still means that I don't have a position."
            greg "I know what you're thinking “That sounds like the same Greg I used to know”.  But things have been different!"
            player "(That's EXACTLY what I've been thinking...)"
            greg "I actually started going to the gym in the mornings lately, so I'm getting used to waking up at a set schedule so I don't repeat my mistake."
            player "That's good! Working out and getting my blood pumping always helps wake me up."
            player "Well Greg, it's getting a bit late - I should probably get home."
            player "Good luck with finding a new job! I hope that I can at least keep seeing you here at the HackerSpace?"
            greg "Definitely! It's a great place to network. You never know where your next gig will come from!"

            scene bg hacker_space_cafe with blinds
            show layla
            layla "So, are you going to recommend Greg?"
            player "No, I actually just have a bad feeling about it... Greg was always kind of a slacker in school. What happens if he hasn't changed?"
            layla "That's a good point. If he comes into an interview late and bombs it, or even gets hired but never comes in on time, that's a bad look for you."
            player "Right. I figured I'd better just play it safe."
    return

label v2_equity:
    player "I wonder what's going on in the HackerSpace today?"
    player "Hm... Oh look, there's Layla! And she's talking to someone, but she looks pretty upset."
    player "I wonder what's going on?"
    show layla
    layla "I'm telling you, you're wrong. If you're going to be a good developer, you've got to change your way of thinking."
    high_school_student "I feel like you're making a big deal out of nothing. I've never even seen this happen in real life."
    player "Sorry to butt in, but what's going on here?"
    layla "This young man asked for some help on his project for school."
    layla "We were looking over his code, and I noticed there wasn't a lot in his frontend's markup for accessibility."
    layla "He doesn't believe that that's necessary, and that he should just turn in his assignment as-is."
    high_school_student "I just don't understand what the point is? My site looks great."
    layla "The point is that even though we're able to see, there are blind and visually-impaired users that you'll have to take into account."
    high_school_student "What's there to change? I was just telling her that I've never seen a blind person using a phone or a computer. What would they use a phone for besides calling people?"
    high_school_student "How would they even use a phone to call people if it isn't a flip-phone? The buttons on a phone-screen aren't even solid!"
    layla "What do you think [player_name]? What should he do?"

    menu:
        "Accessibility is important.":
            player "Accessibility is important!"
            player "One of the students that I used to tutor in my last job had a smartphone, and it had some really cool accessibility features!"
            player "Computers and phones usually have screen-readers on them, which is special software that reads content on a screen out loud."
            high_school_student "Oh yeah? Well what happens when they get to a picture? Pictures aren't text, and my website has lots of pictures on it."
            layla "That's why it's important to use your aria-labels on visual elements like buttons, and alt-text on images."
            layla "When a screen-reader reaches an image, it usually reads out the word, “Image”, and whatever you've put into Alt-Text."
            high_school_student "Wow... so I guess in that way, visually impaired and blind people actually can use computers and phones?"
            player "Absolutely!"
            layla "I read that there is even software for visually impaired software developers to code just like those without visual impairments."
            layla "Just because it doesn't affect you doesn't mean it won't affect others."
            layla "I'm making such a “big deal” because it's good for you to get in the habit of doing these things now before you're working on big projects that others will be using in the future."
            high_school_student "Fine... maybe you're right. Can you remind me again which attributes I should be using so I can go in and make changes?"
            layla "I'd be happy to!"
            "You gained 10 renown. Good job working towards a more equitable world!"
            $ player_stats.change_stats(RENOWN, 10)

        "It's just for a school project Layla. Maybe it isn't that big of a deal?":
            player "I don't know Layla... this is just for a school project? Maybe it isn't that big of a deal?"
            layla "What? [player_name], don't you remember Lamont?"
            player "Lamont? ... Oh!"
            layla "There it is. So you DO remember Lamont."
            layla "You told me about him one day a few months ago. [player_name] here had a visually impaired student that she used to tutor."
            layla "He used a phone with a screen-reader, a special piece of software that read the content on his screen out loud."
            player "That's right... he was a really good student."
            layla "I'm sure he got the chance to be because the sites that you sent him to for study materials were screen-reader friendly."
            high_school_student "Oh yeah? Well what happens when they get to a picture? Pictures aren't text, and my website has lots of pictures on it."
            layla "That's why it's important to use your aria-labels on visual elements like buttons, and alt-text on images."
            layla "When a screen-reader reaches an image, it usually reads out the word, “Image”, and whatever you've put into Alt-Text."
            high_school_student "Wow... so I guess in that way, visually impaired and blind people actually can use computers and phones?"
            layla "[player_name], what would Lamont say to you if he heard what you said earlier?"
            player "Jeez... his feelings would probably be really hurt."
            layla "Exactly. "
            layla "Just because it doesn't affect the two of you doesn't mean it won't affect others."
            layla "I'm making such a “big deal” because it's good for everyone to get in the habit of doing these things now before you're working on big projects that others will be using in the future."
            high_school_student "Fine... maybe you're right. Can you remind me again which attributes I should be using so I can go in and make changes?"
            layla "I'd be happy to!"
            "Layla seems disappointed. You lose 10 Renown."
            $ player_stats.change_stats(RENOWN, -10)
    return

label v2_gelato:
    show layla at left
    show annika at right
    player smile "Hey Layla! Annika!"
    layla "Hey! Did you get the new Hackerspace newsletter?"
    player "No, I haven't checked it recently, why?"
    annika "There's a gelato place RIGHT next door now!"
    player "Wow, I love gelato!"
    layla "Wanna go grab some?"
    "You're just about to say yes when you hear a few voices behind you."
    "Two developers seem to be discussing a project at work."
    developer1 "So you said that you guys are using Flask?"
    developer2 "No, we're using Django on this project. We needed something bigger."
    developer1 "I've been wanting to ask forever - so what's the difference between Django and Flask?"
    developer2 "So flask is basically - "
    "You turn around again to Annika and Layla, the two of them now discussing their favorite gelato flavors."
    player "(Hmm... On one hand, I've had a long day at work today, and would love to take it easy with something cold and sweet.)"
    player "(On the other hand, our most recent meeting at work covered a client that we'll be taking over from another company.)"
    player "(They need maintenance on their larger app written in Django, and the creation of a smaller app written in Flask.)"
    player "(I bet asking if I can listen in on their conversation would help me understand more!)"
    player "(What should I do?)"

    menu:
        "Go get gelato with friends.":
            player "..."
            annika "Hey! Earth to [player_name]! Are you coming?"
            player "Oh! Absolutely!"
            player "My favorite flavor is Pistachio."
            layla "Pistachio??"
            annika "Ewww!"
            "You decide to have gelato with your friends. It's important to have downtime every now and then!"
            "If you really need to research about Flask or Django, you can do it during a bit of downtime at work tomorrow."
            "You gain 10 Energy for taking time with friends."
            $ player_stats.change_stats(ENERGY, 10)

        "Pardon myself and learn more about Flask/Django":
            player "Hey guys? Have either of you ever worked with Flask or Django?"
            layla "Hm... I've used Flask a bit before, but I've never used Django."
            annika "My job uses Django, and I'm learning, but I've never heard of Flask."
            player "Well, those two over there are talking about it! One of them just started explaining the difference between the two."
            player "Want to join their conversation?"
            annika "Sounds like a blast!"
            layla "Let's go - maybe we can invite them to grab gelato with us when we're done!"
            "The three of you approach the two developers and bring up their earlier conversation."
            "The first developer offers you all an in-depth explanation of the two frameworks."
            "You feel much more prepared to follow the conversation at work tomorrow!"
            "Your conversation leads into other topics, and you all don't quite have enough time for gelato,"
            "but you've learned a lot!"
            "You gain 10 Renown points."
            $ player_stats.change_stats(RENOWN, 10)
    return

label v2_internet_safety:
    show layla
    layla "Hey there!"
    player "Hi Layla! Wanna take a look at the community board and see if any good talks are coming up?"
    layla "That sounds like a good time! I missed the React talk last month, so I've been trying to check more often."
    player "Cool! I've been meaning to pick up Angular, so I hope they have a seminar on that ne-..."
    player "..."
    layla "[player_name]? Everything okay?"
    player "I'm just remembering..."
    player "I forgot to get a React ticket submitted today!"
    layla "Oh no! Was it urgent?"
    player "It kind of is. I finished pretty much all of it, but I forgot to commit my code!"
    layla "Well that can't be too hard, right? I don't mind waiting for you while you get that finished up."
    player "Really? Okay!"
    player "All I need now is a wifi connection."
    layla "Oh, I have the wifi password! It's pebcak2022."
    player "Pebcak? Someone at work said that word last week. I still don't know what it means."
    layla "Hehehe..."
    player "Well, I guess I'll get connected and end this so we can get back to what we were doing."

    menu:
        "Connect to the Hackerspace wifi and commit.":
            player "Done! Now we can get back to the community board before all of the pamphlets have been taken - "
            layla "Wait, hold on,"
            layla "when you committed just now, were you connected to a VPN?"
            player "A VPN?"
            layla "Yeah - they're pieces of software that can protect private information on your computer when you're connected to wifi, and hide you from others on the same network."
            player "Why would I want that?"
            layla "Getting on wifi in public spaces can be risky. It's one thing to do it on your personal computer - "
            layla "though you really shouldn't do that either -"
            layla "but it's another thing entirely when it's a work laptop. You could have important private information stolen from your computer."
            player "..."
            layla "It might be okay!"
            layla "Just having been on a public network doesn't mean you definitely got information stolen. But it definitely does open you up to the risk."
            player "How do I even get a VPN?"
            layla "Usually your company has one that they like to use."
            layla "There are lots of ones that you can pay for yourself, but you should probably go with one your job already has a membership with."
            player "Aw man... I really, really hope nothing happens..."
            layla "(sigh) Best not to let it worry you too much now. Your code has already been committed."
            player "Yeah. I guess you're right."
            "You lose 10 Energy, worried about your private information."
            $ player_stats.change_stats(ENERGY, -10)

        "Wait until work tomorrow to commit.":
            player "I dunno... I don't want to stress too much. Maybe I can just commit tomorrow?"
            layla "If you say so! What VPN does your company use?"
            player "VPN?"
            layla "Yeah - they're pieces of software that can protect private information on your computer, and hide you from others on the same network."
            player "Why would I want that?"
            layla "Getting on wifi in public spaces can be risky. It's one thing to do it on your personal computer - "
            layla "though you really shouldn't do that either -"
            layla "but it's another thing entirely when it's a work laptop. You could have important private information stolen from your computer."
            player "Oh jeez! So it sounds like I really should wait until tomorrow anyway! I don't have one."
            player "How do I even get a VPN?"
            layla "Usually your company has one that they like to use."
            layla "There are lots of ones that you can pay for yourself, but you should probably go with one your job already has a membership with."
            player "Gotcha! I'll make sure that I message our IT team first thing in the morning and put in a request for one."
    return

label v2_where_to_start:
    "It's as busy as ever at the Hackerspace."
    "You scan around the room looking for a familiar face and spot Layla and Annika sitting at a table by the vending machine."
    show layla at left
    show annika at right
    "As you slide into a seat and greet your friends, a young man approaches, no older than 18."
    teen "H-hello."
    annika "Hey, what's up? Are you new here?"
    teen "Kind of... I've been coming for a few weeks now after school. I've been mostly scoping the place out."
    layla "That makes sense - it can be a little nerve-wracking in a busy place like this! But everyone's mostly really nice."
    teen "Right - that's why I came to talk to the three of you!"
    teen "Almost every day I come here, I see one of or all of you sitting and talking with newbies or other developers."
    teen "I've started to teach myself to code a few months ago. I'm really close to graduating high school, and I like coding a lot!"
    player "That's awesome! I taught myself how to code too - it's a lot of hard work, but it's definitely worth it!"
    teen "It's definitely been difficult, but I can't seem to put my laptop down once I've really gotten into a bug!"
    layla "Haha, if getting caught on a bug EXCITES or CHALLENGES you more than it makes you want to quit, you're definitely going into the right field!"
    teen "Well, that's what I came over to ask about - "
    teen "I've been reading a lot of articles online to learn what I need to do to start looking for a real job in the field, since I graduate in about six months."
    teen "All of them say that you need a portfolio. I just don't really know what I should be putting into one."
    annika "[player_name], you're the one who's gotten into the field most recently out of the three of us."
    annika "Maybe you should answer this one! Since it's so fresh?"
    player "Er, sure! So you just need an idea of the types of projects you should be making?"
    teen "Yep!"
    player "And what type of programming job would you like?"
    teen "I've researched a lot, and I want to go into web development!"
    player "Hm... Well, if you're preparing projects for a portfolio, you should make sure your projects..."

    menu:
        "...are as visually appealing as possible":
            player "... because if your projects don't look great, potential employers won't take you seriously!"
            teen "Wow, really?"
            teen "I had no clue!"
            player "Yep! So make sure you spend as much time on your frontends as possible."
            teen "Got it! I'm going to grab some coffee, find a comfortable spot, and get started on my portfolio!"
            "Annika and Layla share a look. They both look concerned."
            "Layla quickly whispers something to Annika, and they both nod."
            layla "... hey, you said you're going to grab some coffee?"
            layla "I could use a cup too. Why don't I come with you?"
            teen "Sure!"
            "The two of them walk off, the budding developer excitedly talking about his latest project."
            annika "Hey [player_name], did you really mean what you said a few minutes ago?"
            player "Sure! I mean, I wish I spent more time on the frontend of my projects, so I thought I'd tell him to do the same."
            annika "I see..."
            annika "I just ask, because I definitely wouldn't say that that was the most important thing that he should have been focusing on."
            player "Oh no! What should I have said instead?"
            annika "I mean, think about it:"
            annika "The point of having a portfolio as a developer with no experience is to show a potential employer that you know how to do what they need you to do on the job."
            annika "So a project in a portfolio should show off all of the basic skills of a junior developer."
            player "What do you have in mind?"
            annika "Well, during my interview process, I was asked to describe MVC, and how it worked."
            annika "I was also asked to explain how HTTP requests work."
            annika "So, I would use projects that have a good frontend and a backend that either I made, or an API that I've called."
            annika "That way, they'd know that I know how to make HTTP requests or APIs."
            annika "Having a really attractive frontend doesn't necessarily say anything about your skill as a programmer."
            annika "It'd probably help if you were going for a UX/UI position, it'd be completely fine..."
            player "... but he said he wanted to be a developer."
            player "Sheesh! That's so embarrassing!"
            annika "It's okay! We're only juniors."
            annika "It's just best for new devs to focus on showing off their skills and the functionality of their app rather than how they look,"
            annika "or using a million technologies, or things like that."
            player "So I just told that guy something wrong... What if he follows my advice?"
            annika "Don't worry - Layla's having a chat with him to set him straight."
            annika "So it's okay!"
            "You lose 10 Energy out of embarrassment."
            $ player_stats.change_stats(ENERGY, -10)

        "...have a few cool features, and use at least one API":
            player "... because it's all about showing potential employers what you can do."
            teen "Really? What do you mean by that?"
            player "When I was looking for my first position, I had to work on a portfolio too,"
            player "and I wanted a million features, and I wanted to use a million different technologies, and spend hours making the app look just right..."
            player "But then one of my mentors that I met in freeCodeCamp's forums told me that the most important thing is to create projects that acted as PROOF that my skills matched the job description."
            annika "That's right!"
            annika "I've gotten to sit in on a few interviews at my job, and we look to portfolios the most when an applicant doesn't have any other work experience."
            annika "So because you want to become a web developer, you should build a project that shows that you have web development fundamentals down."
            layla "Yep! That's why [player_name] mentioned using at least one API. A web developer should know how to call on API's (and how to build them for good measure)."
            layla "As far as having a few cool features goes, when I interview applicants at the nonprofit, we'll often get applicants in our junior positions with lots of projects."
            layla "But the funny thing is: They're rarely ever finished!"
            teen "Really?"
            teen "Hm... So it's not good to go into an interview with an unfinished project?"
            layla "No, no, that's definitely fine! It shows that you still have things that you're working on so that you can improve your skills."
            layla "I'd just recommend two complete, fleshed-out projects with cool features to 10 unfinished projects."
            layla "Simply FINISHING a project or two will put you ahead of other applicants..."
            teen "Gotcha! Okay, so I just need to make sure that my projects are finished! That shouldn't be too hard."
            teen "But... how do I come up with ideas for good projects?"
            layla "Good question! Do you have any advice for them, [player_name]?"
            player "Well, some of the best advice I've ever heard is that it's best to make a project that does something that you hate doing."
            player "You come up with a solution to a real problem - a real problem that you're intimately familiar with!"
            teen "Yeah... yeah! And I'll definitely finish if I'm solving my own problem."
            teen "Thanks [player_name]! Can I come back if I have more questions?"
            player "Of course!"
            "It feels great to help new developers get where they want to be even faster than you were able to!"
            "You gain 5 Renown for paying it forward."
            $ player_stats.change_stats(RENOWN, 5)

        "...have as many features and technologies as possible":
            player "... because if you know lots of technologies, the chance of you getting a job is much higher!"
            player "Plus, having a ton of features will really show off your versatility."
            teen "Wow, really?"
            teen "I had no clue!"
            player "Yep! So make sure you really get to studying so you can be a jack of all trades!"
            teen "Got it! I'm going to grab some coffee, find a comfortable spot, and get started on my portfolio!"
            "Annika and Layla share a look. They both look concerned."
            "Layla quickly whispers something to Annika, and they both nod."
            layla "... hey, you said you're going to grab some coffee?"
            layla "I could use a cup too. Why don't I come with you?"
            teen "Sure!"
            "The two of them walk off, the budding developer excitedly talking about his latest project."
            annika "Hey [player_name], did you really mean what you said a few minutes ago?"
            player "Sure! I mean, I feel like I got really lucky landing this job, since I only know about 4 or 5 technologies."
            player "I bet I could have gotten even more interviews if I knew 9 or 10!"
            annika "I see..."
            annika "I just ask, because I definitely wouldn't say that that was the most important thing that he should have been focusing on."
            player "Oh no! What should I have said instead?"
            annika "I mean, think about it:"
            annika "The point of having a portfolio as a developer with no experience is to show a potential employer that you know how to do what they need you to do on the job."
            annika "So a project in a portfolio should show off all of the basic skills of a junior developer."
            player "What do you have in mind?"
            annika "Well, during my interview process, I was asked to describe MVC, and how it worked."
            annika "I was also asked to explain how HTTP requests work."
            annika "So, I would use projects that have a good frontend and a backend that either I made, or an API that I've called."
            annika "That way, they'd know that I know how to make HTTP requests or API's."
            annika "Knowing how to use a dozen technologies doesn't mean that you're going to be a good developer."
            annika "I got hired for this position, and I didn't even know most of the technologies that they asked for."
            annika "Once you know one programming language, you can kind of pick up any of them more easily."
            annika "As far as adding a million features,"
            annika "I wanted to do the same thing while I was building my portfolio."
            annika "But one of my mentors said that 4 or 5 good features per project would be more than enough."
            annika "He actually told me that I should just focus on making TWO good projects."
            annika "It was kind of funny, but he said that it's rare for juniors to even FINISH projects."
            annika "He told me that even having two polished, finished projects would impress a panel of interviewers."
            annika "Otherwise, how are you going to PROVE you know the many technologies you say that you do?"
            player "Sheesh! That's so embarrassing!"
            annika "It's okay! We're only juniors. "
            annika "It's just best for new devs to focus on showing off their skills and the functionality of their app rather than how they look,"
            annika "or using a million technologies, or things like that."
            player "So I just told that guy something wrong... What if he follows my advice?"
            annika "Don't worry - Layla's having a chat with him to set him straight. "
            annika "So it's okay!"
            "You lose 10 Energy out of embarrassment."
            $ player_stats.change_stats(ENERGY, -10)
    return
