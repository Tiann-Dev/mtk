import random,sys,time,os
import cmath
import calendar
import requests
import webbrowser
import itertools
import threading
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
from rich.console import Console

try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import bs4
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall bs4\n")
    os.system("pip install bs4")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install cmath")

# Warna
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'

os.system("git pull")

class Loader:
    def __init__(self, desc="Loading...", end=f"{H}Done!{P}", timeout=0.1):
        """}
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


def coli(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)

def clear():
	os.system("clear")

def kalkulator():
	print('''\n _   __      _ _          _       _             
| | / /     | | |        | |     | |            
| |/ /  __ _| | | ___   _| | __ _| |_ ___  _ __ 
|    \ / _` | | |/ / | | | |/ _` | __/ _ \| '__|
| |\  \ (_| | |   <| |_| | | (_| | || (_) | |   
\_| \_/\__,_|_|_|\_\\__,_|_|\__,_|\__\___/|_|                                                   ''')
	angka1 = input("\nMasukan Angka Ke-1 : ")
	angka2 = input("Masukan Angka Ke-2 : ")
	operator = input("Masukan Operator (+,x,:,-) : ")
	if operator == "+":
		hasil = int(angka1) + int(angka2)
		if __name__ == "__main__":
			with Loader("Sedang Di Kerjakan!..."):
				for i in range(10):
					sleep(0.25)
			loader = Loader("Memuat Hasil...", f"Hasil Dari {angka1} + {angka2} = {hasil}", 0.05).start()
			for i in range(10):
				sleep(0.25)
			loader.stop()
	elif operator == "x":
		hasil = int(angka1) * int(angka2)
		if __name__ == "__main__":
			with Loader("Sedang Di Kerjakan!..."):
				for i in range(10):
					sleep(0.25)
			loader = Loader("Memuat Hasil...", f"Hasil Dari {angka1} X {angka2} = {hasil}", 0.05).start()
			for i in range(10):
				sleep(0.25)
			loader.stop()
	elif operator == "-":
		hasil = int(angka1) - int(angka2)
		if __name__ == "__main__":
			with Loader("Sedang Di Kerjakan!..."):
				for i in range(10):
					sleep(0.25)
			loader = Loader("Memuat Hasil...", f"Hasil Dari {angka1} - {angka2} = {hasil}", 0.05).start()
			for i in range(10):
				sleep(0.25)
			loader.stop()
	elif operator == ":":
		hasil = int(angka1) / int(angka2)
		if __name__ == "__main__":
			with Loader("Sedang Di Kerjakan!..."):
				for i in range(10):
					sleep(0.25)
			loader = Loader("Memuat Hasil...", f"Hasil Dari {angka1} : {angka2} = {hasil}", 0.05).start()
			for i in range(10):
				sleep(0.25)
			loader.stop()
	else:
		coli("Pilih Yang Benar!");time.sleep(2);clear()
		return kalkulator()
	time.sleep(2)
	lagi = input("\nIngin Kalkulator Lagi? (y/t) : ")
	if lagi in ["y","Y"]:
		clear();kalkulator()
	else:
		coli("Selamat Tinggal!");time.sleep(2)

def akar_kuadrat():
	# Memasukkan Inputan Angka
	angka = float(input('Masukan Angka : '))
	# Menghitung Akar Kuadrat
	akar_kuadrat = angka ** 0.5
	#Menampilkan Hasil Akar Kuadrat
	coli('Akar Kuadrat dari %0.3f Adalah %0.3f'%(angka ,akar_kuadrat))

def luas_segitiga():
	# Menginput Alas dan Tinggi Segitiga
	alas = float(input('Masukan Alas Segitiga: '))
	tinggi = float(input('Masukan Tinggi Segitiga: '))
	
	# Hitung Luas Segitiga
	luas = (alas * tinggi) / 2
	
	#Menampilkan Hasil Perhitungan
	coli('Luas Segitiga Adalah %0.2f' %luas)

def volume_kubus():
	# Menginput Sisi Kubus
	sisi = float(input('Masukan Sisi Kubus: '))
	
	# Hitung Volume Kubus
	volume = sisi ** 3
	
	#Menampilkan Hasil Perhitungan
	coli('Volume Kubus adalah %0.2f' %volume)

def persamaan_kuadrat():
	# Menyelesaikan Persamaan Kuadrat ax**2 + bx + c = 0
	# Menginput Angka
	a = int(input('Tulis a: '))
	b = int(input('Tulis b: '))
	c = int(input('Tulis c: '))
	
	# Menghitung Diskriminan
	d = (b**2) - (4*a*c)
	
	# Menghitung x1 dan x2
	x1 = (-b-cmath.sqrt(d))/(2*a)
	x2 = (-b+cmath.sqrt(d))/(2*a)
	
	#Menampilkan Hasil x1 dan x2
	coli('Hasil Persamaan Kuadrat Adalah {0} Dan {1}'.format(x1,x2))

def tukar_nilaiVar():
	# Menginput Nilai Variabel
	x = input('Masukan Nilai X : ')
	y = input('Masukan Nilai Y : ')
	
	# Membuat Variabel tukar dan Menukar nilai Variabel lain
	tukar = x
	x = y
	y = tukar
	
	#Menampilkan Nilai Variabel Setelah Ditukar
	coli('Nilai x Setelah Ditukar adalah: {}'.format(x))
	coli('Nilai y Setelah Ditukar adalah: {}'.format(y))

def angka_acak():
	inpt = input("Masukan Batasan : ")
	print(f"Menampilkan Angka Acak antara 0 sampai {inpt}")
	hasil = random.randint(0,int(inpt))
	#Menampilkan Angka Acak
	coli(f"Angka Acak Yang Terpilih Adalah {hasil}")

def km_mil():
	# Menginput Jarak dalam Satuan Kilometer
	kilometer = float(input("Tuliskan Jarak dalam Kilometer: "))
	# Nilai Faktor Konversi
	faktor_konversi = 0.621371
	# Menghitung Jarak dalam Satuan Mil
	mil = kilometer * faktor_konversi
	#Menampilkan Hasil Konversi Jarak
	coli('%0.2f Kilometer sama dengan %0.2f Mil' %(kilometer,mil))

def celcius_fahrenheit():
	# Menginput Suhu dalam Derajat Celcius
	celcius = float(input("Tuliskan Suhu dalam Celcius: "))	
	# Menghitung Suhu dalam Derajat Fahrenheit
	fahrenheit = (celcius * 1.8) + 32	
	#Menampilkan Hasil Konversi Jarak
	coli('%0.2f Derajat Celcius sama dengan %0.2f Derajat Fahrenheit' %(celcius,fahrenheit))

def positif_negatif_nol():
	#Menginput Angka
	angka = float(input("Tulis Sebuah Angka: "))	
	#Menampilkan Kondisi Angka Positif
	if angka > 0:
		coli("Angka Positif")	
	#Menampilkan Kondisi Angka Nol   
	elif angka == 0:
		coli("Angka Nol")	
	#Menampilkan Kondisi Angka Negatif
	else:
		coli("Angka Negatif")

def ganjil_genap():
	# Menginput Angka
	angka = int(input("Tulis sebuah Angka: "))
	
	#Jika Habis Dibagi Nol, Maka Genap
	if (angka % 2) == 0:
		print("{0} adalah Bilangan Genap".format(angka))
	
	#Jika Tidak Habis Dibagi Nol, Maka Ganjil
	else:
		print("{0} adalah Bilangan Ganjil".format(angka))

def tahun_kabisat():
	# Menginput Tahun
	tahun = int(input("Tulis Sebuah Tahun: "))
	
	#Perulangan Pertama
	if (tahun % 4) == 0:
	
	#Perulangan Kedua
		if (tahun % 100) == 0:
	
		#Perulangan Ketiga
			if (tahun % 400) == 0:
	
			#Tergolong Tahun Kabisat
				print("{0} adalah Tahun Kabisat".format(tahun))
	
		#Bukan Tergolong Tahun Kabisat
			else:
				print("{0} bukan Tahun Kabisat".format(tahun))
	
	#Tergolong Tahun Kabisat
		else:
			print("{0} adalah Tahun Kabisat".format(tahun))	
	#Bukan Tergolong Tahun Kabisat
	else:
		print("{0} bukan Tahun Kabisat".format(tahun))
def masehi():
	# Menginput Tahun dan Bulan
	yy = int(input("Masukkan Tahun: "))
	mm = int(input("Masukkan Bulan: "))
	
	# Menampilkan Kalender Bulanan
	print(calendar.month(yy, mm))

def urut_abjad():
	# Menginput Kalimat
	kalimat = input("Tulis Sebuah Kalimat: ")
	
	# Memecah Kalimat menjadi Kata-Kata
	kata = kalimat.split()
	
	# Mengurutkan Kata-Kata
	kata.sort()
	
	# Menampilkan Kata-Kata yang Telah Diurutkan
	print("Berikut Urutan Kata-Kata:")
	for urut in kata:
		print(urut)

def tabel_kali():
	# Menginput Angka
	angka = int(input("Menampilkan Tabel Perkalian dari: "))
	
	# Menghitung 10 Kali dari Kisaran 1 sampai 10
	for i in range(1, 11):
	
	#Menampilkan Tabel Perkalian
		print(angka, 'x', i, '=', angka*i)

def nilai_lulus():
	#Menginput Nilai Tugas, UTS, dan UAS
	tugas = float(input("Masukkan nilai Tugas: "))
	uts = float(input("Masukkan nilai UTS: "))
	uas = float(input("Masukkan nilai UAS: "))
	
	#Menghitung Nilai Akhir sesuai dengan Bobot
	nilai =  (0.15 * tugas) + (0.35 * uts) +  (0.50 * uas)
	
	#Menentukan Grade Berdasarkan Nilai Akhir
	if nilai > 80:
		grade = 'A'
	elif nilai > 70:
		grade = 'B'
	elif nilai > 60:
		grade = 'C'
	elif nilai > 50:
		grade = 'D'
	else:
		grade = 'E'
	
	#Menentukan Status Kelulusan Berdasarkan Nilai Akhir
	if nilai > 60:
		status = 'Lulus'
	else:
		status = 'Tidak Lulus'
	
	#Menampilkan Nilai Akhir, Grade, dan Status Kelulusan
	print('Nilai Akhir: %0.2f' % nilai)
	print('Grade: {}'.format(grade))
	print('Status: {}'.format(status))

def logo():
	print(f'''
░░░░░░███████ ]▄▄▄▄▄▄▄▄▃
▂▄▅█████████▅▄▃▂
I███████████████████] {B}Mathematical Tools{P}
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...    Developed By => {H}Christian S.{P}
''')
clear()
logo()
ip = requests.get('https://api.ipify.org').text
def menu():
	coli('''	  __              __          
	 (  _ /_ _  __/  /  )__/_   _ 
	__)(-((///)(//  /(_/(//(//)(/ 
	                          _/  ''')
	print(f"1. Kalkulator	{H}(Active|On){P}")
	print("2. Menghitung Akar Kuadrat")
	print("3. Menghitung Luas Segitiga")
	print("4. Menghitung Volume Kubus")
	print("5. Menyelesaikan Persamaan Kuadrat")
	print("6. Menukar Nilai Variabel")
	print("7. Menghasilkan Angka Acak")
	print("8. Mengubah Kilometer jadi Mil")
	print("9. Mengubah Celcius jadi Fahrenheit")
	print("10. Menentukan Bilangan Positif, Negatif, atau Nol")
	print("11. Menentukan Bilangan Ganjil atau Genap")
	print("12. Menentukan Tahun Kabisat")
	print("13. Menampilkan Kalender Masehi")
	print("14. Mengurutkan Kata Sesuai Abjad")
	print("15. Menampilkan Tabel Perkalian")
	print("16. Menentukan Nilai dan Kelulusan")
	print("0. Kontak Developer\n")
	put = input("Pilih => ")

	if put in ["1","01"]:
		kalkulator()
	elif put in ["2","02"]:
		akar_kuadrat()
	elif put in ["3","03"]:
		luas_segitiga()
	elif put in ["4","04"]:
		volume_kubus()
	elif put in ["5","05"]:
		persamaan_kuadrat()
	elif put in ["6","06"]:
		tukar_nilaiVar()
	elif put in ["7","07"]:
		angka_acak()
	elif put in ["8","08"]:
		km_mil()
	elif put in ["9","09"]:
		celcius_fahrenheit()
	elif put in ["10"]:
		positif_negatif_nol()
	elif put in ["11"]:
		ganjil_genap()
	elif put in ["12"]:
		tahun_kabisat()
	elif put in ["13"]:
		masehi()
	elif put in ["14"]:
		urut_abjad()
	elif put in ["15"]:
		tabel_kali()
	elif put in ["16"]:
		nilai_lulus()
	elif put in ["p","0"]:
		url = "https://wa.me/6282257561165?text=Hai+Tian!+Saya+Pengguna+Toolsmu"
		webbrowser.open(url)
	else:
		coli("Pilih Yang Benar!");time.sleep(2);clear();logo()
		return menu()

console = Console()
koi = ["Koneksi","Ip Address","Versi Aplikasi","Versi Python","List Menu","Kestabilan Progam","Apikey","Server"]

tasks = [f"Mengecek {n}" for n in koi]
with console.status("[bold green]Sedang Mengecek...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} [green]Complete[white]")
time.sleep(1)
clear();logo();menu()
