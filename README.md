To run the program, just execute the main.py file.

EXPLANATION:
To do the first three tasks, I developed the following strategy:

First I opened the image and saved all the pixel values(returns RGBA values), image height and width in variables.
Task 1 & 2: I traversed the pixels array, checking for pure white or pure red RGBA values. If it was white, I'd add it to a Stars counter. If it was red, I’d add it to a Meteor counter. Then returned the values.

Task 3:  The strategy for Task 3 was identify the water level, then save all x(width) values of the water level pixels. Then, I saved all width values for meteors inside the same loop used for Task 2. As the last step, I intersected water level pixels width values with meteor width values, which resulted in meteors widths that were perpendicular to water pixels, and counted the list for the final value of meteors.

Task 4: To start Task 4, I had a suspicion in mind that it was related to Morse Code, but had no starting point regarding it. I decided to start my investigation by saving the number of meteors/stars in each row and column of pixels, and printing it out. By doing so,I realized columns either had one(1) or zero(0) meteors/stars. I decided to try to decode it by thinking of it as binary representations of ASCII values. So I transformed both binary arrays into strings, and ran it through a built-in binary decoder. The end result was a message of Rocky Balboa in one of its movies.
