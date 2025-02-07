from binance.client import Client

# Khởi tạo Binance Client
api_key = "your_api_key"
api_secret = "your_api_secret"
client = Client(api_key, api_secret)

# Tính toán Volume Profile
volume_profile = calculate_volume_profile(client)

# In kết quả
print("Bins (Price Levels):", volume_profile['bins'])
print("Volumes:", volume_profile['volumes'])
print("POC Price:", volume_profile['poc_price'])
