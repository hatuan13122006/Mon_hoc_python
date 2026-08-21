diem = 6.5
tuoi = 20

is_kha = (diem >= 6.5) and (diem < 8.0)
print("Điểm đạt loại Khá:", is_kha)  

is_ngoai_tuoi_lao_dong = (tuoi < 18) or (tuoi > 60)
print("Chưa đủ 18 hoặc trên 60 tuổi:", is_ngoai_tuoi_lao_dong)  

print("Phủ định điều kiện tuổi:", not is_ngoai_tuoi_lao_dong)  