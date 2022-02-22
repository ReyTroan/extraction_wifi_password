import subprocess

def extract_wifi_passwords():
	profiles_data = subprocess.check_output('netsh wlan show profiles')

	profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]
	# print(profiles)

	for profile in profiles():
		profile_info = subprocess.check_output(f'netsh wlan show profiles {profile} key=clear').decode('utf-8').split('\n')
		# print(profile_info)

		password = [i.split(':')[1].strip() for i in profile_info if 'key content' in i]
		print(password)