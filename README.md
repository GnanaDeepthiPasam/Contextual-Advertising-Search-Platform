# Contextual Advertising Platform

## Technologies used:
Python: Programming language

Django : For web app

Requests: For making HTTP request to blog pages

BeautifulSoup: To parse webpages

RakeNLTK: To find relevant keywords

## Tools used:
Visual Studio Code

## Project description:
Contextual advertising is a technology that finds relevant ads from a given blog article to maximise a blog or websites 
revenue. Contextual advertising is the reason why we see an ad for nike shoes on a fitness related article. In this 
project, I build a contextual advertising platform which reads data from any blog who's URL you pass in, find relevant 
keywords on that blog and find ads which are relevant to them. All of this is done automatically. I first create a basic
Diango app that could accept a blog URL. then read all the data on that blog page using the requests library and
parse the data using BeautifulSoup. I then feed the parsed data to the rake library which then finds the most relevant 
and prominent keywords in that blog article. These relevant keywords are then matched with the ads present in our 
database and gives us back the ads which are most relevant to the blog post.

Finally, I style the web application with Tailwind.

## Screenshots:
![Screenshot (1251)](https://github.com/GnanaDeepthiPasam/Contextual-Advertising-Search-Platform/assets/148503787/7a938af4-6f39-4f6d-a118-7c37659df88d)
![Screenshot (1252)](https://github.com/GnanaDeepthiPasam/Contextual-Advertising-Search-Platform/assets/148503787/f1cf9425-de97-40b5-9c20-a22f0cb4cdbb)


