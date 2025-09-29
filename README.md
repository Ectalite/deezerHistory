# DeezerHistory

Minimal working example to scrobble latests listening history of deezer without using their deprecated public API.

## How to use

1. Have python3 and pip installed.
2. `pip install .` to install requirements
3. Get the ARL cookie from `deezer.com` and paste it value in `deezer_history.py`
4. (optional) Update timezone with yours
5. `python3 deezer_history.py`

## Limitations
- The visibility scope of a family members is the same as on the website. If a family member has a private account
other members won't be able to see its history and he won't be able to see others history.
