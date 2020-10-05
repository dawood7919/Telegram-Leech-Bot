from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "866564625:AAH6FVxV-T6PNhRR6v3bcpU-k_jHo10Zh9I"
	APP_ID = 1195139
	API_HASH = "8b5ead996db2f3fda8f14fedc3d4ca77"
	OWNER_ID = "1096429310" #ID of bot owner
	AUTH_CHANNEL = [-1001227047259]
	DESTINATION_FOLDER = "HelloMan" #Name of your folder read readme
	RCLONE_CONFIG = """type = dropbox\ntoken = {"access_token":"89t6gGUgqiAAAAAAAAAv1fleE4b6VVmNIvaLhqGoPbpo9-5_nHMX6to3jr8BXTvY","token_type":"bearer","expiry":"0001-01-01T00:00:00Z"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
