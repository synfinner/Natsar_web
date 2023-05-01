# Natsar Web

Hello! Welcome to the web (streamlit) version of my previous Natsar script. There are a lot of features that I want to add, so things will probably change.

## Installation and Setup

**Install Dependencies:**

```
pip3 install -r requirements.txt
```

**Get Telegram client API keys:**

Login copy the app_id and app_hash values from:  

* https://my.telegram.org

**Add Telegram API data to env**

Put the app_id and app_hash into a .env file, feel free to rename `.env_sample` to `.env`. You will need a eventually need a session file for when I get some additional sections coded. There is a `natsar_init.py` that will walk you through generating the session file. 

## Run

`streamlit run natsar.py`

![](/images/image_2.jpg)

### Downloading files

If files are found within the bot, Natsar will retrieve the downloadable link and present it to you: 

![](/images/file_download.jpg)