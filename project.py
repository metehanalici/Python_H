import cv2
import pandas as pd
from pyzbar.pyzbar import decode

# Excel dosyasını yükle
excel_dosyasi = 'balo.xlsx'
df = pd.read_excel(excel_dosyasi)

# Kamerayı aç
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    isim_bulundu = False
    eslesen_ad_soyad = ''  # Eşleşen kişinin ad soyadını saklamak için boş bir string oluştur

    # QR kodu okuv
    for barcode in decode(frame):
        myData = barcode.data.decode('utf-8')
        print('QR Kodu:', myData)  # QR kodundan alınan veriyi yazdır

        # Excel'deki AD SOYAD sütununu tara
        for index, row in df.iterrows():
            ad_soyad = row['AD SOYAD']
            print('Aranan:', ad_soyad)  # Aranan ismi yazdır

            if myData == ad_soyad:
                print('Eşleşme Bulundu!')  # Eşleşme olduğunda yazdır
                isim_bulundu = True
                eslesen_ad_soyad = ad_soyad  # Eşleşen kişinin ad soyadını sakla
                cv2.putText(frame, f'Onaylandi: {ad_soyad}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                break

    cv2.imshow('QR Kod Okuyucu', frame)
    key = cv2.waitKey(1)
    if key == ord('q') or isim_bulundu:
        while True:
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('c'):
                cv2.destroyAllWindows()
                break

cap.release()
cv2.destroyAllWindows()





