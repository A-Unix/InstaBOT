#!/usr/bin/python3

import instaloader
import os
import subprocess
import time

try:
    from colorama import init, Fore
except ImportError:
    print(Fore.Red + "Colorama is not installed. Installing it...")
    subprocess.run(["pip", "install", "colorama"], check=True)
    from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def scrape_instagram_profiles():
    # Create an Instaloader instance
    L = instaloader.Instaloader()

    # Define your search terms
    keywords = ['hairdresser', 'hairdressing', 'eyelashes', 'lashes', 'makeup artist', 'barber', 'nails', 'nail tech', 'pedicure', 'massage', 'masseuse', 'wax', 'waxing', 'hair removal', 'tattoo artist', 'piercing', 'piercings by', 'aesthetics', 'facial filler', 'fillers', 'vitamin shots', 'botox', 'dermal fillers', 'fat dissolve', 'facials', 'anti wrinkle', 'skin boosters', 'teeth whitening', 'mobile teeth whitening', 'spray tanning', 'mobile spray tanning']

    for keyword in keywords:
        # Search for profiles based on keyword
        profiles = instaloader.Profile.from_username(L.context, keyword).get_followers()

        for profile in profiles:
            # Check if the profile has a profile picture
            if profile.profile_pic_url:
                print(Fore.GREEN + f"Username: {profile.username}, Followers: {profile.followers}")

                # You can add additional checks, such as business account and bio keywords
                if profile.is_business_account and any(keyword.lower() in profile.biography.lower() for keyword in keywords):
                    # Do something with the profile, e.g., scrape business category and Explore Businesses suggestions
                    business_category = profile.business_category_name
                    explore_businesses = profile.get_explore_businesses()

                    print(Fore.CYAN + f"Business Category: {business_category}")
                    print(Fore.LIGHTYELLOW_EX + f"Explore Businesses: {explore_businesses}")

                print(Fore.LIGHTMAGENTA_EX + "")

if __name__ == "__main__":
    scrape_instagram_profiles()
