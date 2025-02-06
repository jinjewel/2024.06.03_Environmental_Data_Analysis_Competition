from shapely.geometry import Point, Polygon
import folium
import pandas as pd
import numpy as np
from folium.plugins import MeasureControl


### 지역을 지도에 표시
# 중심 좌표
center = [35.8266, 129.236]

# 지도 객체 생성
m = folium.Map(location=center, zoom_start=7)

### 경상북도 경주시의 경계 좌표
Gyeongju_boundary = [
    [35.6508, 129.4498],
    [35.848, 129.5198],
    [35.8438, 129.5162],
    [35.8522, 129.4851],
    [35.8474, 129.4539],
    [35.8789, 129.4363],
    [35.8838, 129.4237],
    [35.8613, 129.4102],
    [35.8651, 129.3604],
    [35.8739, 129.3553],
    [35.877, 129.3631],
    [35.8878, 129.3612],
    [35.8913, 129.3382],
    [36.0263, 129.2776],
    [36.0701, 129.2857],
    [36.0796, 129.2743],
    [36.0729, 129.2473],
    [36.0316, 129.1889],
    [36.0544, 129.1658],
    [36.0548, 129.1511],
    [36.0359, 129.1358],
    [36.0107, 129.1448],
    [36.0054, 129.1268],
    [36.013, 129.116],
    [35.9613, 129.1164],
    [35.9314, 129.1364],
    [35.9167, 129.1187],
    [35.9398, 129.095],
    [35.941, 129.0658],
    [35.9064, 129.0264],
    [35.7379, 128.9656],
    [35.6405, 129.0748],
    [35.6467, 129.0814],
    [35.6719, 129.0678],
    [35.7029, 129.0914],
    [35.7202, 129.1554],
    [35.6973, 129.2593],
    [35.6601, 129.2557],
    [35.6473, 129.3001],
    [35.6785, 129.3567],
    [35.6508, 129.4498]  # 폴리곤을 닫기 위한 좌표
]
folium.Polygon(Gyeongju_boundary, color='blue', fill=True, fill_color='#3186cc').add_to(m)
gwangjin_poly = Polygon(Gyeongju_boundary)

### 해당 위치를 지도에 표시
# 엑셀 파일 경로
excel_file_path = "C:/Users/CBNU/Desktop/Location_recommendation/경상북도_경주시.xlsx"

# 엑셀 파일 불러오기
df_hasu = pd.read_excel(excel_file_path, sheet_name="공공하수처리시설")
df_jj = pd.read_excel(excel_file_path, sheet_name="찌꺼기처리시설")
df_gachu = pd.read_excel(excel_file_path, sheet_name="가축분뇨시설")
df_ummsig = pd.read_excel(excel_file_path, sheet_name="음식물류폐기물처리시설")

# DataFrame에서 필요한 컬럼 선택
data_1 = df_hasu[['Address', 'Latitude', 'Longitude', 'count']]
data_2 = df_jj[['Address', 'Latitude', 'Longitude', 'count']]
data_3 = df_gachu[['Address', 'Latitude', 'Longitude', 'count']]
data_4 = df_ummsig[['Address', 'Latitude', 'Longitude', 'count']]

# 데이터의 절대값에 따른 반지름 조정하기 위한 스케일링 팩터 설정
# scale_factor = 68
scale_factor = 17.5

# 공공하수처리시설 위치를 지도에 표시
for index, row in data_1.iterrows():
    radius = abs(row['count']) * scale_factor
    folium.CircleMarker([row['Latitude'], row['Longitude']], radius=radius, color='blue', fill = True, fill_color='blue', fill_opacity=0.5, tooltip=row['Address']).add_to(m)
    # folium.Marker([row['Latitude'], row['Longitude']], icon=folium.Icon(color='blue'), tooltip=row['Address']).add_to(m)

# 찌꺼기처리시설 위치를 지도에 표시
for index, row in data_2.iterrows():
    radius = abs(row['count']) * scale_factor
    folium.CircleMarker([row['Latitude'], row['Longitude']], radius=radius, color='red', fill = True, fill_color='red', fill_opacity=0.5, tooltip=row['Address']).add_to(m)
    # folium.Marker([row['Latitude'], row['Longitude']], icon=folium.Icon(color='blue'), tooltip=row['Address']).add_to(m)

# 가축분뇨시설 위치를 지도에 표시
for index, row in data_3.iterrows():
    radius = abs(row['count']) * scale_factor
    folium.CircleMarker([row['Latitude'], row['Longitude']], radius=radius, color='yellow', fill = True, fill_color='yellow', fill_opacity=0.5, tooltip=row['Address']).add_to(m)
    # folium.Marker([row['Latitude'], row['Longitude']], icon=folium.Icon(color='blue'), tooltip=row['Address']).add_to(m)

# 음식물류폐기물처리시설 위치를 지도에 표시
for index, row in data_4.iterrows():
    radius = abs(row['count']) * scale_factor
    folium.CircleMarker([row['Latitude'], row['Longitude']], radius=radius, color='pink', fill = True, fill_color='pink', fill_opacity=0.5, tooltip=row['Address']).add_to(m)
    # folium.Marker([row['Latitude'], row['Longitude']], icon=folium.Icon(color='blue'), tooltip=row['Address']).add_to(m)

# 지도에 거리 측정 컨트롤 추가
m.add_child(MeasureControl())

# HTML 파일로 저장
m.save('C:/Users/CBNU/Desktop/Location_recommendation/경상북도_경주시_지역테두리설정.html')





