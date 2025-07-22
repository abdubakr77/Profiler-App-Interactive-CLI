import time
import os



# Convert the uppercase to lowercase and the oppisite is ture 
# print("Abdu Bakr".swapcase()) 
 
# reverse the list
# name = ["Bakr","Abdu"]
# name.reverse()
# print(" ".join(name))

# profile = {}

# a = ("key1","key2","key3")
# b = ("x","i")

# #profile.setdefault("nickname","ABOD")
# print(profile.fromkeys(a,b))



def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_profile():
    for profile_name, profile_lang in profiles.items():
        print(f"Profile name is: {profile_name}")
        print(f"{profile_name} Experiences is:")

        for child_lang, child_exp in profile_lang.items():
            print(f"{child_lang} => {child_exp}")

profiles = {}

print(" Welcome To Profiler App ".center(50,"="))

while True:
    
    name = input("What is your name: ").strip().capitalize()
    print(f"Let's setup your profile {name}!")
    time.sleep(2)
    lang = input(f"Hello {name}, What lang do u learned? ").strip().capitalize()
    langskill = input(f"How much experience do u have in {lang} {name}? %").strip().capitalize()

    profiles[name]= {lang: f"%{langskill}"}
    
    
    while input(f"Do u want add one more lang u already learned? (y/n) ").strip().lower() == "y":

        another_lang = input(f"What another lang u learned? ").strip().capitalize()
        another_langskill = input(f"How much experience do u have in {another_lang} {name}? %").strip().capitalize()

        profiles[name][another_lang] = f"%{another_langskill}"

        
    if input("Do u want to save this profile data? (y/n): ").strip().lower() == "y":
        print("Saving your data please wait...")
        time.sleep(3)

    else:
        print("This profile not saved")
        profiles.clear()
    
    if input("Do u want to see currently profile? (y/n): ").strip().lower() == "y":
        if profiles:
            print("Showing the currently profile, please wait...")
            time.sleep(2)
            display_profile()
        else:
            print("Sorry, ur data maybe not saved please make sure u save ur data next time!")

    if input("Do u want add another profile? (y/n)").strip().lower() == "y":
        print("Please wait...")
        time.sleep(2)
        clear_screen()
    else:
        print(f"See u later {name}!")
        time.sleep(2)
        break
    