# kr-stock-parser

Parses Korean stock data and draws a graph.  
> 한국의 주식 데이터를 파싱하고, 그래프를 그려줍니다.  

## Background

- Parses stock codes from [KIND공시 - 한국거래소](http://kind.krx.co.kr/)  
- Parses stock data from [NAVER Finance - 네이버](http://finance.naver.com)  

## Install  
`$ git clone https://github.com/PJunhyuk/kr-stock-parser.git`

#### Dependencies

- pandas  
- lxml  
- BeautifulSoup4  
- matplotlib (for visualizer)

## Usage  
`$ python get_stock.py`

> You have to change custom font routes to use visualizer. (It's in [functions.py](https://github.com/PJunhyuk/kr-stock-parser/blob/master/functions.py))  

#### Arguments

`-n`, `--stockName`: Name of Stock (default: 카카오)  
`-v`, `--visualize`: Visualizer on/off  

#### Example

`$ python get_stock.py -n "카카오" -v 1`

## References

[5. Pandas를 이용한 Naver금융에서 주식데이터 가져오기](http://excelsior-cjh.tistory.com/109)  
