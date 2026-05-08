import random
is_alive = True
has_tourch = False
bhaute_gone = False
search_count = 0 

print("......Archale Ban ma Swagat Cha......\n")
print("Kalo Adhyaro cha jata tatai, hussu le chiso baadi rako cha...")
print("Achanak Bhaute timro agadi ayo ra timro bato rokyo")

while is_alive and not bhaute_gone:
    print("\nKat... Kat... kat...")
    action = input("\nKe garchau? (khojne / balne / cross): ").lower()

    if action == "khojne":
        if search_count < 2:  
            search_count += 1
            print(f"(Search attempt {search_count}/2)")
            
            if random.random() > 0.4:
                print("Yee bhetyu! Euta purano tuki bhetyu.")
                has_tourch = True
            else:
                print("Kei bhetiyena...")
                if search_count == 2:
                    print("Abba baki thau chaina khojna lai! Bhaute jhan najik ayo.")
        else:
            print("Timi dherai beri jhadima bhulyeu! Bhaute le timilai dekhyo.")
            print("Dherai khojera basda Bhaute le timilai samatyo!")
            is_alive = False
            print("-----Game Over: The man has died-----")

    elif action == "balne":
        if has_tourch:
            print("Timi tuki balchau!! Bhaute ujyelo dekhna na sakera karaucha ra bhagcha.")
            bhaute_gone = True
        else:
            print("K Tuki cha ra balchu bhaneko!! Paile khojnu parcha ni!!")
            print("Bhaute timro najik aucha ra akha nikal dincha! Timi chatpataudai marchau.")
            print("-----Game Over-----")
            is_alive = False

    elif action == "cross":
        print("Bhagchau khub... Bhaute ta timi bhanda agadi pugera 'Hi' garera basecha bridge ma!")
        print("Marne manche lai over confidence le pani bachaunna!!\n")
        print("-----Game Over-----")
        print("Maryu!! Arko Janma ma bhetam la!!")
        is_alive = False
    
    else:
        print("Ali dhangako kura gara! Bhaute jhaskira cha.")

if bhaute_gone:
    print("\nLa badai cha, jyaan bachyo! Archale Ban bata niskine bato bhetiyo.")