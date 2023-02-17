import requests


## necessary cookies
cookies = {
    'li_at': 'AQEDATLDxQYFH-WmAAABhlvLzzEAAAGGf9hTMVYAl_0ZJvhqDcyI6nGjA15J3EC0RLj2mvwu840JY0enB466Xz0m6l7h470hCqlcMeYtsjBgHGG7ljnxp9b1IANJ0yi09nsk038aebC6XyGSKA_gRMsK',
    'JSESSIONID': '"ajax:1639288170270568174"',
}

headers = {
    'authority': 'www.linkedin.com',
    'accept': 'application/graphql',
    'accept-language': 'en-US,en;q=0.5',
    'csrf-token': 'ajax:1639288170270568174',  ## necessary header
    'referer': 'https://www.linkedin.com/messaging/thread/2-ZGUyNmJjZDEtMDczZS00OGZmLWIwZGEtZTEyOTlhZGM3MWE5XzAxMA==/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-li-lang': 'en_US',
    'x-li-track': '{"clientVersion":"1.11.8996","mpVersion":"1.11.8996","osName":"web","timezoneOffset":-7,"timezone":"America/Edmonton","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":2,"displayWidth":2880,"displayHeight":1800}',
    'x-restli-protocol-version': '2.0.0',
}

response = requests.get(
    'https://www.linkedin.com/voyager/api/voyagerMessagingGraphQL/graphql?queryId=messengerMessages.8d15783c080e392b337ba57fc576ad21&variables=(conversationUrn:urn%3Ali%3Amsg_conversation%3A%28urn%3Ali%3Afsd_profile%3AACoAADLDxQYB9jJrepldGurMPwYR4WOjBGNE_aI%2C2-NDY4NzY1ZWMtODVkZS00NDMwLThkOTctMzZmMThkYmE3MmNiXzAxMA%3D%3D%29)',
    cookies=cookies,
    headers=headers,
)

print(response.status_code)