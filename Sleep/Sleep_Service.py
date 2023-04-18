import Sleep.Sleep as S
import csv
from datetime import datetime

class Sleep_Service(S.Sleep):
    def __init__(self):
        super().__init__()
        
    def validate_sleep(self, jam_start, menit_start, jam_selesai, menit_selesai):
        if (len(jam_start) != 2 or len(menit_start) != 2 or len(jam_selesai) != 2 or len(menit_selesai) != 2):
            return False
        if (not jam_start.isnumeric() and not menit_start.isnumeric() and not jam_selesai.isnumeric() and not menit_selesai.isnumeric()):
            return False
        if (int(jam_start) < 0 or int(jam_start) > 23 or int(menit_start) < 0 or int(menit_start) > 59 or int(jam_selesai) < 0 or int(jam_selesai) > 23 or int(menit_selesai) < 0 or int(menit_selesai) > 59):
            return False
        if (int(jam_start) == int(jam_selesai) and int(menit_start) == int(menit_selesai)):
            return False
        return True
    
    def create_sleep(self, jam_start, menit_start, jam_selesai, menit_selesai):
        # Setup variable
        bulan_31 = [1, 3, 5, 7, 8, 10, 12]
        bulan_30 = [4, 6, 9, 11]
        nama_file = "Sleep.csv"
        now = datetime.now()
        date_time = now.strftime("%d%m%Y")
        Year = int(now.strftime("%Y"))
        date_time += jam_start + menit_start
        jam_start = int(jam_start)
        menit_start = int(menit_start)
        jam_selesai = int(jam_selesai) 
        menit_selesai = int(menit_selesai)

        ## Ketika waktu selesai tidur di hari yang berbeda
        if (jam_start > jam_selesai) or (jam_start == jam_selesai and menit_start > menit_selesai):
            durasi = self.duration_count(jam_start, menit_start, 24, 0)
            with open(nama_file, mode='a', newline='') as file_csv:
                writer = csv.writer(file_csv)
                writer.writerow([date_time, jam_start, menit_start, durasi])

            durasi = self.duration_count(jam_start, menit_start, jam_selesai, menit_selesai)

            # Ketika bulan saat ini di bulan 31
            if now.strftime("%m") in bulan_31:
                if now.strftime("%d") == "31":
                    if now.strftime("%m") == "12":
                        date_time = "0101" + str(int(now.strftime("%Y")) + 1) + "0000"
                    else:
                        date_time = "01" + str(int(now.strftime("%m")) + 1) + now.strftime("%Y") + "0000"
                
                else:
                    date_time = "0" + str(int(now.strftime("%d")) + 1) + now.strftime("%m%Y") + "0000"

            # Ketika bulan saat ini di bulan 30
            elif now.strftime("%m") in bulan_30:
                if now.strftime("%d") == "30":
                    date_time = "01" + str(int(now.strftime("%m")) + 1) + now.strftime("%Y") + "0000"
                else:
                    date_time = "0" + str(int(now.strftime("%d")) + 1) + now.strftime("%m%Y") + "0000"
            else:
                if self.is_kabisat(Year):
                    if now.strftime("%d") == "29":
                        date_time = "01" + str(int(now.strftime("%m")) + 1) + now.strftime("%Y") + "0000"
                    else:
                        date_time = "0" + str(int(now.strftime("%d")) + 1) + now.strftime("%m%Y") + "0000"
                else:
                    if now.strftime("%d") == "28":
                        date_time = "01" + str(int(now.strftime("%m")) + 1) + now.strftime("%Y") + "0000"
                    else:
                        date_time = "0" + str(int(now.strftime("%d")) + 1) + now.strftime("%m%Y") + "0000"

            with open(nama_file, mode='a', newline='') as file_csv:
                writer = csv.writer(file_csv)
                writer.writerow([date_time, 0, 0, durasi])

        ## Ketika waktu selesai tidur di hari yang sama
        else:
            durasi = self.duration_count(jam_start, menit_start, jam_selesai, menit_selesai)
            with open(nama_file, mode='a', newline='') as file_csv:
                writer = csv.writer(file_csv)
                writer.writerow([date_time, jam_start, menit_start, durasi])
            
        

    def duration_count(self, jam_start, menit_start, jam_selesai, menit_selesai):
        if (jam_selesai < jam_start) or (jam_selesai == jam_start and menit_selesai < menit_start):
            durasi = jam_selesai * 60 + menit_selesai
        else:
            durasi_jam = jam_selesai - jam_start
            durasi_menit = 0
            if menit_selesai < menit_start:
                durasi_jam -= 1
                durasi_menit = 60 - (menit_start - menit_selesai)
            else:
                durasi_menit = menit_selesai - menit_start
            
            durasi = durasi_jam * 60 + durasi_menit
        
        return durasi
    
    def is_kabisat(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    
