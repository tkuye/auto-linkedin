#!/bin/sh

python3 -m src.recruiter connect \
--leads data/recruiter/leads/saf_waterloo_2025_2026.json \
--identity identities/zoe \
--max_connections 70 \
--message data/messages/business_development.txt \
--send_delay_min 60 \
--send_delay_max 120 \
--person Zoe \
--connect_file data/recruiter/connections/saf_waterloo_2025_2026.csv