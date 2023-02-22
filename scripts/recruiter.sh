

python3 -m src.recruiter connect \
	--identity ../identities/alex \ ## change this to the identity you want to use
	--max_connections 70 \
	--message ../data/messages/business_development.txt \
	--send_delay_min 90 \
	--send_delay_max 120 \
	--person Alex \
	--leads ../data/recruiter/leads/haskayne_2025_2026.json \ ## change this to the leads file you want to connect with
	--connect_file ../data/recruiter/connections/haskayne_2025_2026.csv ## change this to the connections file you want to save to