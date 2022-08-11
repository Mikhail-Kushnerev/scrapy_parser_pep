import csv
import logging
from datetime import datetime as dt

from scrapy.exceptions import DropItem

from constants import BASE_DIR, DT_FORMAT


class PepParsePipeline:

    def open_spider(self, spider):
        self.status = {}

    def process_item(self, item, spider):
        try:
            if "status" not in item:
                raise DropItem
        except DropItem:
            logging.error("Не полные данные: нет ключа 'status'")
        else:
            key = item["status"]
            self.status[key] = self.status.get(key, 0) + 1
        finally:
            return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / "results"
        results_dir.mkdir(exist_ok=True)
        now_time = dt.now().strftime(DT_FORMAT)
        file_name = results_dir / f"status_summary_{now_time}.csv"
        with open(file_name, mode="w", encoding="utf-8") as file:
            writer = csv.writer(
                file,
                dialect="unix",
                delimiter=";"
            )
            writer.writerows(
                (
                    ("Статус", "Колличество"),
                    *self.status.items(),
                    ("Total", sum(self.status.values()))
                )
            )
