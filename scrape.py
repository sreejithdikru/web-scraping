import requests
import datetime

now = datetime.datetime.now()
year = now.year

def url_to_txt(url, file_name= 'world.html', save = False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html" , 'w') as f:
                f.write(html_text)
        return html_text
    return ""


url = "https://www.boxofficemojo.com/"

html_text = url_to_txt(url)

