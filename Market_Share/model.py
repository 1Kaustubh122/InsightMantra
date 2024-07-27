from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import json

def get_amazon_product_details(product_name):
    # Specify the path to the Edge WebDriver executable
    edge_driver_path = r"C:\Users\Satyam\Downloads\edgedriver_win64\msedgedriver.exe" 

    options = webdriver.EdgeOptions()
    options.add_argument("--headless")  
    driver = webdriver.Edge(service=Service(edge_driver_path), options=options)
    
    # URL
    amazon_search_url = f"https://www.amazon.com/s?k={'+'.join(product_name.split())}"
    # indiamart_search_url = f""
    
    # open the URL
    driver.get(amazon_search_url)
    time.sleep(3)  # Wait for the page to load

    # product listing
    products = driver.find_elements(By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')

    product_details = []

    for product in products:
        try:
            title = product.find_element(By.TAG_NAME, 'h2').text.strip()
            # seller = product.find_element(By.CSS_SELECTOR, 'span.a-size-base-plus.a-color-base.a-text-normal').text.strip()
            # rating = product.find_element(By.CSS_SELECTOR, 'span.a-size-base s-underline-text').text.strip()
            # reviews = product.find_element(By.CSS_SELECTOR, 'span.a-size-base').text.strip()
            quantity_sold = product.find_element(By.CSS_SELECTOR, 'span.a-size-base.s-underline-text').text.strip()

            product_details.append({
                'title': title,
                # 'seller': seller,
                # 'rating': rating,
                'quantity_sold': quantity_sold,
            })
        except Exception as e:
            print(f"Error extracting product details: {e}")
            continue

    driver.quit()
    return product_details
product_name = "condoms"
amazon_search_url = f"https://www.amazon.com/s?k={'+'.join(product_name.split())}"
product_info = get_amazon_product_details(product_name)

company = []
for product in product_info:

    company_name = (product['title'].split())[:1]
    if(company_name not in company): 
        company.append({company_name[0] : product['quantity_sold']}) 
    

def consolidate_data(data):
  """Consolidates data by summing values for duplicate keys."""
  result = {}
  for d in data:
    key, value = list(d.items())[0]
    value = int(value.replace(',', ''))  # Remove commas and convert to int
    result[key] = result.get(key, 0) + value  # Add or create key with cumulative sum
  return result

cons_company = consolidate_data(company)

def calculate_ratios(data_dict):
  """Calculates ratios for each company based on the total sum."""
  total_value = sum(data_dict.values())
  ratios = {key: value / total_value for key, value in data_dict.items()}
  return ratios

ratios = calculate_ratios(cons_company)

json_dir = r"C:\Users\Satyam\Desktop\FOSSHACK\Amazon_Web_Scapping\scrapped.json"

with open(json_dir , 'w') as f:
   json.dump(ratios , f)