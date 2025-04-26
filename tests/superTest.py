import requests

BASE_URL = "http://127.0.0.1:8000"  # Базовый URL сервера
LOGIN_ENDPOINT = "/auth/login"  # Эндпоинт для авторизации
PRODUCT_CREATE_ENDPOINT = "/products/create"  # Эндпоинт для создания продукта

# Данные для входа
login_data = {
    "email": "user@example.com",
    "password": "string"
}

# Продукты для добавления
products = [
  {
    "name": "Pineapple",
    "price": 25,
    "quantity": 30,
    "ingredients": "Pineapple",
    "nutrition": "74cal",
    "description": "Exotic and refreshing taste",
    "stars": 4,
    "image_id": 7
  },
  {
    "name": "Mango",
    "price": 30,
    "quantity": 30,
    "ingredients": "Mango",
    "nutrition": "60cal",
    "description": "Tropical sweetness",
    "stars": 5,
    "image_id": 8
  },
  {
    "name": "Kiwi",
    "price": 22,
    "quantity": 30,
    "ingredients": "Kiwi",
    "nutrition": "42cal",
    "description": "Packed with vitamin C and fiber",
    "stars": 4,
    "image_id": 9
  }
]

def login_and_get_token():
    url = BASE_URL + LOGIN_ENDPOINT
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=login_data, headers=headers)
        response.raise_for_status()  # Проверка на успешный запрос
        
     
        print("Full response text:", response.text)  # Это покажет весь ответ сервера

        try:
            data = response.json()  
            print("Response JSON:", data) 
            token = data.get("access_token")
            if not token:
                print(f"JWT token not found in response: {data}")
                return None
            return token
        except ValueError:
            print(f"Response is not a valid JSON: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")
    return None

def add_product(token, product):
    if not token:
        print("JWT token is empty!")
        return None
    
    url = BASE_URL + PRODUCT_CREATE_ENDPOINT
    headers = {
        "Content-Type": "application/json"
    }
    
    cookies = {
        "login_access_token": token #Передаем JWT токен через куки
    }

    response = requests.post(url, json=product, headers=headers, cookies=cookies)

    return response

if __name__ == "__main__":
    token = login_and_get_token()
    if not token:
        print("Login failed. Exiting.")
    else:
        print("Login successful. Token obtained.")
        
        # Добавляем продукты
        for product in products:
            response = add_product(token, product)
            if response and response.status_code == 200:
                print(f"Product added successfully: {product['name']}")
            else:
                error_message = response.text if response else "No response received"
                print(f"Failed to add product: {product['name']}. Error: {error_message}")
