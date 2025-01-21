#This tools created by ./DaxxzXploit
#If you want to use this script you can tell me in my Telegram
# https://t.me/DaxxzXploit

import re
import requests
import whois
from email.parser import Parser
from ipwhois import IPWhois
from colorama import Fore, init
import exifread
from pymediainfo import MediaInfo
from bs4 import BeautifulSoup
import os
import sys
import platform
import time
import getpass

# Fungsi mencetak teks perlahan
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

# Fungsi membersihkan terminal
def clear_terminal():
    os.system("cls" if platform.system() == "Windows" else "clear")

# Inisialisasi Colorama
init(autoreset=True)

# Proses login
clear_terminal()
slowprint("Starting...")
time.sleep(2)
clear_terminal()
USERNAME = "daxxzxploit"
PASSWORD = "daxxzxploit"

input_username = input("Masukkan Username: ")
input_password = getpass.getpass("Masukkan Password: ")

if USERNAME != input_username or PASSWORD != input_password:
    print(Fore.RED + "Login Gagal. Keluar program.")
    sys.exit()

clear_terminal()
logonya = Fore.CYAN + '''
   _____ ______  __   __________  ____  __   _____
  / ___// __ \ \/ /  /_  __/ __ \/ __ \/ /  / ___/
  \__ \/ /_/ /\  /    / / / / / / / / / /   \__ \ 
 ___/ / ____/ / /    / / / /_/ / /_/ / /______/ / 
/____/_/     /_/    /_/  \____/\____/_____/____/  
                                                  
            Create By./DaxxzXploit   
               t.me/DaxxzXploit
'''

def get_phone_number_info(phone_number, api_key):
    """
    Mengambil informasi terkait nomor telepon menggunakan Numverify API.
    
    Parameters:
        phone_number (str): Nomor telepon yang ingin diperiksa.
        api_key (str): API key dari Numverify.
        
    Returns:
        dict: Informasi terkait nomor telepon.
    """
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data.get("valid"):
            return {
                "Valid": data.get("valid"),
                "Number": data.get("number"),
                "Local Format": data.get("local_format"),
                "International Format": data.get("international_format"),
                "Country Name": data.get("country_name"),
                "Location": data.get("location"),
                "Carrier": data.get("carrier"),
                "Line Type": data.get("line_type")
            }
        else:
            return {"Error": "Nomor telepon tidak valid atau tidak ditemukan."}
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

# Contoh penggunaan
def main_telepon():
    API_KEY = "eM7E1j19zavWHfvkOdYK4jRk7wvEQNSS"  # Ganti dengan API key Anda
    phone_number = input("Masukkan nomor telepon (dengan kode negara): ")
    
    info = get_phone_number_info(phone_number, API_KEY)
    for key, value in info.items():
        print(f"{key}: {value}")

def get_ip_info(ip_address):
    """Mengambil informasi IP menggunakan API ipinfo.io"""
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}

def get_domain_info(domain):
    """Mengambil informasi domain menggunakan API whoisxmlapi.com"""
    api_key = "at_c3iGj9w02cERxu4HTYuLi4LUUABOW"  # Masukkan API Key Anda
    url = f"https://whoisxmlapi.com/whoisserver/WhoisService?apiKey={api_key}&domainName={domain}&outputFormat=JSON"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}

def search_username(username):
    """Mencari username di media sosial menggunakan https://github.com/sherlock-project/sherlock"""
    try:
        response = requests.get(f"https://usersearch.org/api/v1/lookup?username={username}")
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}

def get_email_domain_info(email):
    domain = email.split('@')[1]  # Mendapatkan domain dari email
    print(f"Domain: {domain}")
    
    # Melakukan pencarian WHOIS pada domain
    try:
        domain_info = whois.whois(domain)
        print("Informasi Domain WHOIS:")
        print(domain_info)
    except Exception as e:
        print(f"Error while fetching WHOIS information: {e}")

def get_ip_location(ip_address):
    try:
        ipwhois = IPWhois(ip_address)
        ip_info = ipwhois.lookup_rdap()
        print("Informasi Lokasi IP:")
        print(ip_info)
    except Exception as e:
        print(f"Error while looking up IP: {e}")

def extract_ip_from_header(header):
    # Mengekstrak alamat IP dari header email
    lines = header.split('\n')
    for line in lines:
        if 'Received:' in line:
            parts = line.split(' ')
            for part in parts:
                if part.startswith('[') and part.endswith(']'):
                    return part.strip('[]')
    return None

def get_email_header_info(header):
    ip_address = extract_ip_from_header(header)
    if ip_address:
        print(f"IP Address Found: {ip_address}")
        get_ip_location(ip_address)
    else:
        print("No IP Address found in the header.")

def main():
    # Contoh email yang dianalisis
    email = input("Masukan Email: ")
    print(f"Analyzing email: {email}")
    get_email_domain_info(email)

    # Header email yang dapat diperoleh dari email yang dikirim
    # Berikut adalah contoh header email yang harus diubah sesuai dengan header asli
    email_header = """Return-Path: <someone@example.com>
Received: from mail.example.com ([192.168.1.1]) by mailserver.com with ESMTP; Fri, 19 Jan 2025 09:00:00 +0000
From: Someone <someone@example.com>
To: Me <me@example.com>
Subject: Test Email
Date: Fri, 19 Jan 2025 09:00:00 +0000"""

    get_email_header_info(email_header)

def search_social_media(name):
    """
    Mencari nama lengkap di beberapa platform media sosial.
    """
    platforms = {
        "Twitter": f"https://twitter.com/{name}",
        "Instagram": f"https://www.instagram.com/{name}/",
        "Facebook": f"https://www.facebook.com/{name}",
        "LinkedIn": f"https://www.linkedin.com/in/{name}/"
    }

    for platform, url in platforms.items():
        print(Fore.YELLOW + f"\n[*] Mencari di {platform}...")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(Fore.GREEN + f"[{platform}] Profil ditemukan: {url}")
            elif response.status_code == 404:
                print(Fore.RED + f"[{platform}] Profil tidak ditemukan.")
            else:
                print(Fore.RED + f"[{platform}] Terjadi kesalahan saat mengakses {url}")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"[{platform}] Terjadi kesalahan: {str(e)}")
            
def extract_gps_info(tags):
    def convert_to_degrees(value):
        d = float(value[0].num) / float(value[0].den)
        m = float(value[1].num) / float(value[1].den)
        s = float(value[2].num) / float(value[2].den)
        return d + (m / 60.0) + (s / 3600.0)

    gps_info = {}
    if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
        lat = tags["GPS GPSLatitude"]
        lat_ref = tags["GPS GPSLatitudeRef"]
        lon = tags["GPS GPSLongitude"]
        lon_ref = tags["GPS GPSLongitudeRef"]

        latitude = convert_to_degrees(lat.values)
        if lat_ref.values[0] != "N":
            latitude = -latitude

        longitude = convert_to_degrees(lon.values)
        if lon_ref.values[0] != "E":
            longitude = -longitude

        gps_info["Latitude"] = latitude
        gps_info["Longitude"] = longitude

    return gps_info

# Ekstraksi metadata gambar
def extract_image_metadata(image_path):
    try:
        with open(image_path, 'rb') as image_file:
            tags = exifread.process_file(image_file)
        
        gps_info = extract_gps_info(tags)  # Assuming `extract_gps_info` is defined elsewhere
        metadata = {tag: str(value) for tag, value in tags.items() if tag not in ['JPEGThumbnail', 'TIFFThumbnail']}
        
        if gps_info:
            metadata.update(gps_info)
        
        return metadata
    except Exception as e:
        return {"error": f"Gagal membaca metadata gambar: {str(e)}"}

# Ekstraksi metadata video
def extract_video_metadata(video_path):
    try:
        media_info = MediaInfo.parse(video_path)
        metadata = {}
        for track in media_info.tracks:
            if track.track_type == "General":
                metadata['Duration'] = track.duration
                metadata['Format'] = track.format
                metadata['File size'] = track.file_size
                metadata['Bit rate'] = track.overall_bit_rate
            elif track.track_type == "Video":
                metadata['Resolution'] = f"{track.width}x{track.height}"
                metadata['Frame rate'] = track.frame_rate
                metadata['Codec'] = track.codec_id
        return metadata
    except Exception as e:
        return {"error": f"Gagal membaca metadata video: {str(e)}"}

def analyze_media(file_path):
    if not os.path.exists(file_path):
        return {"error": "File tidak ditemukan."}
    
    file_extension = os.path.splitext(file_path)[-1].lower()
    if file_extension in ['.jpg', '.jpeg', '.png']:
        return extract_image_metadata(file_path)
    elif file_extension in ['.mp4', '.mkv', '.avi']:
        return extract_video_metadata(file_path)
    else:
        return {"error": "Format file tidak didukung."}
        
if __name__ == "__main__":
  while True:
        print(logonya)
        print(Fore.YELLOW + "=== OSINT Tool ===")
        print(Fore.YELLOW + "1. Cari informasi IP")
        print(Fore.YELLOW + "2. Cari informasi domain")
        print(Fore.YELLOW + "3. Analisis file media (foto/video)")
        print(Fore.YELLOW + "4. Cari informasi menggunakan nama lengkap")
        print(Fore.YELLOW + "5. Cari Menggunakan Alamat Email")
        print(Fore.YELLOW + "6. Cari Menggunakan Nomor Telpon")
        print(Fore.YELLOW + "7. Clear Terminal")
        print(Fore.YELLOW + "8. Keluar Program")
        
        choice = input(Fore.YELLOW + "Pilih opsi (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            ip = input(Fore.CYAN + "Masukkan IP address: ")
            # You need to implement the get_ip_info() function
            result = get_ip_info(ip)
            print(result)

        elif choice == "2":
            domain = input(Fore.CYAN + "Masukkan nama domain: ")
            # You need to implement the get_domain_info() function
            result = get_domain_info(domain)
            print(result)

        elif choice == "3":
            file_path = input(Fore.CYAN + "Masukkan path file media: ")
            # You need to implement the analyze_media() function
            metadata = analyze_media(file_path)
            for key, value in metadata.items():
                print(f"{key}: {value}")

        elif choice == "4":
            name = input(Fore.CYAN + "Masukkan nama lengkap (gunakan nama pengguna di platform jika ada): ")
            search_social_media(name)
            
        elif choice == "5":
          main()
          
        elif choice == "6":
          main_telepon()

        elif choice == "7":
          print(Fore.GREEN + "Succes Clear Terminal!!")
          clear_terminal()

        elif choice == "8":
          print(Fore.GREEN + "Keluar Program, Terimakasih Telah Menggunakan Tools Ini!!")
          time.sleep(2)
          break  # keluar dari loop

        else:
            print(Fore.RED + "Pilihan tidak valid. Coba lagi.")