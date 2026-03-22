from functions.get_file_content import get_file_content

# Тест на усечение
print("Testing lorem.txt truncation:")
result = get_file_content("calculator", "lorem.txt")
print(f"  Length: {len(result)} characters")
print(f"  End of content: ...{result[-80:]}")

print()
print("get_file_content('calculator', 'main.py'):")
print(get_file_content("calculator", "main.py"))

print()
print("get_file_content('calculator', 'pkg/calculator.py'):")
print(get_file_content("calculator", "pkg/calculator.py"))

print()
print("get_file_content('calculator', '/bin/cat'):")
print(get_file_content("calculator", "/bin/cat"))

print()
print("get_file_content('calculator', 'pkg/does_not_exist.py'):")
print(get_file_content("calculator", "pkg/does_not_exist.py"))