@echo off

python3 "-m" "src.recruiter" "connect" "--leads" "data\recruiter\leads\saf_waterloo_2025_2026.json" "--identity" "identities\tosin" "--max_connections" "50" "--message" "data\messages\business_development.txt" "--send_delay_min" "60" "--send_delay_max" "120" "--person" "Tosin" "--connect_file" "data\recruiter\connections\saf_waterloo_2025_2026.csv"