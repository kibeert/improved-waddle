from bs4 import BeautifulSoup


with open('index.html', "r") as html_file:
    content = html_file.read()
    

    soup = BeautifulSoup(content, 'lxml')
    couses_html_tags = soup.find_all('h5')
    desc = soup.find_all("p")
    price = soup.find_all('a')
    for course, descs, prices in zip(couses_html_tags, desc, price):
        print(course.text + ', '+ descs.text +" - " + prices.text)