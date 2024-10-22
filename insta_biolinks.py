from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def configure_driver():
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')  # Run headless to avoid UI load overhead
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def login_to_instagram(driver, username, password):
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        
        # Wait for the username field to be visible and interactable
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')
        
        # Enter credentials
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        # Wait for the login button to be visible and interactable
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[div[contains(text(), 'Log In')]]"))
        )
        login_button = driver.find_element(By.XPATH, "//button[div[contains(text(), 'Log In')]]")
        login_button.click()
        
        # Wait for an element that confirms successful login
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'your-profile-class')]"))
        )
    except TimeoutException as e:
        print(f"Error: Page elements did not load in time: {str(e)}")
    except NoSuchElementException as e:
        print(f"Error: Could not find an expected element: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def extract_bio_url(driver):
    try:
        # Modify the selector based on the new classes provided
        bio_url_element = driver.find_element(By.CLASS_NAME, 'x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft')
        return bio_url_element.text
    except NoSuchElementException:
        return "N/A"  # Return "N/A" if no bio link is found

def scrape_instagram_links(instagram_urls, username, password):
    driver = configure_driver()
    login_to_instagram(driver, username, password)  # Log into Instagram before scraping
    results = []

    for url in instagram_urls:
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "x1lliihq")))
            bio_link_text = extract_bio_url(driver)
            results.append({
                'Instagram URL': url,
                'Bio URL': bio_link_text or "N/A"
            })
        except TimeoutException:
            results.append({
                'Instagram URL': url,
                'Bio URL': "N/A"
            })
        except WebDriverException as e:
            results.append({
                'Instagram URL': url,
                'Bio URL': f"Error: {str(e)}"
            })

    driver.quit()
    return results

# Usage example
instagram_urls = [
"https://www.instagram.com/_themarketingmind_/",
"https://www.instagram.com/legalmuze/",
"https://www.instagram.com/alliancetimemedia/",
"https://www.instagram.com/vakeelkhoj/",
"https://www.instagram.com/gourlegalassociates/",
"https://www.instagram.com/a.c.e_arts_/",
"https://www.instagram.com/acidcatproductions/",
"https://www.instagram.com/baazbikes/",
"https://www.instagram.com/kuwar_designs/",
"https://www.instagram.com/riiunf1ltered/",
"https://www.instagram.com/paramlodaya7/",
"https://www.instagram.com/suhani_artzone/",
"https://www.instagram.com/art_hash_/",
"https://www.instagram.com/quackk.a.doodle/",
"https://www.instagram.com/monishas_design/",
"https://www.instagram.com/stop_n_stare_7/",
"https://www.instagram.com/its_dog.junction/",
"https://www.instagram.com/mouldy_louboutons/",
"https://www.instagram.com/devs_designwork/",
"https://www.instagram.com/_farmiskin/",
"https://www.instagram.com/_jkothari_/",
"https://www.instagram.com/_.artistics._07/",
"https://www.instagram.com/small.world/",
"https://www.instagram.com/why.not_designers/",
"https://www.instagram.com/_____artville_____/",
"https://www.instagram.com/https://bluezonevitrified.com//",
"https://www.instagram.com/shambhu_edits_04/",
"https://www.instagram.com/minimaxcreations/",
"https://www.instagram.com/minimaxmusicclub/",
"https://www.instagram.com/graphic_pallete/",
"https://www.instagram.com/sjgraphic_designer/",
"https://www.instagram.com/aesthete_voyage/",
"https://www.instagram.com/slayi_ngart/",
"https://www.instagram.com/homemadefood__sg/",
"https://www.instagram.com/seasonalspectra/",
"https://www.instagram.com/the_designallure/",
"https://www.instagram.com/ssoulwhisperer/",
"https://www.instagram.com/_sweet.scented/",
"https://www.instagram.com/zikvaa_/",
"https://www.instagram.com/catslikepeaches/",
"https://www.instagram.com/spandan.psd/",
"https://www.instagram.com/bansal_design_lab_/",
"https://www.instagram.com/the_artsy_yellow/",
"https://www.instagram.com/_shivankaam_/",
"https://www.instagram.com/abhinowv/",
"https://www.instagram.com/castle_crewarts_/",
"https://www.instagram.com/design_with_vivek/",
"https://www.instagram.com/suryanshxdesign/",
"https://www.instagram.com/artsysnoop/",
"https://www.instagram.com/rudrarts/",
"https://www.instagram.com/cursed.mind/",
"https://www.instagram.com/artthrobe/",
"https://www.instagram.com/candlesbyli.in/",
"https://www.instagram.com/artsy_blends25/",
"https://www.instagram.com/_upstart.art._/",
"https://www.instagram.com/tarish_photography/",
"https://www.instagram.com/infaefx/",
"https://www.instagram.com/bakedbyannzz/",
"https://www.instagram.com/beadscape_creations/",
"https://www.instagram.com/80degreefootwear/",
"https://www.instagram.com/artby.radz/",
"https://www.instagram.com/dishanlifecare/",
"https://www.instagram.com/wear.kivi/",
"https://www.instagram.com/sigmaboyperfumeclub/",
"https://www.instagram.com/_khoj_/",
"https://www.instagram.com/freak_kicks_/",
"https://www.instagram.com/think_b_yond/",
"https://www.instagram.com/lens_klicks/",
"https://www.instagram.com/zerento.co/",
"https://www.instagram.com/art._.attic05/",
"https://www.instagram.com/rajesh_sarees/",
"https://www.instagram.com/its.carryculture/",
"https://www.instagram.com/just_different_view/",
"https://www.instagram.com/livesthepoetryshecantwrite/",
"https://www.instagram.com/__artjournal__/",
"https://www.instagram.com/art.by.abhi.i/",
"https://www.instagram.com/divishirecords/",
"https://www.instagram.com/nomadic.explorer_/",
"https://www.instagram.com/artxkosmos/",
"https://www.instagram.com/rookiemedia.in/",
"https://www.instagram.com/https://directbysammy.art//",
"https://www.instagram.com/thereddoor26/",
"https://www.instagram.com/pritryingphotography/",
"https://www.instagram.com/travel_with_krutika/",
"https://www.instagram.com/_the_design_box/",
"https://www.instagram.com/_hastag.shuterbug_/",
"https://www.instagram.com/patakka.studios/",
"https://www.instagram.com/desi.gnsby.sk/",
"https://www.instagram.com/ashiy_photography/",
"https://www.instagram.com/lj.drawss/",
"https://www.instagram.com/grapevine.animations/",
"https://www.instagram.com/portraitin_life/",
"https://www.instagram.com/musical.seconds/"]
username = 'nbs_untold_'
password = ''
results = scrape_instagram_links(instagram_urls, username, password)
df = pd.DataFrame(results)
df.to_csv("instagram_bio_links.csv", index=False)
print("Scraping complete. Results saved to CSV.")

