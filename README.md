# Bot, send me ...

Simple Telegram Bot that resends you a message sent to a server to your mobile/desktop.

## Installation
TBD

Rename `example_settings.py` to `settings.py` and set the correct values in it.

## Example POST
```
POST https://botsend.me
```
with data
```json
{
    "message": "Everything gonna be alright."
}
```
## Example GET
```
GET https://botsend.me?message=Hi.
```
