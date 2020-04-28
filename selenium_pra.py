# yahooコメント欄からコメント、ユーザー名、日付、賛成数、反対数を取得するコード


import csv
import time
from selenium import webdriver
driver = webdriver.Chrome()

comment_boxes = []
comments = []
names = []
dates = []
agrees = []
disagrees = []

start = 1
end = 10
cou = 0

for page in range(start, end):
    url = "https://headlines.yahoo.co.jp/cm/main?d=20200428-00050198-yom-soci&s=lost_points&o=desc&t=t&p={}".format(page)
    driver.get(url)
    time.sleep(6)
    iframe = driver.find_element_by_class_name("news-comment-plguin-iframe")
    driver.switch_to.frame(iframe)

    comment_boxes = driver.find_elements_by_class_name("root")
    
    for comment_box in comment_boxes:
        #コメント取得
        elem_comment = comment_box.find_element_by_class_name("cmtBody")
        comment = elem_comment.text.split("\n")
        comments.append(comment)
        print(comment)        
        
        #ユーザー名取得
        elem_name = comment_box.find_element_by_class_name("rapid-noclick-resp")
        name = elem_name.text
        names.append(name)
                
        #日付取得
        elem_date = comment_box.find_element_by_class_name("date")
        date = elem_date.text
        dates.append(date) 
        
        #good数取得
        agree_box = comment_box.find_element_by_class_name("good")
        elem_agree = agree_box.find_element_by_class_name("userNum")
        agree = elem_agree.text
        agrees.append(agree)

        #bad数取得
        disagree_box = comment_box.find_element_by_class_name("bad")
        elem_disagree = disagree_box.find_element_by_class_name("userNum")
        disagree = elem_disagree.text
        disagrees.append(disagree)
        cou+=1
       
#csvファイルとして出力    
print(cou)   
with open('tes.csv', 'a') as f:
    writer = csv.writer(f)
    for i in range(cou):
        print(i)
        writer.writerow([comments[i], names[i], dates[i], agrees[i], disagrees[i]])
