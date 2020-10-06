from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "866564625:AAH6FVxV-T6PNhRR6v3bcpU-k_jHo10Zh9I"
	APP_ID = 1195139
	API_HASH = "8b5ead996db2f3fda8f14fedc3d4ca77"
	OWNER_ID = 1096429310 #ID of bot owner
	AUTH_CHANNEL = [-1001227047259]
	DESTINATION_FOLDER = "Bot" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMBQjJNyELdYheSB_h-Pe-9Y5zUGIXgZhpqY1oGjlsToggcMH-5lzl-II9kfeWzrgcxSwDgN7cdxSKRaaMnGXLNngxfvSxW-TCFAmpuflt2RB5ryC4iAm0bzZkvbOLk1uJxvuLyA9dIlh5o5Kk9C9JUn-vTwz50","token_type":"Bearer","refresh_token":"1//05L1bq9YFZJeTCgYIARAAGAUSNgF-L9Ir87mwvnL81PWZ91JcQej-Sjd8Ojp7SOONQOeriRkhciLgAf_5n22YtOTLDvDXZMaYMw","expiry":"2020-10-05T23:06:32.352941022+07:00"}\nteam_drive = 0ALmAQbPSBT0rUk9PVA\nroot_folder_id = 1FstTvibvJB559SRCcAkzLyczerkG70CZ"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
