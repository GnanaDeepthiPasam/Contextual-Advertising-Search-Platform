from django.shortcuts import render

import requests

from bs4 import BeautifulSoup

from rake_nltk import Rake 
import nltk
import collections
import difflib

from .models import Tag
from .models import Advert

nltk.download('punkt')
# nltk.download('stopwords') # These are some words which needs to be eliminated and this only needs to run once
                             # So once you run your code, you could actually comment this line of code out

# Create your views here.

def index(request):

    if(request.method=='POST'):

        url=request.POST.get('url')
        # print(url) 

        response=requests.get(url=url) # The right hand side of the url is the one which we have mentioned in the above step
        # print(response.content) 

        soup=BeautifulSoup(response.content,'html.parser') # 'html.parser' indicates that we are parsing the content which is html
        # print(soup) 

        # para_list=soup.find_all('p') # 'p' indicates paragraph and then it will return the output in the form of 'list'
        # print(para_list)

        # for i in soup.find_all('p'):

            # print(i.get_text())

        all_text='' # Combine all of this together in one string 
        for i in soup.find_all('p'):

            all_text+=str(i.get_text())
        # print(all_text)

        rake_var=Rake()
        rake_var.extract_keywords_from_text(all_text) # This will extract all the keywords and are going to be saved in 'rake_var'
        keywords_extracted=rake_var.get_ranked_phrases() # This is going to get only the important keywords
        # print(keywords_extracted)

        ad_tags=[] # Created an empty list
        tags=Tag.objects.all()

        for j in tags:

            ad_tags.append(j.tagname)

        set_a=set(keywords_extracted)
        set_b=set(ad_tags)
        common_words=[]

        if(set_a & set_b):

            common_words=list(set_a & set_b)

        # print(common_words)

        relevant_ads=[]
        for k in Advert.objects.all():

            for m in k.tags.all():

                if m.tagname in common_words:

                    relevant_ads.append(k)
                    relevant_ads=set(relevant_ads)
                    relevant_ads=list(relevant_ads)
                
                # If there are 3 keywords which match up with the single ad, then that ad is going to be
                # placed inside the 'relevant_ads' 3 times. So in order to avoid the issue of duplicate ads, 
                # we are converting it into a 'set' and then convert it back to list

        print(relevant_ads)

        context={
                 "common_words":common_words,
                 "relevant_ads":relevant_ads
                }

        return render(request,'myapp/index.html',context)

    return render(request,'myapp/index.html')
