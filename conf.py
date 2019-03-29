#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# allegro web data
div_class = {"class": "ed3ac72"}
delay = 1
user = "SmA_Honor"
price_from = 0
price_to = 2
req = "https://allegro.pl/uzytkownik/%s?order=n&price_from=%s&price_to=%s" % (user, price_from, price_to)

# allegro api data
api_seller_id = "49444071"
api_basic_auth = "yourbasic_base64_api_auth"
api_redirect_url = "https://deregowski.net/"

api_access_token_h = {
    'allegro': [
        ('Content-Type', 'application/vnd.allegro.public.v1+json'),
        ('Accept', 'application/vnd.allegro.public.v1+json'),
        ('Authorization', 'Bearer your_auth_token_code'),
    ]
}

api_refresh_token_h = {
        'Authorization': 'Basic yourrefresh_token',
}

api_refresh_token = "your_auth_token_code"

api_url_get_offers = "https://api.allegro.pl/offers/listing?seller.id=%s&price.from=%s&price.to=%s&sort=+price" \
                     % (api_seller_id, price_from, price_to)

api_url_refresh_token = "https://allegro.pl/auth/oauth/token?grant_type=refresh_token&refresh_token=%s&" \
                        "redirect_uri=%s" % (api_refresh_token, api_redirect_url)

api_allegro_listing = "https://allegro.pl/listing?string=%s"
