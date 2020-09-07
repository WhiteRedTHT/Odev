import requests

def httpsorgu():

    with open("siteler.txt", "r", encoding="utf-8") as dosya:
        siteler = [ad.replace('\n', '') for ad in dosya.readlines()]
        for ad in siteler:

                try:
                    response = requests.get(ad)

                    if response.status_code == 200:
                        with open("200.txt", "a", encoding="utf-8") as dosya2:
                            dosya2.write(ad+'\n')

                    elif response.status_code == 404:
                        with open("404.txt", "a", encoding="utf-8") as dosya3:
                            dosya3.write(ad+'\n')

                    elif response.status_code == 500:
                        with open("500.txt", "a", encoding="utf-8") as dosya4:
                            dosya4.write(ad+'\n')

                except (ConnectionError and requests.exceptions.ConnectionError) as hata:
                    print("Sitelere erişilemedi..")

print("""                          Yahoo Domain Sorgulayıcı\n 
--------------------------------------------WhiteRed---------------------------------------------
      """)

print("""
      NOT : 200 OK , 404 hatalı istek veya dosya bulunamadı hatası, 500 server hatasıdır.\n
      
      NOT 2 : 200,404 ve 500 geri dönüşleri klasöre txt dosyası olarak kaydedilecektir.\n
-------------------------------------------------------------------------------------------------
      




""")
try:
    sorgu = input("İşlem yapmak isiyorsanız 'WhiteRed' yazınız... : ")
    if sorgu == "WhiteRed":
        print("İşlem başlıyor lütfen biraz bekleyiniz...")
        httpsorgu()
    else:
        print("Lütfen 'WhiteRed' değerini giriniz aksi taktirde program çalışmayacaktır...")
except (FileNotFoundError):
    print("Lütfen 'domainssiteleri.txt' dosyasını klasöre ekleyiniz..")


                    


            
            
            
            
            
            
            
            
           sandra          
            
