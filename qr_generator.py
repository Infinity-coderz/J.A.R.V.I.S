import qrcode as qr
import time
import pyfiglet as draw

def qr_gen():
    try:
        big = draw.figlet_format("QR code")
        print(big)

        command = print("Press 'q' to exit the program...")

        png_counter = 1
        png_counter += 1

        WEB_URL = input("Enter the name of website to generate qrcode : ")
        qrcode = qr.make(WEB_URL)
        qrcode.save(f"qr_imgs/qrcode_{png_counter}.png")

        time.sleep(1)

        print("Done! QR code has been generated successfully")
        qrcode.show()

        if command == 'q':
            print("Exiting the program...")
            exit()
    except Exception as e:
        print(e)

if __name__ == "__main__":

    while True:
        qr_gen()
