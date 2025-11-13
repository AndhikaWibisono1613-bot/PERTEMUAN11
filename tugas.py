# PERTEMUAN11

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://lms.unm.ac.id/"
USERNAME = "240210501056"
PASSWORD = "Maba24ft"

# Setup Chrome
opts = Options()
opts.add_argument("--start-maximized")
service = Service()
driver = webdriver.Chrome(service=service, options=opts)
wait = WebDriverWait(driver, 20)

try:
    print("Membuka halaman LMS...")
    driver.get(URL)

    print("Klik Login/Register...")
    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mm-0"]/div[1]/header/div/nav/ul[2]/li[1]/a/span'))
    )
    driver.execute_script("arguments[0].click();", login_button)
    time.sleep(2)

    print("Mengisi username dan password...")
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_username"]')))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_password"]')))
    username_field.clear()
    username_field.send_keys(USERNAME)
    password_field.clear()
    password_field.send_keys(PASSWORD)

    submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/form/button'))
    )
    driver.execute_script("arguments[0].click();", submit_button)
    print("Login dikirim...")

    # === BAGIAN 2: Masuk ke mata kuliah ===
    print("Membuka mata kuliah...")
    course_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='mcc_view' and contains(text(),'View')]")))
    driver.execute_script("arguments[0].click();", course_link)
    time.sleep(4)

        # === BAGIAN 3: Klik Pengantar Perkuliahan ===
    print("Masuk ke Pengantar Perkuliahan...")


    try:
        # Cari link dengan teks 'Pengantar Perkuliahan'
        pengantar = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//a[contains(@class,'accordion-toggle') and normalize-space(text())='Pengantar Perkuliahan']"
        )))
        
        # Scroll agar terlihat
        driver.execute_script("arguments[0].scrollIntoView(true);", pengantar)
        time.sleep(1)

        # Klik panel Pengantar Perkuliahan
        driver.execute_script("arguments[0].click();", pengantar)
        print("✅ Klik Pengantar Perkuliahan berhasil.")
        time.sleep(3)

        # Tunggu hingga panel terbuka (absensi muncul)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='module-695962']")))
        print("✅ Panel terbuka dan elemen Absensi terdeteksi.")

    except Exception as e:
        print(f"❌ Gagal klik Pengantar Perkuliahan: {e}")


    # === BAGIAN 4: Klik menu Absensi ===
    print("Membuka halaman Absensi...")
    absen_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="module-695962"]/div/div/div[2]/div[1]/a/span')))
    driver.execute_script("arguments[0].click();", absen_button)
    time.sleep(4)

    # === BAGIAN 5: Klik tombol 'Submit Absen' ===
    print("Klik tombol Submit Absen...")

    try:
        # Tunggu elemen muncul di DOM
        submit_absen = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ccn-main"]/table[1]/tbody/tr[6]/td[3]/a'))
        )

        # Scroll ke bawah agar tombol terlihat
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_absen)
        time.sleep(1.5)

        # Tunggu tombol bisa diklik
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ccn-main"]/table[1]/tbody/tr[6]/td[3]/a')))
        driver.execute_script("arguments[0].click();", submit_absen)
        print("✅ Tombol Submit Absen berhasil diklik.")
        time.sleep(2)

    except Exception as e:
        print(f"❌ Gagal klik tombol Submit Absen: {e}")

    # === BAGIAN 6: Pilih 'Hadir' ===
    print("Memilih opsi Hadir...")
    hadir_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_status_520420"]')))
    driver.execute_script("arguments[0].click();", hadir_option)
    time.sleep(2)

    # === BAGIAN 7: Klik 'Save Absen' ===
    print("Menyimpan absensi...")
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_submitbutton"]')))
    driver.execute_script("arguments[0].click();", save_button)
    time.sleep(3)

    print("✅ Absen berhasil disubmit!")

except Exception as e:
    print(f"❌ Terjadi error: {e}")

finally:
    print("\nMenutup browser...")
    time.sleep(5)
    driver.quit()
