from data_fetcher import DataFetcher
from data_processor import DataProcessor
from visualizer import Visualizer
from logger import Logger

import requests

def main():
    API_KEY = ''  # openweathermap API 키 입력
    city = input("Which City? ")

    fetcher = DataFetcher(API_KEY, city)
    processor = DataProcessor()
    visualizer = Visualizer()
    logger = Logger()

    raw_data = fetcher.fetch_weather()
    processed_data = processor.process_data(raw_data)
    logger.save_data(processed_data)
    visualizer.plot_data(processed_data)

if __name__ == "__main__":
    main()
