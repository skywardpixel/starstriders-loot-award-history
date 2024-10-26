map( . += { itemName: (.itemLink | ltrimstr("[") | rtrimstr("]") ) }
  | { item: .itemName, winner: (.awardedTo | split("-") | .[0]), os: .OS, timestamp: .timestamp } )
#  | (map(keys) | add | unique) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv
