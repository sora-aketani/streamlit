import pandas as pd
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# タイトル
st.title('GAFA株価の可視化アプリ')

# 株式ティッカーシンボルの入力
tickers = ['GOOGL', 'AAPL', 'META', 'AMZN']
selected_tickers = st.multiselect('表示したい銘柄を選択してください:', tickers, default=tickers)

# 日付範囲の選択
start_date = st.date_input('開始日', value=pd.Timestamp('2023-01-01'))
end_date = st.date_input('終了日', value=pd.Timestamp('2023-12-31'))

# 株価データの取得と表示
if st.button('データを取得して可視化'):
    if selected_tickers:
        # 株価データを取得
        data = yf.download(selected_tickers, start=start_date, end=end_date)['Close']

        # データをテーブル表示
        st.subheader('株価データ（表形式）')
        st.dataframe(data)  # 動的な表を表示

        # データをグラフで可視化
        st.subheader('株価データ（グラフ）')
        st.line_chart(data)
    else:
        st.warning('少なくとも1つの銘柄を選んでください。')
        
