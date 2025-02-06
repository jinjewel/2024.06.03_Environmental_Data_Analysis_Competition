from shapely.geometry import Point, Polygon
import folium
import pandas as pd
import numpy as np
from folium.plugins import MeasureControl

### 지역을 지도에 표시
# 중심 좌표
center = [37.2804, 127.0079]

# 지도 객체 생성
m = folium.Map(location=center, zoom_start=7)

### 경기도 수원시의 경계 좌표 (2024 기준)
# Suwon_boundary = [
#     [37.3032, 126.9631],
#     [37.301, 126.9519],
#     [37.3031, 126.9337],
#     [37.3009, 126.9319],
#     [37.2983, 126.9361],
#     [37.2959, 126.9405],
#     [37.2948, 126.941],
#     [37.2925, 126.9354],
#     [37.2872, 126.9293],
#     [37.2784, 126.9277],
#     [37.2764, 126.9283],
#     [37.2712, 126.927],
#     [37.2704, 126.9293],
#     [37.2609, 126.9307],
#     [37.257, 126.9355],
#     [37.2574, 126.9468],
#     [37.2402, 126.9578],
#     [37.235, 126.9677],
#     [37.2297, 126.9699],
#     [37.2335, 126.9878],
#     [37.2289, 126.9976],
#     [37.2272, 126.9973],
#     [37.2265, 127.0006],
#     [37.2289, 127.0028],
#     [37.2244, 127.0219],
#     [37.2385, 127.0376],
#     [37.2388, 127.0436],
#     [37.233, 127.0465],
#     [37.2344, 127.0507],
#     [37.2326, 127.0538],
#     [37.2317, 127.0526],
#     [37.2363, 127.0603],
#     [37.246, 127.069],
#     [37.2475, 127.0795],
#     [37.2503, 127.0819],
#     [37.2532, 127.0808],
#     [37.2548, 127.0824],
#     [37.2562, 127.0816],
#     [37.2566, 127.08],
#     [37.2597, 127.0795],
#     [37.2614, 127.0811],
#     [37.2625, 127.0845],
#     [37.2649, 127.0863],
#     [37.2699, 127.0848],
#     [37.267, 127.0773],
#     [37.2657, 127.0775],
#     [37.2667, 127.07],
#     [37.2687, 127.0684],
#     [37.2693, 127.0643],
#     [37.2808, 127.0735],
#     [37.286, 127.0912],
#     [37.3014, 127.0911],
#     [37.3037, 127.0863],
#     [37.2956, 127.0801],
#     [37.2934, 127.0794],
#     [37.2968, 127.0597],
#     [37.3152, 127.0574],
#     [37.3168, 127.0496],
#     [37.3207, 127.045],
#     [37.3469, 127.0282],
#     [37.3559, 127.0157],
#     [37.3462, 127.0133],
#     [37.3268, 126.9816],
#     [37.3319, 126.9712],
#     [37.3246, 126.9678],
#     [37.322, 126.9704],
#     [37.3079, 126.9665],
#     [37.3032, 126.9631]
# ]
Suwon_boundary = [
    [37.3032, 126.9631],
    [37.301, 126.9519],
    [37.3031, 126.9337],
    [37.3009, 126.9319],
    [37.2983, 126.9361],
    [37.2959, 126.9405],
    [37.2948, 126.941],
    [37.2925, 126.9354],
    [37.2872, 126.9293],
    [37.2784, 126.9277],
    [37.2764, 126.9283],
    [37.2712, 126.927],
    [37.2704, 126.9293],
    [37.2609, 126.9307],
    [37.257, 126.9355],
    [37.2574, 126.9468],
    [37.2402, 126.9578],
    [37.235, 126.9677],
    [37.2297, 126.9699],
    [37.2335, 126.9878],
    [37.2289, 126.9976],
    [37.2272, 126.9973],
    [37.2265, 127.0006],
    [37.2154, 127.0033],
    [37.2093, 127.0142],
    [37.2065, 127.0234],
    [37.2181, 127.033],
    [37.2344, 127.0507],
    [37.2326, 127.0538],
    [37.2317, 127.0526],
    [37.2363, 127.0603],
    [37.246, 127.069],
    [37.2475, 127.0795],
    [37.2503, 127.0819],
    [37.2532, 127.0808],
    [37.2548, 127.0824],
    [37.2562, 127.0816],
    [37.2566, 127.08],
    [37.2597, 127.0795],
    [37.2614, 127.0811],
    [37.2625, 127.0845],
    [37.2649, 127.0863],
    [37.2699, 127.0848],
    [37.267, 127.0773],
    [37.2657, 127.0775],
    [37.2667, 127.07],
    [37.2687, 127.0684],
    [37.2693, 127.0643],
    [37.2808, 127.0735],
    [37.286, 127.0912],
    [37.3014, 127.0911],
    [37.3037, 127.0863],
    [37.2956, 127.0801],
    [37.2934, 127.0794],
    [37.2968, 127.0597],
    [37.3152, 127.0574],
    [37.3168, 127.0496],
    [37.3207, 127.045],
    [37.3469, 127.0282],
    [37.3559, 127.0157],
    [37.3462, 127.0133],
    [37.3268, 126.9816],
    [37.3319, 126.9712],
    [37.3246, 126.9678],
    [37.322, 126.9704],
    [37.3079, 126.9665],
    [37.3032, 126.9631]
]

folium.Polygon(Suwon_boundary, color='blue', fill=True, fill_color='#3186cc').add_to(m)
gwangjin_poly = Polygon(Suwon_boundary)


### 해당 위치를 지도에 표시
# 엑셀 파일 경로
excel_file_path = "C:/Users/CBNU/Desktop/Location_recommendation/경기도_수원시.xlsx"

# 엑셀 파일 불러오기
df_hasu = pd.read_excel(excel_file_path, sheet_name="공공하수처리시설")
df_jj = pd.read_excel(excel_file_path, sheet_name="찌꺼기처리시설")
# df_gachu = pd.read_excel(excel_file_path, sheet_name="가축분뇨시설")
df_ummsig = pd.read_excel(excel_file_path, sheet_name="음식물류폐기물처리시설")


# DataFrame에서 필요한 컬럼 선택
data_1 = df_hasu[['Address', 'Latitude', 'Longitude', 'count']]
data_2 = df_jj[['Address', 'Latitude', 'Longitude', 'count']]
# data_3 = df_gachu[['Address', 'Latitude', 'Longitude', 'count']]
data_4 = df_ummsig[['Address', 'Latitude', 'Longitude', 'count']]

# 데이터의 절대값에 따른 반지름 조정하기 위한 스케일링 팩터 설정
# scale_factor = 68
scale_factor = 37

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

# # 가축분뇨시설 위치를 지도에 표시
# for index, row in data_3.iterrows():
#     radius = abs(row['count']) * scale_factor
#     folium.CircleMarker([row['Latitude'], row['Longitude']], radius=radius, color='yellow', fill = True, fill_color='yellow', fill_opacity=0.5, tooltip=row['Address']).add_to(m)
#     folium.Marker([row['Latitude'], row['Longitude']], icon=folium.Icon(color='blue'), tooltip=row['Address']).add_to(m)

# 음식물류폐기물처리시설 위치를 지도에 표시
for index, row in data_4.iterrows():
    radius = abs(row['count']) * scale_factor
    folium.CircleMarker([row['Latitude'], row['Longitude']], radius=radius, color='pink', fill = True, fill_color='pink', fill_opacity=0.5, tooltip=row['Address']).add_to(m)
    # folium.Marker([row['Latitude'], row['Longitude']], icon=folium.Icon(color='blue'), tooltip=row['Address']).add_to(m)

# 지도에 거리 측정 컨트롤 추가
m.add_child(MeasureControl())

# HTML 파일로 저장
m.save('C:/Users/CBNU/Desktop/Location_recommendation/경기도_수원시_지역테두리설정.html')





