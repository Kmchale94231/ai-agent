from functions.get_files_info import get_files_info


def _print_section(call_desc, header, working_directory, directory):
    print(call_desc)
    print(header)
    try:
        result = get_files_info(working_directory, directory)
        if not result:
            print("  (empty)")
        else:
            for line in result.splitlines():
                print(f"  {line}")
    except ValueError as exc:
        print(f"    {exc}")


def main():
    _print_section('get_files_info("calculator", "."):', 'Result for current directory:', 'calculator', '.')
    print()
    _print_section('get_files_info("calculator", "pkg"):', "Result for 'pkg' directory:", 'calculator', 'pkg')
    print()
    _print_section('get_files_info("calculator", "/bin"):', "Result for '/bin' directory:", 'calculator', '/bin')
    print()
    _print_section('get_files_info("calculator", "../"):', "Result for '../' directory:", 'calculator', '../')


if __name__ == '__main__':
    main()

