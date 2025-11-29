import time
import random

# Định nghĩa các dịch vụ giả lập
DICH_VU_GIẢ_LẬP = {
    "1": "Tăng Lượt Theo Dõi (FL) Giả lập",
    "2": "Tăng Lượt Thích (TIM) Giả lập",
    "3": "Tăng Lượt Xem (VIEW) Giả lập"
}

def hien_thi_menu():
    """Hiển thị menu và yêu cầu người dùng chọn dịch vụ."""
    print("\n" + "="*50)
    print("🤖 HỆ THỐNG MÔ PHỎNG TĂNG SỐ LIỆU (MỤC ĐÍCH HỌC TẬP) 🤖")
    print("Vui lòng chọn dịch vụ bạn muốn mô phỏng:")
    for key, value in DICH_VU_GIẢ_LẬP.items():
        print(f"[{key}] {value}")
    print("[0] Thoát chương trình")
    print("="*50)

def nhap_lua_chon(max_lua_chon):
    """Xử lý nhập liệu và kiểm tra lựa chọn."""
    while True:
        lua_chon = input("👉 Nhập số lựa chọn của bạn: ")
        if lua_chon.isdigit() and 0 <= int(lua_chon) <= max_lua_chon:
            return lua_chon
        print("❌ Lựa chọn không hợp lệ. Vui lòng nhập số từ 0 đến 3.")

def chay_mo_phong(ten_dv, link, so_muc_tieu):
    """Chạy mô phỏng bộ đếm tăng dần."""
    so_hien_tai = 0
    print("\n--- BẮT ĐẦU MÔ PHỎNG ---")
    print(f"Dịch vụ: **{ten_dv}**")
    print(f"Link: **{link}**")
    print(f"Mục tiêu: **{so_muc_tieu:,}**")
    print("-" * 30)
    
    # Số lần cập nhật tối đa để giữ tốc độ ổn định
    so_lan_cap_nhat = 0

    while so_hien_tai < so_muc_tieu:
        # 1. Cộng Random từ 1 đến 3 (theo yêu cầu)
        buoc_tang = random.randint(1, 3) 
        
        # 2. Cộng bước tăng vào số hiện tại
        so_hien_tai += buoc_tang
        
        # Đảm bảo không vượt quá số mục tiêu
        if so_hien_tai > so_muc_tieu:
            so_hien_tai = so_muc_tieu
        
        # In kết quả mô phỏng
        print(f"➕ +{buoc_tang:<3} | {ten_dv} hiện tại: **{so_hien_tai:,} / {so_muc_tieu:,}**")
        
        # Tạm dừng ngắn để tạo hiệu ứng "đang chạy"
        time.sleep(0.01) 
        
        # Giới hạn số lần in ra màn hình để tránh quá tải
        so_lan_cap_nhat += 1
        if so_lan_cap_nhat > 1000:
            # Nếu chạy quá 1000 lần, chỉ nhảy thẳng đến kết quả cuối cùng để tiết kiệm thời gian
            so_hien_tai = so_muc_tieu
            print("... (Quá trình mô phỏng được tăng tốc) ...")

    print("-" * 30)
    print(f"🎉 **CHÚC MỪNG!** Đã hoàn thành mô phỏng cho {ten_dv}.")
    print(f"Tổng số đạt được: **{so_hien_tai:,}**")
    print("--------------------------")


# --- LOGIC CHƯƠNG TRÌNH CHÍNH ---
def main():
    while True:
        hien_thi_menu()
        chon = nhap_lua_chon(len(DICH_VU_GIẢ_LẬP))

        if chon == "0":
            print("\nCảm ơn bạn đã sử dụng chương trình mô phỏng. Tạm biệt!")
            break
        
        # Lấy tên dịch vụ đã chọn
        ten_dich_vu = DICH_VU_GIẢ_LẬP[chon]
        
        print(f"Bạn đã chọn: **{ten_dich_vu}**")
        
        # --- Bước 2: Nhập link cần buff ---
        link_can_buff = input(f"🔗 Nhập **Link** cần mô phỏng {ten_dich_vu}: ")
        
        # --- Bước 3: Nhập số lượng ---
        while True:
            try:
                so_luong = int(input("🔢 Nhập **Số lượng Mục tiêu** (ví dụ: 10000): "))
                if so_luong > 0:
                    break
                else:
                    print("❌ Số lượng phải là số nguyên dương.")
            except ValueError:
                print("❌ Đầu vào không hợp lệ. Vui lòng chỉ nhập số.")

        # --- Bước 4: Chạy mô phỏng ---
        chay_mo_phong(ten_dich_vu, link_can_buff, so_luong)

if __name__ == "__main__":
    main()
