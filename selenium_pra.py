# yahooコメント欄からコメント、ユーザー名、日付、賛成数、反対数を取得するコード
# end と url を標準入力から受け取る

import csv
import time
from selenium import webdriver

class YahooNewsCommentScraping:
    
    comment_boxes = []
    comments = []
    names = []
    dates = []
    agrees = []
    disagrees = []

    start = 1
    cou = 0
    
    def __init__(self, end, url):
        self.end = end
        self.url = url
    
    def scrape(self):
        driver = webdriver.Chrome()
        for page in range(self.start, self.end):
            
            self.url = self.url + "&s=lost_points&o=desc&t=t&p={}".format(page)
            driver.get(self.url)
            time.sleep(5)
            iframe = driver.find_element_by_class_name("news-comment-plguin-iframe")
            driver.switch_to.frame(iframe)

            self.comment_boxes = driver.find_elements_by_class_name("root")
    
            for comment_box in self.comment_boxes:
                #コメント取得
                elem_comment = comment_box.find_element_by_class_name("cmtBody")
                comment = elem_comment.text.split("\n")
                self.comments.append(comment)
                print(comment)        
        
                #ユーザー名取得
                elem_name = comment_box.find_element_by_class_name("rapid-noclick-resp")
                name = elem_name.text
                self.names.append(name)
                
                #日付取得
                elem_date = comment_box.find_element_by_class_name("date")
                date = elem_date.text
                self.dates.append(date) 
        
                #good数取得
                agree_box = comment_box.find_element_by_class_name("good")
                elem_agree = agree_box.find_element_by_class_name("userNum")
                agree = elem_agree.text
                self.agrees.append(agree)

                #bad数取得
                disagree_box = comment_box.find_element_by_class_name("bad")
                elem_disagree = disagree_box.find_element_by_class_name("userNum")
                disagree = elem_disagree.text
                self.disagrees.append(disagree)
                self.cou+=1
       
        #csvファイルとして出力    
        print(self.cou)   
        with open('tes.csv', 'a') as f:
            writer = csv.writer(f)
            for i in range(self.cou):
                print(i)
                writer.writerow([self.comments[i], self.names[i], self.dates[i], self.agrees[i], self.disagrees[i]])

def main():
    input_end = int(input())
    input_url = input()
    obj = YahooNewsCommentScraping(input_end, input_url)
    obj.scrape()

if __name__ == "__main__":
    main()
#url = "https://headlines.yahoo.co.jp/cm/main?d=20200428-00050198-yom-soci&s=lost_points&o=desc&t=t&p={}".format(page)
