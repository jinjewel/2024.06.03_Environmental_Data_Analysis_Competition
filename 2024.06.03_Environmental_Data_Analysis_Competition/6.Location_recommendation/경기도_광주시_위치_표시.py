from shapely.geometry import Point, Polygon
import folium
import pandas as pd
import numpy as np
from folium.plugins import MeasureControl

### 지역을 지도에 표시
# 중심 좌표
center = [37.4352, 127.301]
# 지도 객체 생성
m = folium.Map(location=center, zoom_start=7)


### 경기도 광주시의 경계 좌표 (미완)
gwangju_boundary = [
    [37.5148, 127.2832],
    [37.5078, 127.2974],
    [37.5295, 127.3196],
    [37.5345, 127.3486],
    [37.5315, 127.3601],
    [37.4964, 127.3882],
    [37.4574, 127.386],
    [37.4562, 127.371],
    [37.4465, 127.3769],
    [37.4447, 127.3867],
    [37.4209, 127.3968],
    [37.3857, 127.4231],
    [37.3854, 127.4445], 
    [37.2774, 127.3504],
    [37.266, 127.3013],
    [37.2657, 127.2969],
    [37.2714, 127.2909],
    [37.2692, 127.2795],
    [37.2754, 127.2768],
    [37.2784, 127.2816],
    [37.3454, 127.2813],
    [37.3438, 127.2639],
    [37.3592, 127.2371],
    [37.3543, 127.2181],
    [37.3469, 127.221],
    [37.3297, 127.2004],
    [37.3465, 127.1918],
    [37.3363, 127.1429],
    [37.358, 127.1347],
    [37.3793, 127.1618],
    [37.3873, 127.176],
    [37.3944, 127.1683],
    [37.4633, 127.1819],
    [37.4814, 127.1843],
    [37.4794, 127.218],
    [37.4763, 127.2439],
    [37.4862, 127.2455],
    [37.5091, 127.2535]
]
folium.Polygon(gwangju_boundary, color='blue', fill=True, fill_color='#3186cc').add_to(m)
gwangjin_poly = Polygon(gwangju_boundary)


### 해당 위치를 지도에 표시
# 엑셀 파일 경로
excel_file_path = "C:/Users/CBNU/Desktop/Location_recommendation/경기도_광주시.xlsx"
# 엑셀 파일 불러오기
df_hasu = pd.read_excel(excel_file_path, sheet_name="공공하수처리시설")
# df_jj = pd.read_excel(excel_file_path, sheet_name="찌꺼기처리시설")
df_gachu = pd.read_excel(excel_file_path, sheet_name="가축분뇨시설")
# df_ummsig = pd.read_excel(excel_file_path, sheet_name="음식물류폐기물처리시설")


# DataFrame에서 필요한 컬럼 선택
data_1 = df_hasu[['Address', 'Latitude', 'Longitude', 'count']]
# data_2 = df_jj[['Address', 'Latitude', 'Longitude', 'count']]
data_3 = df_gachu[['Address', 'Latitude', 'Longitude', 'count']]
# data_4 = df_ummsig[['Address', 'Latitude', 'Longitude', 'count']]

# # 데이터의 절대값에 따른 반지름 조정하기 위한 스케일링 팩터 설정
# max_abs_diff = subway_stations['count'].abs().max()
# scale_factor = 3 / max_abs_diff
scale_factor = 17.5


# 공공하수처리시설 위치를 지도에 표시
for index, row in data_1.iterrows():
    radius = abs(row['count']) * scale_factor
    folium.CircleMarker([row['Latitude'], row['Longitude']], radius=radius, color='blue', fill = True, fill_color='blue', fill_opacity=0.5, tooltip=row['Address']).add_to(m)
    # folium.Marker([row['Latitude'], row['Longitude']], icon=folium.Icon(color='blue'), tooltip=row['Address']).add_to(m)

# # 찌꺼기처리시설 위치를 지도에 표시
# for index, row in data_2.iterrows():
#     radius = abs(row['count']) * scale_factor
#     folium.CircleMarker([row['Latitude'], row['Longitude']], radius=radius, color='red', fill = True, fill_color='red', fill_opacity=0.5, tooltip=row['Address']).add_to(m)
#     folium.Marker([row['Latitude'], row['Longitude']], icon=folium.Icon(color='blue'), tooltip=row['Address']).add_to(m)

# 가축분뇨시설 위치를 지도에 표시
for index, row in data_3.iterrows():
    radius = abs(row['count']) * scale_factor
    folium.CircleMarker([row['Latitude'], row['Longitude']], radius=radius, color='yellow', fill = True, fill_color='yellow', fill_opacity=0.5, tooltip=row['Address']).add_to(m)
    # folium.Marker([row['Latitude'], row['Longitude']], icon=folium.Icon(color='blue'), tooltip=row['Address']).add_to(m)

# 음식물류폐기물처리시설 위치를 지도에 표시
# for index, row in data_4.iterrows():
#     radius = abs(row['count']) * scale_factor
#     folium.CircleMarker([row['Latitude'], row['Longitude']], radius=radius, color='pink', fill = True, fill_color='pink', fill_opacity=0.5, tooltip=row['Address']).add_to(m)
#     folium.Marker([row['Latitude'], row['Longitude']], icon=folium.Icon(color='blue'), tooltip=row['Address']).add_to(m)

# 지도에 거리 측정 컨트롤 추가
m.add_child(MeasureControl())


# HTML 파일로 저장
m.save('C:/Users/CBNU/Desktop/Location_recommendation/경기도_광주시_지역테두리설정.html')





