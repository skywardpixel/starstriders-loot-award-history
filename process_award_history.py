from dataclasses import dataclass
import json
import sys
import csv

@dataclass
class AwardEntry:
  winner: str
  item_id: int
  item_link: str
  timestamp: int
  is_off_spec: bool
  is_soft_res: bool
  master_looter: str

def remove_realm(name):
  return name.split('-')[0]

def main():
  if len(sys.argv) < 2:
    print("Usage: python process_award_history.py <award_history_file1> <award_history_file2> ...")
    sys.exit(1)

  entries = []
  for file in sys.argv[1:]:
    with open(file, 'r') as f:
      data = json.load(f)
      for entry in data:
        entry = AwardEntry(item_id=entry['itemID'],
                           item_link=entry['itemLink'],
                           timestamp=entry['timestamp'],
                           winner=remove_realm(entry['awardedTo']),
                           is_off_spec=entry['OS'],
                           is_soft_res=entry['SR'],
                           master_looter=remove_realm(entry['awardedBy']))
        entries.append(entry)
  entries.sort(key=lambda x: x.winner)
  csv.DictWriter(sys.stdout, fieldnames=entries[0].__dict__.keys()).writeheader()
  for entry in entries:
    csv.DictWriter(sys.stdout, fieldnames=entry.__dict__.keys()).writerow(entry.__dict__)

if __name__ == "__main__":
  main()
