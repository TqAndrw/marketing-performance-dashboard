import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# --- CẤU HÌNH THÔNG SỐ (CONFIG) ---
# Số lượng ngày muốn tạo (1 năm + 1 tháng để so sánh YoY nếu cần)
days_to_generate = 395 
start_date = datetime(2025, 1, 1)

# Danh sách các Platform và đặc tính giả lập của chúng
# CTR: Click Through Rate (Tỷ lệ nhấp)
# CPC: Cost Per Click (Giá mỗi click - USD)
# CR: Conversion Rate (Tỷ lệ chuyển đổi ra đơn hàng)
# AOV: Average Order Value (Giá trị trung bình đơn hàng - USD)
platforms = {
    'Facebook Ads': {
        'ctr_base': 0.015, 'ctr_var': 0.005, 
        'cpc_base': 0.8, 'cpc_var': 0.3, 
        'cr_base': 0.025, 'cr_var': 0.01,
        'aov_base': 45, 'aov_var': 15
    },
    'Google Ads': {
        'ctr_base': 0.045, 'ctr_var': 0.015, # Search intent cao -> CTR cao
        'cpc_base': 1.5, 'cpc_var': 0.5,     # Giá thầu Google thường đắt
        'cr_base': 0.04, 'cr_var': 0.015,
        'aov_base': 60, 'aov_var': 20
    },
    'TikTok Ads': {
        'ctr_base': 0.008, 'ctr_var': 0.003, # Lướt nhanh -> CTR thấp
        'cpc_base': 0.4, 'cpc_var': 0.2,     # Giá rẻ
        'cr_base': 0.01, 'cr_var': 0.005,    # Chuyển đổi thấp
        'aov_base': 30, 'aov_var': 10
    }
}

# Các loại chiến dịch
campaign_types = ['Awareness', 'Traffic', 'Sales_Conversion', 'Retargeting']

data = []

print("Đang khởi tạo dữ liệu mô phỏng...")

for i in range(days_to_generate):
    current_date = start_date + timedelta(days=i)
    
    # --- YẾU TỐ MÙA VỤ (SEASONALITY) ---
    # Cuối năm (Tháng 11, 12) traffic tăng 1.5 lần, Đầu năm giảm nhẹ
    seasonality_factor = 1.0
    if current_date.month in [11, 12]:
        seasonality_factor = 1.5
    elif current_date.month in [1, 2]:
        seasonality_factor = 0.8
        
    # Tạo biến động ngẫu nhiên hàng ngày (Daily Noise) +/- 10%
    daily_noise = random.uniform(0.9, 1.1)
    
    for platform, metrics in platforms.items():
        # Mỗi platform chạy 2-4 campaigns mỗi ngày
        num_campaigns = random.randint(2, 4)
        
        for _ in range(num_campaigns):
            # Chọn ngẫu nhiên loại chiến dịch
            camp_type = random.choice(campaign_types)
            
            # Tên chiến dịch (Ví dụ: FB_Sales_TetHoliday)
            camp_name = f"{platform.split()[0]}_{camp_type}_{current_date.strftime('%B')}"
            
            # 1. Tính Impressions (Lượt hiển thị)
            # Base impressions từ 5,000 đến 50,000 tùy platform
            base_imp = random.randint(5000, 50000) 
            if platform == 'TikTok Ads': base_imp *= 1.5 # TikTok viral hơn
            
            impressions = int(base_imp * seasonality_factor * daily_noise)
            
            # 2. Tính Clicks dựa trên CTR
            # CTR thực tế = Base + Biến động
            actual_ctr = max(0.001, np.random.normal(metrics['ctr_base'], metrics['ctr_var']))
            # Retargeting thường có CTR cao hơn
            if camp_type == 'Retargeting': actual_ctr *= 1.3
            
            clicks = int(impressions * actual_ctr)
            
            # 3. Tính Cost (Chi phí) dựa trên CPC
            actual_cpc = max(0.05, np.random.normal(metrics['cpc_base'], metrics['cpc_var']))
            cost = round(clicks * actual_cpc, 2)
            
            # 4. Tính Conversions (Đơn hàng) dựa trên CR
            actual_cr = max(0, np.random.normal(metrics['cr_base'], metrics['cr_var']))
            # Chiến dịch Awareness thường ít đơn hàng
            if camp_type == 'Awareness': actual_cr *= 0.1
            if camp_type == 'Retargeting': actual_cr *= 1.4
            
            conversions = int(clicks * actual_cr)
            
            # 5. Tính Revenue (Doanh thu)
            actual_aov = max(10, np.random.normal(metrics['aov_base'], metrics['aov_var']))
            revenue = round(conversions * actual_aov, 2)
            
            # Thêm vào dataset
            data.append([
                current_date.strftime('%Y-%m-%d'),
                platform,
                camp_name,
                camp_type,
                impressions,
                clicks,
                cost,
                conversions,
                revenue
            ])

# Tạo DataFrame
df = pd.DataFrame(data, columns=[
    'Date', 'Platform', 'Campaign_Name', 'Campaign_Type', 
    'Impressions', 'Clicks', 'Cost', 'Conversions', 'Revenue'
])

# Thêm logic: Không thể có Revenue nếu Conversions = 0
df.loc[df['Conversions'] == 0, 'Revenue'] = 0

# Xuất ra file CSV
output_file = 'Marketing_Data_Project1.csv'
df.to_csv(output_file, index=False)

print(f"Xong! Đã tạo file '{output_file}' với {len(df)} dòng dữ liệu.")
print(df.head())
