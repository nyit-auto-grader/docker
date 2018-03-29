import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='activity')
subparsers.required = True

grade_parser = subparsers.add_parser('grade')
grade_parser.add_argument('--repo', required=True, type=str, help='repository')
grade_parser.add_argument('--teacher', type=str, dest='teacher.username')
grade_parser.add_argument('--token', type=str, dest='teacher.token')
grade_parser.add_argument('--organization', type=str)

hello_parser = subparsers.add_parser('hello')
hello_parser.add_argument('--message', required=True, type=str)
hello_parser.add_argument('--count', required=True, type=int)
