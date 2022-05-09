import pandas as pd

BULK_THRESHOLD = 100
PRICE_THRESHOLD = 1000

def calculate_AOV(df:pd.DataFrame) -> float:
  bulk_filter = df['total_items'] < BULK_THRESHOLD
  price_filter = (df['order_amount'] / df['total_items']) < PRICE_THRESHOLD
  return df['order_amount'].loc[bulk_filter & price_filter].mean()

def calculate_bulk_sale_AOV(df:pd.DataFrame) -> dict:
  bulk_sales_dict = {}
  for shop in df['shop_id'].loc[df['total_items'] > BULK_THRESHOLD]:
      shop_record = {}
      shop_bulk_sales = df.loc[(df['shop_id'] == shop) & (df['total_items']> BULK_THRESHOLD)]
      shop_record['n_orders'] = len(shop_bulk_sales)
      shop_record['AOV'] = shop_bulk_sales['order_amount'].mean()
      bulk_sales_dict[shop] = shop_record
  return bulk_sales_dict

def identify_price_outliers(df:pd.DataFrame) -> dict:
  item_prices = (df['order_amount'] / df['total_items'])
  item_prices.name = 'item_price'
  price_df = pd.concat([df['shop_id'],item_prices],axis=1).groupby('shop_id').mean()
  return price_df[price_df['item_price'] > 1000]['item_price'].to_dict()
    

if __name__ == '__main__':
  df = pd.read_csv('2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv') 
  aov = calculate_AOV(df)
  bulk = calculate_bulk_sale_AOV(df)
  price_outliers = identify_price_outliers(df)
  print(f"The average AOV for typical sneeker stores is: {'${:,.2f}'.format(aov)}")
  if (len(bulk) > 0) or (len(price_outliers) > 0):
    print('\nNotable outliers not included in this calculation are:\n')
    for shop, record in bulk.items():
      print(f"Shop #{shop} had {record['n_orders']} bulk orders which alone had an AOV of {'${:,.2f}'.format(record['AOV'])}")
    for shop, price in price_outliers.items():
      print(f"Shop #{shop} is selling it's items for {'${:,.2f}'.format(price)} each, which is above the threshold to be considered a typical sneaker store or the result of an error.")