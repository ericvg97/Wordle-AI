ssh-keygen -t ed25519 -C "eric.vallsg@gmail.com"

Enter
Enter
Enter

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

sudo apt-get update
cat ~/.ssh/id_ed25519.pub


//anar a github i afegir
git clone git@github.com:ericvg97/Wordle-AI.git

cd Wordle-AI/

sudo apt install python3.8-venv
python3 -m venv venv
source venv/bin/activate
pip install selenium
//canviar a requirements

sudo apt-get install unzip


sudo wget https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_linux64.zip
 unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
 rm chromedriver_linux64.zip


wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install ./google-chrome-stable_current_amd64.deb 
rm google-chrome-stable_current_amd64.deb 

# afegir aixo al principi


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
d = webdriver.Chrome('your-chrome-driver-path',chrome_options=chrome_options)
# d.get('https://www.google.nl/')