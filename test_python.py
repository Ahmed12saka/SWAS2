import unittest
import json
import csv
from selenium import webdriver
import time
import pandas as pd

class PerformanceTest(unittest.TestCase):

    def setUp(self):
        # initialize the web driver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_performance(self):
        perf_data_list = []
        for i in range(10):
            # get the performance data
            self.driver.get("https://en.wikipedia.org/wiki/Software_metric")
            perf_data = self.driver.execute_script("return window.performance.getEntries()")
            perf_data_list.append(perf_data)
            time.sleep(1) # wait 1 second before next measurement

        # write the json output to file
        with open("perf_data.json", "w") as f:
            json.dump(perf_data_list, f)

        # calculate the average performance
        average_perf_data = {}
        for entry in perf_data_list[i]:
            sum_duration = 0
            for perf_data in perf_data_list:
                for e in perf_data:
                    if e["name"] == entry["name"]:
                        sum_duration += e["duration"]
            average_perf_data[entry["name"]] = sum_duration / 10

        # write the average data to csv file
        with open("average_perf_data.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "duration"])
            for key, value in average_perf_data.items():
                writer.writerow([key, value])
                
        def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()