# Artificial Intellligence

Till today, Artificial Intelligence or AI is focused on solving a single task efficiently. An ML model wherein weights in matrices are updated based on the data and loss function. Loss function is minimized and weights are updated.
This ML model is then used for getting inference on new data. Same is true for deep learning based neural networks. The weights and biases for neurons are updated untill the loss function is minimized.

But what do we do if you ask this ML or DL model on some unknown tasks or domain. Generally, an ML model memorizes the pattern for the domain from which training was done.

# Artificial General Intelligence

We want AI to learn new tasks on the fly with minimal amount of data on new tasks. Let's see how we as humans generally learn multitasking. Say I am born today morning, and today I learned to differntiate between colors.
At the end of the day only know how to differentiate different colors. Next morning, I am to identify object boundaries from real world based on the color. This is how it evolves:
I look at objects, gather the visual input inside my brain, and then retrieve the learned pattern/memory for each patch I saw - with comparison of each pixel/smallest fragment I could get down upto, and place them into two categories of colors - red and green.
Based on this differnitation, I came up with number of different objects of red and green color from the view I captured through my eyes, say my existence was for that moment only.

In this momentary life, I did the following tasks:

1) I learned to differentiate between red and white color. Assume this is an ML model, trained on domain color differentiation.
2) I gathered data through my eyes, that is a momentary view.
3) I then broke it down into as smallest possible patches.
4) I used previous color differentiation task learning to categories each of the patches into red or green.
5) I then merged each adjoining patch in same category of color.
6) I then based on previous learning categorized each of these biggest connected patches into two objects.
7) I am now trained to differentiate two objects in a picture of red and green.

This shows that the T1 task learning helped to achieve T2 task in my short-lived life.
How did I accomplish this? What was common between these two tasks?
It was color based differentiation. Its basis was color.
One task is for classification of two colors - T1.
Second task is for classification of object by using feature differentiating abilities or boundaries detection learned in T1 that is - T2.

I can go on and on adding additional tasks in same domain.

If I want to understand uttered words or sounds' direction, I will need to map its intensity, and objects in its path while it reaches me. I will need some model of my vicinity which gives me spatial coordinate based on certain voice features.
This is completely different task - T3 which can not be learned from T1 or T2. It is totally different domain. This domain is impossible to learn as it is for different sense organ, ear.

T2 learning from T1's information is called transfer learning. If you have to put in dummy neural network form, you can put it as [Input ---> <T1 NN Layer> --> <T2 NN Layer> ---> Object [Red or Green].
Learning T2 from T1 is called domain adaptation. This is a simple example of Artificial General Intelligence.

You might have observed that it has two model. One is inner model which is trained first. And then outer layer which uses the inner model for its training. What do you feel - to learn T2, did we at all need the data used for training for 
T1 task, all we needed is output from T1 and few data points from our instant visual perception. 

AGI is therefore all about instant learning in a vague words. Instant here means-with data as much as observed by our visual perception instantly.

Transfer learning as shown from above neural network example of object differentiation is simply adding additional layer of NN or ML in the downstream which can be trained from small data, keeping previous layer intact or unchanged.
In transfer learning, you utilize abilities from all tasks learned from previous model(s) or part.
Meta Learning is the branch of AGI wherein the model learns to learn. It learns how to learn for new task. In previous example, you can see that if T2 would have been my requirement, this orchestration of T1 --> T2 would
be called meta-learning. In that scenario, all you would have been given was data to distinguish beween red and green based on features of red and green colors say R, G, B channel values and any additional features along with an instant perception received from visual system.
Based on this, the model should have been able to figure out training for T1 task from R,G,B data and then T2 task based on small one instant data received from visual senses and perception - which is instantaneous data.
This ability to orchestrate this entire learning process from some receievd data so that task T2 can be accomplished instantly is called Meta-Learning. This initial discussion will help us build dummy AGI systems in Python.

This repository is an intellectual property of Technocraft AI, a parent of AItomation Pvt Ltd. Use of this data is strictly prohibited, can be sued in International Courts of respective countries, financially as well as otherwise.

**&copy; AItomation Pvt Ltd 2026**
