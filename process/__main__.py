import os, sys

sys.path.insert(0, os.getcwd())

if __name__ == '__main__':
    from process.logger import LoggerFactory
    from process.config import build_config
    from process.commands import *
    from process.parser import parser

    config_name = os.environ.get('AUTO_GRADER_CONFIG')
    config = build_config(config_name)
    logger = LoggerFactory.build('process', 'info')
    args = parser.parse_args()
    commands = {'grade': GradeActivity, 'hello': HelloActivity}
    activity = commands.get(args.activity)

    params = config.to_dict()

    for key, value in args.__dict__.items():
        if value:
            parts = key.split('.')
            cursor = params
            for part in parts[:-1]:
                if part in cursor:
                    cursor = cursor[part]
            cursor[parts[-1]] = value

    success = False
    if activity:
        try:
            command = activity(**params)
            command.execute()
            success = True
        except Exception as e:
            logger.exception('main command failed', extra=dict(activity=args.activity))
    else:
        logger.critical('invalid activity', extra=dict(activity=args.activity, expected=list(commands.keys())))

    if success is False:
        sys.exit(1)
