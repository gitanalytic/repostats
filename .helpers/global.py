def get_email_data_from_file():
	emailinformation = None
	with open('/Users/Paul/TestDeveloper/emailinformation.txt', 'r+') as textfile:
		lines = textfile.readlines()
		
		# Get relevant information and store in dictionary
		filename = lines[0]
		filename = filename[:-1]
		text = lines[1]
		emailinformation = {IMAGE_FILE_NAME: filename, MESSAGE_BODY: text}

		# Write back to file, but get rid the lastest email
		lines = lines[2:]
		textfile.seek(0)
		for line in lines:
			textfile.write(line)
		textfile.truncate()

	return emailinformation;