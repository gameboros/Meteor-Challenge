# Meteor-Challenge


* Meteor Challenge (Part 1)

Tasks:

    Count the number of Stars

    Count the number of Meteors

    If the Meteors are falling perpendicularly to the Ground (Water level), count how many will fall on the Water

    (optional) Find the phrase that is hidden in the dots in the sky.

HINT 1: 175 Characters

HINT 2: Most of the last tasks’ code can be reused for this one

    Please, send us the result and code you used to solve the tasks above. Explain how you achieved the results in each question. Good work!!

Subject: [CHALLENGE] [METEOR] João Vítor Almeida Araújo Belchior

[Sample] Answers:

| Number of Stars              | 315                                                                                                                                                                              |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of Meteors            | 328                                                                                                                                                                              |
| Meteors falling on the Water | 105                                                                                                                                                                              |
| (optional) Hidden Phrase     | "It's not about how hard you hit. It's about how hard you can get hit and keep moving forward. How much you can take and keep moving forward"  - Rocky Balboa/Sylvester Stallone |

Pixel Ref:

    (pure white)    Stars

    (pure red)      Meteors

    (pure blue)     Water

    (pure black)    Ground

EXPLANATION:

To do the first three tasks, I developed the following strategy:

First I opened the image and saved all the pixel values(returns RGBA values), image height and width in variables.

Task 1 & 2: I traversed the pixels array, checking for pure white or pure red RGBA values. If it was white, I'd add it to a Stars counter. If it was red, I’d add it to a Meteor counter. Then returned the values.

Task 3:  The strategy for Task 3 was identify the water level, then save all x(width) values of the water level pixels. Then, I saved all width values for meteors inside the same loop used for Task 2. As the last step, I intersected water level pixels width values with meteor width values, which resulted in meteors widths that were perpendicular to water pixels, and counted the list for the final value of meteors.

Task 4: To start Task 4, I had a suspicion in mind that it was related to Morse Code, but had no starting point regarding it. I decided to start my investigation by saving the number of meteors/stars in each row and column of pixels, and printing it out. By doing so,I realized columns either had one(1) or zero(0) meteors/stars. I decided to try to decode it by thinking of it as binary representations of ASCII values. So I transformed both binary arrays into strings, and ran it through a built-in binary decoder. The end result was a message of Rocky Balboa in one of its movies.
