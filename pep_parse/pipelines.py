import csv
from datetime import datetime as dt

from scrapy.exceptions import DropItem

from constants import BASE_DIR, DT_FORMAT

class PepParsePipeline:

    def open_spider(self, spider):
        self.status = {}
        self.total: int = 0

    def process_item(self, item, spider):
        try:
            if "status" not in item:
                raise DropItem
        except DropItem:
            print("Не полные данные: нет ключа 'status'")
        else:
            key = item["status"]
            self.status[key] = self.status.get(key, 0) + 1
            self.total += 1
        finally:
            return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / "results"
        results_dir.mkdir(exist_ok=True)
        now_time = dt.now().strftime(DT_FORMAT)
        file_name = results_dir / f"status_summary_{now_time}.csv"
        with open(file_name, mode="w", encoding="utf-8") as file:
            fieldnames = ("Статус", "Колличество")
            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames,
                dialect="unix"
            )
            writer.writeheader()
            for key in self.status:
                writer.writerow(
                    {
                        "Статус": key,
                        "Колличество": self.status[key]
                    }
                )
            writer.writerow(
                {
                    "Статус": "Total",
                    "Колличество": self.total
                }
            )