import twint
import os
import glob
import pandas as pd
#Put your list of accounts in like the template
username = ["its_erick_76"]
#limit the number of tweets collected per account: c.Limit = 1000
def ai(user):
 c = twint.Config()
 c.Username = user
 c.Custom["tweet"] = ["tweet"]
 c.Store_csv = True
 c.Output = f'{user}.csv'
 print(user)
 twint.run.Search(c)
for users in username:
 ai(users)
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "alltweets.csv", index=True, encoding='utf-8-sig')
