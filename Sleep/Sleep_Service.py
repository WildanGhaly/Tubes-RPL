import Sleep as S
import csv
from datetime import datetime

class Sleep_Service(S.Sleep):
    def __init__(self):
        super().__init__()
        
    def validate_sleep(self, jam_start, menit_start, jam_selesai, menit_selesai):
        if (len(jam_start) == 0 or len(menit_start) == 0 or len(jam_selesai) == 0 or len(menit_selesai) == 0):
            return False
        if (not jam_start.isnumeric() and not menit_start.isnumeric() and not jam_selesai.isnumeric() and not menit_selesai.isnumeric()):
            return False
        if (int(jam_start) < 0 or int(jam_start) > 24 or int(menit_start) < 0 or int(menit_start) > 60 or int(jam_selesai) < 0 or int(jam_selesai) > 24 or int(menit_selesai) < 0 or int(menit_selesai) > 60):
            return False
        return True
    
    def create_sleep(self, jam_start, menit_start, jam_selesai, menit_selesai):
        jam_start = int(jam_start)
        menit_start = int(menit_start)
        jam_selesai = int(jam_selesai) 
        menit_selesai = int(menit_selesai) 
        durasi = self.duration_count(jam_start, menit_start, jam_selesai, menit_selesai)
        nama_file = "Sleep.csv"
        now = datetime.now()
        date_time = now.strftime("%m%d%Y%H%M%S")
        with open(nama_file, mode='a', newline='') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow([date_time, jam_start, menit_start, durasi])
            
        

    def duration_count(self, jam_start, menit_start, jam_selesai, menit_selesai):
        if jam_selesai < jam_start:
            jam_selesai += 24
            
        durasi_jam = jam_selesai - jam_start
        durasi_menit = 0
        
        if menit_selesai < menit_start:
            durasi_jam -= 1
            durasi_menit = 60 - (menit_start - menit_selesai)
        else:
            durasi_menit = menit_selesai - menit_start
        
        durasi = durasi_jam * 60 + durasi_menit
        return durasi
