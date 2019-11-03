### Acquisition
  - [Acquisition Site]
  - [Preprocessing Code]
  
#### Acquisition Site
  1. Chicken/Pizza/Chinese-food data were searched from
  ```
  https://www.bigdatahub.co.kr/product/list.do?menu_id=1000150
  ```
  2. Populations of each Gu were searched from
  ```
  http://data.seoul.go.kr/together/statbook/statbookList.do?tr_code=short#submenu1
  ```
  3. Store Informations were searched from
  ```
  https://www.data.go.kr/dataset/15012005/fileData.do
  ```
  
#### Preprocessing Code

transform.py

>Merge monthly information(chicken/pizza/chinese-food data) into yearly information.

>Convert encoding type of data from cp949 to utf-8
