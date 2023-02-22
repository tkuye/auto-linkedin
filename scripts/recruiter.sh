#!/bin/sh

python3 -m src.recruiter connect \
--leads data/recruiter/leads/haskayne_2025_2026.json \
--identity identities/alex \
--max_connections 70 \
--message data/messages/business_development.txt \
--send_delay_min 90 \
--send_delay_max 120 \
--person Alex \
--connect_file data/recruiter/connections/haskayne_2025_2026.csv