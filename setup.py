from setuptools import setup

setup(
   name='History data downloader from yahoo finance, finam and binance',
   version='0.1',
   description='Download history data from https://finance.yahoo.com, https://www.finam.ru and https://www.binance.com and save to dataframe or csv file',
   author='Zenoftrading',
   url='https://github.com/zenoftrading/barloader',
   packages=['barloader'],
   install_requires=['pandas', 'tqdm', 'python-binance', 'dotmap', 'finam-export', 'loguru', 'yfinance'],
)