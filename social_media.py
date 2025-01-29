from seleniumbase import SB
import random
import pyautogui
import pyperclip

import pandas as pd
initial_df = pd.read_csv("/home/himaghna/Desktop/big-data/Onlyfinder-combined-FREE-urls-v-3.csv")
platform_columns = {
        'instagram': 'INSTAGRAM URL',
        'x.com': 'X URL',
        'twitter.com': 'X URL',
        'fansly': 'FANSLY URL',
        'pornhub': 'PORNHUB URL',
        'tiktok' : 'TIKTOK URL',
        'patreon' : 'PATREON URL'
    }

with SB(uc=True, test=True, locale_code="en") as sb:
    
    url = "https://onlyfindersearch.com/"
    first_name = initial_df["Onlyfans_name"][0]
    initial_x_coordinate = 858

    sb.activate_cdp_mode(url)
    sb.sleep(10.62)
    sb.cdp.gui_click_x_y(534, 589)
    #pyautogui.click(534,587)
    #sb.cdp.click_active_element()
    selector = "div#resultsProfiles.container.collect"
    sb.sleep(8.65)
    sb.cdp.press_keys("input#landing-input", first_name)
    sb.sleep(5.42)
    sb.cdp.gui_click_x_y(900, 550)
    sb.sleep(5.43)
    if initial_df["filled_links"][0] >0:
        social_list =[]
        for i in range(initial_df["filled_links"][0]):
            sb.cdp.gui_click_x_y(initial_x_coordinate -(30*i), 383)
            sb.sleep(60)
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
            account = pyperclip.paste()
            pyautogui.hotkey('ctrl', 'w')
            social_list.append(account)
        for link in social_list:
            link_lower = link.lower()
            for platform, column in platform_columns.items():
                if platform in link_lower:
                    initial_df[column][0] = link
                    
    sb.sleep(4.8)
    for i in range(1, len(initial_df)):
        if initial_df["filled_links"][i] >0:
            social_list = []
            sb.cdp.gui_click_x_y(770, 245)
            sb.cdp.press_keys("input#landing-input", initial_df["Onlyfans_name"][i])
            sb.sleep(3.4)
            sb.cdp.gui_click_x_y(800, 250)
            sb.sleep(3.42)        
            
            for j in range(initial_df["filled_links"][i]):
                sb.cdp.gui_click_x_y(initial_x_coordinate -(30*j), 383)
                sb.sleep(2.5)
                pyautogui.hotkey('ctrl', 'l')
                pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
                account = pyperclip.paste()
                if "onlyfindersearch" not in account:
                    pyautogui.hotkey('ctrl', 'w')
                    social_list.append(account)
                    sb.sleep(1.5)
                else:
                    continue

            for link in social_list:
                link_lower = link.lower()
                for platform, column in platform_columns.items():
                    if platform in link_lower:
                        initial_df[column][i] = link

            initial_df.to_csv("/home/himaghna/Desktop/big-data/Onlyfinder-combined-FREE-urls-v-3.csv", index=False)

        else:
            continue

    #initial_df.to_csv("/home/himaghna/Desktop/big-data/Onlyfinder-combined-urls-v-3.csv", index=False)

            #himuitis
            #Nandini11223456
#@HimaghnaMuk
#Nandini123

