import pathlib
import os



#Функция находит файлы в папке, по указанному пути, и всех вложенных в нее папках


def sort_script(user_path):
	

	files = {'immages': {'.jpeg', '.png', '.jpg', '.svg', '.psd'},
			'video': {'.avi', '.mp4', '.mov', '.mkv'},
			'documents': {'.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.xls'},
			'music': {'.mp3', '.ogg', '.wav', '.amr'},
			'books': {'fb2', '.epub'},
			'drawings': {'.dwg', '.dxf'},
			'archives': {'.rar', '.zip'},
			'apps': {'.exe', '.msi'}}

	files_extension = set()

	files_name = []

	files_path = []

	folders_path = []

	is_files = set()

	keys = []

	not_files = set()


	path = pathlib.Path(user_path)
	if path.exists():
		for element in path.rglob('*.*'):
			if element.is_file():
				files_extension.add(element.suffix)
				files_path.append(element)
				files_name.append(element.name)
	else:
		print(f'path {path.absolute()} not exists')


	other_folder_path = path.joinpath(path, 'other')
	other_folder_path.mkdir(exist_ok=True)
	for key, val in files.items():
		if val & files_extension:
			folder_path = path.joinpath(path, key)
			folder_path.mkdir(exist_ok=True)
			folders_path.append(folder_path)
			keys.append(key)


# Переносит файлы в созданные папки в соответствии с их расширением
	for element in path.rglob('*.*'):
		if element.is_file():
			for key, val in files.items():
				if element.suffix in val:
					new_folder_path = path.joinpath(path, key)
					new_file_path = new_folder_path.joinpath(new_folder_path, element.name)
					is_files.add(element.suffix)
					os.replace(element, new_file_path)


	# Переносит файлы с неизвестным расширением в созданную папку Other
	for element in path.rglob('*.*'):
		if element.is_file():
			if element.suffix not in is_files:
				other_folder_path = path.joinpath(path, 'other')
				other_file_path = other_folder_path.joinpath(other_folder_path, element.name)
				not_files.add(element.suffix)
				os.replace(element, other_file_path)
	

	return f'Folders created {keys}', 'Unknown files replased to folder "other"', f'List of all extensions known to the script {is_files}', f'List of all extensions unknown to the script {not_files}', 'left to delete empty folders'
	
	

	


def main():
	user_path = input('Insert path: ')
	print(sort_script(user_path))


if __name__ == '__main__':
	main()










