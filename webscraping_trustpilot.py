from bs4 import BeautifulSoup
import requests
import mysql.connector
def createConn():
    return mysql.connector.connect(host = "localhost", user = "root",passwd = "123456789", database = "scraping")
url = "https://www.trustpilot.com/categories/electronics_technology"
res = requests.get(url)
soup = BeautifulSoup(res.content,'html5lib')

data = soup.find_all('a', attrs = {'class':'link_internal__YpiJI link_wrapper__LEdx5'}) 
for e,i in enumerate(data):
    try:
        title=i.find('div', {"class" : 'styles_businessTitle__1IANo'}).text
        desc=i.find('div', {"class" : 'styles_categories__c4nU-'}).text
        review1=i.find('div', {"class" : 'styles_textRating__19_fv'}).text
        reviewlist=review1.split()
        review,star=reviewlist[0],reviewlist[4]
        print(title," : ",review, " : ",star)
        tup1 = (title,desc,review,star)
        conn = createConn()
        cursor = conn.cursor()
        query = "insert into trustpilot (title,Description,reviews,star_rating) values(%s,%s,%s,%s)"
        cursor.execute(query,tup1)
        conn.commit()
    except:
        pass