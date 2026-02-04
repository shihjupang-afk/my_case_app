import streamlit as st
import pandas as pd
from datetime import datetime

# 設定頁面資訊
st.set_page_config(page_title="藥癮個案管理系統", layout="centered")

st.title("🏥 藥癮個案管理系統")

# 側邊欄：導覽
menu = ["新增個案", "個案清單查詢"]
choice = st.sidebar.selectbox("選單", menu)

# 1. 預定義選單內容
risk_levels = ["🔴 高風險", "🟡 中風險", "🟢 低風險"]
substances = ["海洛因", "安非他命", "愷他命 (K)", "大麻", "依托咪酯 (Etomidate)", "多重藥物", "其他"]
sources = ["法院轉介", "地檢署緩起訴", "醫療機構轉介", "自行求助", "家屬代求助"]
hospitals = ["聯醫板橋", "八療土城", "亞東醫院", "聯醫三重", "完成治療", "無需治療", "社區處遇", "利伯他茲", "自行新增"]

# 2. 新增個案功能
if choice == "新增個案":
    st.header("📋 基本資料輸入")
    
    with st.form("case_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            case_id = st.text_input("個案編號", value=datetime.now().strftime("%Y-%m%d-%H%M"), help="系統自動生成建議編號")
            name = st.text_input("姓名/化名")
            phone = st.text_input("聯絡電話")
            emergency = st.text_input("緊急聯絡人 (姓名/電話)")
        
        with col2:
            risk = st.selectbox("風險等級", risk_levels)
            substance = st.selectbox("主要物質", substances)
            source = st.selectbox("個案來源", sources)
            hospital = st.selectbox("戒癮治療醫院/處遇", hospitals)
            
        st.divider()
        
        st.subheader("📅 區間設定")
        col3, col4 = st.columns(2)
        with col3:
            service_range = st.date_input("服務區間", value=[datetime.today(), datetime.today()])
        with col4:
            visit_range = st.date_input("家訪區間 (日期範圍)", value=[datetime.today(), datetime.today()])
            
        last_visit = st.date_input("最後訪視日")

        submit_button = st.form_submit_button("儲存個案資料")
        
        if submit_button:
            st.success(f"✅ 個案 {name} (編號: {case_id}) 已成功儲存！")
            st.balloons()

# 3. 個案清單查詢 (模擬清單)
elif choice == "個案清單查詢":
    st.header("📂 目前管理個案")
    
    # 這裡建立一個簡單的範例表格
    data = {
        "編號": ["2026-0001", "2026-0002"],
        "姓名": ["小明", "阿華"],
        "風險": ["🔴 高", "🟢 低"],
        "主要物質": ["依托咪酯", "大麻"],
        "醫院/狀態": ["聯醫板橋", "完成治療"],
        "下次家訪範圍": ["2026/02/10~02/17", "2026/03/01~03/07"]
    }
    df = pd.DataFrame(data)
    
    st.dataframe(df, use_container_width=True)
    st.info("提示：點擊欄位標題可進行排序")
