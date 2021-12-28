#linkedin is commented
#call the function to get variable
#!!!modify the time at line5! it should be the folder name!!!

time="2021_12_20_20_35_40"


import glob
import json
'''
linkedin_path = "./{}/linkedin_*.json".format(time)
for linkedin_json in glob.glob(linkedin_path):

    import_file = open(linkedin_json, "r")
    posts=import_file.read()
    print(posts)

import_file.close()
'''
def twitter_posts():
    twitter_posts=[]
    twitter_path = "./{}/twitter_*.json".format(time)
    for twitter_file in glob.glob(twitter_path):

        twitter_json=open(twitter_file,"r")
        for line in twitter_json:
            line=json.loads(line)
            twitter_posts.append(line["tweet"])
    twitter_json.close()
    return twitter_posts

def insta_posts():
    insta_posts=[]
    insta_path = "./{}/instagram_*.json".format(time)
    for insta_file in glob.glob(insta_path):

        insta_json_file=open(insta_file,"r")

        insta_json=json.loads(insta_json_file.read())
        for number in range(len(insta_json)):
            if insta_json["{}".format(number)]["post"] != None:
                insta_posts.append(insta_json["{}".format(number)]["post"])
    insta_json_file.close()
    return insta_posts

print(twitter_posts())
print(insta_posts())


