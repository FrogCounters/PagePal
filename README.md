# PagePal

## Links

[Devpost Submission](https://devpost.com/software/random-dude-carry)
## Rationale of our project

It is estimated that on average, about 1 in 100 children has autism spectrum disorder (ASD) worldwide, and although there are support systems in place that aims to support individuals with ASD through their early stage in life, there is a lot more that we can do to aid these children in their education.

Children with ASD may have difficulties in recognising and understanding emotions. Such difficulties may lead to trouble in trying to convey some of the emotions that they are feeling and perhaps lead them to feel a sense of helplessness because they are not able to communicate their feelings to others.

What if we can teach these children to better understand emotion? Can emotions really be learnt and taught though? Of course! Studies have shown that early behavioural intervention allows us to help children with ASD better understand emotion and in turn respond appropriately. Popular methods to do so include the use of Emotion Flashcards and programmes that focus on recognising facial expressions. While there already exists ways to educate these children on emotional literacy, we wanted to come up with a better and more creative way to help parents or teachers aid children with ASC in emotional recognition.

And with the advent of technology, what better way to do it than through storytelling?


![Story Book](https://i.imgur.com/bLXICrW.jpg)

*Image 1 : Story Book*
<br> </br>

Stories and Literature are an essential tool for teaching young children emotional literacy skills and through story books, we can convey what feelings can look like and explore different ways and possibilities to react to different emotions.

## PagePal and what it does

PagePal is an assistive tool that labels emotional traits in texts and story books to aim to help children with ASD to better recognise emotions through the use of storytelling. 

![Page Pal Front Page](https://i.imgur.com/PLki6Hh.png)

*Image 2 : Page Pal*
<br> </br>

PagePal makes clever use of the expert.ai NL API to split texts into sentences, extract their emotional traits and display them on our Web Application (Web app). This allows young readers to more easily follow the emotional elements and links throughout the story and serves as an easy-to-use assistive tool to help children with ASD better understand emotions through the medium of storytelling.

PagePal already has a few stories that are tagged with emotional traits and is available for anyone who wants to start reading. Additionally, users are able to add their own stories or texts on PagePal to generate labels for emotional traits.

![Page Pal More Books](https://i.imgur.com/C8FS1yA.png)

*Image 3 : Page Pal Stories*

## Tech Stack

- Frontend
    - Vue
- Backend
    - Python
    - Firebase
    - Fast API
- Deployed on AWS Amplify + Heroku

## How to Use?

**Read stories already available on PagePal**

1. Simply click on any of the available stories to start reading now!

**Upload custom stories/texts**

1. Upload your story under the `Custom` tab

2. Click on the `Analyse` button to generate the emotional traits analysis.

3. Click on the `Generate URL` button, then the `Book ID` to access the analysed text 


## Challenges Faced

PagePal experienced many initial challenges throughout its conceptualisation.

Specifically, we faced many issues with the deployment of the application and ran into many bugs before finally succeeding in deployment.

This being the first Hackathon for some of us, the process of turning an idea into a Web app was a difficult and daunting task. Nevertheless, it was a success, and we hope that through PagePal, parents and teachers are better able to develop emotional literacy in children with ASD.

## What's next for PagePal

We hope to integrate and incorporate access to stories from popular online book catalogues such that users can have access to a greater variety of stories.

We believe the PagePal has great potential for expansion. Integrating AR and CV technology, we could apply the same idea and provide emotion display overlays for real books as well!

## References 

- Autism Spectrum Disorders. https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders#:~:text=It%20is%20estimated%20that%20worldwide,prevalence%20varies%20substantially%20across%20studies. (accessed Oct 27,  2022). 

- Image From : Moreh, J. Free stock photo of story book - childhood imagination concept. https://www.stockvault.net/photo/182254/story-book-childhood-imagination-concept (accessed Oct 27,  2022). 

