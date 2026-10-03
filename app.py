import streamlit as st
st.image("logo.jpg.jpg")
# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính lãi tiền gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("💰APP TÍNH LÃI GỬI TIẾT KIỆM_ NGUYỄN THẢO MI💰")
st.write("Nhập thông tin khoản tiền gửi để tính số tiền lãi và tổng số tiền nhận được.")

st.divider()

# =========================
# NHẬP DỮ LIỆU
# =========================

# Số tiền gửi
tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=100_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

# Kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# =========================
# NÚT TÍNH
# =========================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Kiểm tra dữ liệu
    if tien_gui <= 0:
        st.error("Vui lòng nhập số tiền gửi lớn hơn 0.")
    
    elif lai_suat <= 0:
        st.error("Vui lòng nhập lãi suất lớn hơn 0.")
    
    else:
        # ---------------------------------
        # TÍNH TỔNG TIỀN LÃI
        # ---------------------------------
        # Công thức:
        # Tiền lãi = Tiền gốc × Lãi suất năm × Kỳ hạn / 12
        #
        # Lãi suất nhập theo % nên chia 100.
        
        tong_lai = tien_gui * (lai_suat / 100) * (ky_han / 12)

        # ---------------------------------
        # TÍNH LÃI ĐỊNH KỲ
        # ---------------------------------
        
        if hinh_thuc == "Cuối kỳ":
            lai_dinh_ky = tong_lai
            so_ky_nhan_lai = 1
            don_vi_ky = "cuối kỳ"

        elif hinh_thuc == "Hàng tháng":
            lai_dinh_ky = tien_gui * (lai_suat / 100) / 12
            so_ky_nhan_lai = ky_han
            don_vi_ky = "tháng"

        else:  # Hàng quý
            lai_dinh_ky = tien_gui * (lai_suat / 100) / 4
            so_ky_nhan_lai = ky_han // 3
            don_vi_ky = "quý"

        # ---------------------------------
        # TỔNG TIỀN NHẬN ĐƯỢC
        # ---------------------------------
        tong_tien = tien_gui + tong_lai

        # =========================
        # HIỂN THỊ KẾT QUẢ
        # =========================
        st.success("✅ TÍNH TOÁN THÀNH CÔNG")

        st.subheader("📊 Kết quả")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Tiền lãi định kỳ",
                f"{lai_dinh_ky:,.0f} VNĐ"
            )

        with col2:
            st.metric(
                "Tổng tiền lãi",
                f"{tong_lai:,.0f} VNĐ"
            )

        st.metric(
            "💰 Tổng tiền gốc + lãi",
            f"{tong_tien:,.0f} VNĐ"
        )

        st.divider()

        # =========================
        # CHI TIẾT KHOẢN GỬI
        # =========================

        st.subheader("📋 Chi tiết khoản tiền gửi")

        st.write(f"**Số tiền gửi:** {tien_gui:,.0f} VNĐ")
        st.write(f"**Kỳ hạn:** {ky_han} tháng")
        st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
        st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

        if hinh_thuc == "Cuối kỳ":
            st.info(
                f"Bạn nhận toàn bộ tiền lãi {tong_lai:,.0f} VNĐ vào cuối kỳ."
            )

        elif hinh_thuc == "Hàng tháng":
            st.info(
                f"Mỗi tháng bạn nhận khoảng {lai_dinh_ky:,.0f} VNĐ tiền lãi."
            )

        else:
            st.info(
                f"Mỗi quý bạn nhận khoảng {lai_dinh_ky:,.0f} VNĐ tiền lãi."
            )

        # =========================
        # BẢNG DÒNG TIỀN NHẬN LÃI
        # =========================

        if hinh_thuc != "Cuối kỳ":

            st.subheader("📅 Lịch nhận tiền lãi")

            if hinh_thuc == "Hàng tháng":
                so_ky = ky_han

            else:
                so_ky = ky_han // 3

            for i in range(1, so_ky + 1):
                if hinh_thuc == "Hàng tháng":
                    thoi_diem = f"Tháng {i}"
                else:
                    thoi_diem = f"Quý {i}"

                st.write(
                    f"**{thoi_diem}:** {lai_dinh_ky:,.0f} VNĐ"
                )

        else:
            st.subheader("📅 Lịch nhận tiền")

            st.write(
                f"**Cuối kỳ:** {tong_lai:,.0f} VNĐ tiền lãi"
            )

            st.write(
                f"**Tổng nhận:** {tong_tien:,.0f} VNĐ"
            )


# =========================
# GHI CHÚ
# =========================

st.divider()

st.caption(
    "📌 Công thức tính lãi đơn: Tiền lãi = Tiền gốc × Lãi suất (%/năm) × Kỳ hạn (tháng) / 12."
)

st.caption(
    "Lưu ý: Kết quả mang tính tham khảo và chưa tính các trường hợp đặc biệt "
    "như lãi nhập gốc, rút trước hạn hoặc thay đổi lãi suất."
)
