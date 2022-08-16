# Projeto-Final-Programa-Bolsas
This project was created with the purpose of concluding the "Programa de bolsas Compasso" and has the goal of representing some of the tech skills needed to qualify for a role as a data scientist in the company that gave me the opportunity of working with them for the past few months

This readme will serve as a guide to understand how the program works and show the default path proposed.

## Scrapping with tweepy

In the scrapping package we have a single file, both scrapping and sentiment analysis will be done on it. 
<br />
![image](https://user-images.githubusercontent.com/72091031/184949649-2de1f238-b628-4601-b809-14a2e22096a7.png)
<br />
<br />
first we will need to import the **Tweepy** and set up our keys that can be provided in **developer session** of twitter
<br />
![image](https://user-images.githubusercontent.com/72091031/184950875-48ddd3d1-4154-4154-a947-0d1e9f8cd3ef.png)
<br />
<br />
I'm using a config file so I can provide the source code without having to modify it that much
<br />
![aaaaaaxxxx](https://user-images.githubusercontent.com/72091031/184951842-7316fcde-5d71-485a-b41a-db274c73f91d.png)
<br />
<br />
Now for the scrapping part, after we authenticate our project with the keys, we will provide a cursor with the parameters of our search, that being time of posting, user name and tweet content, I exported it to a csv file for later analysis.
![image](https://user-images.githubusercontent.com/72091031/184952283-8c1008c9-cefc-466a-8d1b-861538ff1c62.png)
<br />
<br />
## Sentiment Analysis with **roBERTa**

Before we use roberta to make our tension maps, we need to pre process the data, every mention by **"@"** must be replaced by **"@user"** and every link must be replaced by **"http"**, I did it in a separate function.
<br />
![image](https://user-images.githubusercontent.com/72091031/184956395-6a296e03-536a-4194-8a01-6cf50576dbec.png)
<br />
After that we can send that pre processed tweet to roberta
![image](https://user-images.githubusercontent.com/72091031/184957563-dd09eb73-a7ca-43bf-8273-02a5d17393c9.png)

this function will give you 3 tension masks, with the following id labels (Negative, Neutral, Positive), the higher value will determine what sentiment can be described in that respective tweet. (the sentiment and the tensor value will be attatched to the csv file)

## Ploting and filters

The ploting will be done in other packages separated by use and a general ploting
<br />
![image](https://user-images.githubusercontent.com/72091031/184959560-8deb06de-c777-486f-b826-20f638f9d86a.png)
<br />
<br />
After seing the general ploting I observed a tendency for Neutral results that was caused by tweets that have just @user's and http's links
![image](https://user-images.githubusercontent.com/72091031/184960916-be3b10ab-aa4a-4149-9d75-3af00dc5cdc1.png)
<br />
<br />
After filtering that particular error you should have a ploting that looks like this
![image](https://user-images.githubusercontent.com/72091031/184961204-43714cd1-7b0c-456d-b0c0-f95162157cac.png)
<br />
thats how having a non verbal language can influence our results when we just count with NPL and discard the possibility of being required a visual data processing method.
<br />
<br />
The other packages are used to provide an information of how many tweets respectively have http (how I obtained the information about neutral tweets with http and just users)




