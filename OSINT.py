# Skyfire

#In OSINT, hold ctrl and click "ProfileScraper" at line 17
#slide down to replace the function at around line 29 with the following code
#may need to save as admin user
'''
def scrape(self, url='', user=None):
    output=[]
    for x in user:
        self.load_profile_page(url, x)
        output.append(self.get_profile().to_dict())
        print("1")
    return output
'''


from scrape_linkedin import ProfileScraper
from instagramy import InstagramUser
import twint
import json 
import os
import datetime


linkedin_cookie='AQEDATkY7_4BYlm6AAABfdhhnFYAAAF9_G4gVk4AmK4lsEkSd42kiNQgj0FJHTRx7nfisel76viAB9lkp2DwQy75nrLrblwTadc7aHH8wH_NDPsFOEd_9mElbKDQx69fFj9x_PMtFSGpqOJdUJRHlNPN'
linkedin_username=["austinoboyle","lee-y-4b7144131"]

insta_cookie="50417429503%3A26oTMzJaLCCStW%3A24"
insta_username="lukadoncic"

twitter_username="tim_cook"

def LinkedIN(cookie, username,time):
    with ProfileScraper(cookie) as scraper:
        results=scraper.scrape(user=username)
    z=0
    for result in results:
        
        output={}
        output["name"]=result["personal_info"]["name"]
        output["school"]=result["personal_info"]["school"]
        output["company"]=result["personal_info"]["company"]
        output["location"]=result["personal_info"]["location"]
        output["jobs"]={}
        for x in range(len(result["experiences"]["jobs"])):
            output["jobs"][x]={}
            output["jobs"][x]["title"]=result["experiences"]["jobs"][x]["title"]
            output["jobs"][x]["company"]=result["experiences"]["jobs"][x]["company"]
            output["jobs"][x]["locatoin"]=result["experiences"]["jobs"][x]["location"]
        output["education"]={}
        for y in range(len(result["experiences"]["education"])):
            output["education"][y]={}
            output["education"][y]["name"]=result["experiences"]["education"][y]["name"]
            output["education"][y]["field_of_study"]=result["experiences"]["education"][y]["field_of_study"]
        out_file = open("./{}/linkedin_{}.json".format(time,username[z]), "w")
        json.dump(output,out_file)
        out_file.close()
        z+=1
    return


def insta(cookie,username,time): 
    user=InstagramUser(username,sessionid=cookie)
    result=user.posts
    output={}
    for x in range(len(result)):
        output[x]={}
        output[x]["post"]=result[x][2]
        output[x]["location"]=result[x][5]
        output[x]["time"]=result[x][-1].strftime("%Y-%m-%d")
    
    out_file = open("./{}/instagram_{}.json".format(time, username), "w")
    json.dump(output,out_file)
    out_file.close()

    return 



def twitter(username,time):
    c = twint.Config()
    c.Username = username
    c.User_full = True
    c.Show_hashtags = True
    c.Custom["tweet"] = ["date", "time", "place", "tweet", "hashtags", "geo"]
    c.Store_object = True
    c.Store_json = True
    c.Output = "./{}/twitter_{}.json".format(time, username)
    c.Since = "2021-11-01"

    twint.run.Profile(c)
    return


task_time=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
os.umask(0)
os.mkdir("./{}".format(task_time),mode = 0o777)


LinkedIN(linkedin_cookie,linkedin_username,task_time)
insta(insta_cookie,insta_username,task_time)
twitter(twitter_username,task_time)

