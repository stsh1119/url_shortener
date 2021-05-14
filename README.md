# url_shortener 

The API can shorten any url(up to 2000 symbols) and give you a short version of it, that can later be used to access the original URL.

Created with Flask

### To run the app locally:

1. Clone the repository ```git clone https://github.com/stsh1119/url_shortener.git```
2. Create virtual environment with ```python -m venv venv```
3. Activate an environment
4. With activated environment, run ```pip install -r requirements.txt```
5. Run ```python run.py```

### Usage:
1. To create a short URL, without specifying its expiration time(by default, expiration time will be set to 90 days):

Send [POST] request to `localhost:5000` with the following body:
```json
{
	"original_url": "https://github.com/stsh1119/url_shortener"
}
```

You can explicitly specify expiration period, in days by sending days_to_expire parameter in body. 

days_to_expire should be within 1 and 365 days
```json
{
	"original_url": "https://github.com/stsh1119/url_shortener",
	"days_to_expire": 10
}
```

2. To view the original link using a short one, send a [GET] request to `localhost:5000/short_link`

Example:
[GET] `localhost:5000/d9235`

---
#### Cleanup of expired links
Cleanup of expired links can be done by scheduling `cleanup.py` script in cron or by running sql script directly.
Links, that are going to be deleted will be logged to `deletion.log`
