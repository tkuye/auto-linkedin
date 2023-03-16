@echo off

python3 "-m" "src.sales" "connect" "--leads" "data\sales\leads\leads_ranked.json" "--identity" "data\identities\matt" "--message" "data\sales\message\sales.txt" "--connect_file" "data\sales\connections\connections.csv" "--max_connections" "40" "--send_delay_min" "60" "--send_delay_max" "120"