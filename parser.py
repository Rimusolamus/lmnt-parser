#! /usr/bin/env python3
import sys

WILDCARD = "*"
ZEROES = "00"


def main():
    input_time = get_input_time()
    if sys.stdin is None:
        print("Failed to parse config line")
        quit()
    has_one_line = False
    for line in [line for line in sys.stdin]:
        has_one_line = True
        params = prepare_config(line)
        process_param_line(params, input_time)
    if not has_one_line:
        print("Config file is blank")


# check input time format
def get_input_time():
    if len(sys.argv) == 2:
        # argv[0] - script name, argv[1] - first argument
        input_time = sys.argv[1]
    else:
        print("Provide current time as argument to this script as HH:MM")
        quit()

    # check if given time is good
    input_time = input_time.split(":")
    if len(input_time) != 2:
        print("Input time isn't in format HH:MM: given " + str(input_time))
        quit()
    if input_time[0].isdigit() and input_time[0].isdigit():
        pass
    else:
        print("Failed to parse input date: " + str(input_time))
        quit()
    return input_time


# Check if config params are good
# Only 3 params are supported like
# For example: * * /task
def prepare_config(params):
    params = params.split(" ")
    if len(params) == 3:
        if params[0] != WILDCARD:
            if is_valid_minutes_value(params[0]):
                pass
            else:
                print("Failed to parse config: given minutes are incorrect " + str(params))
                quit()
        if params[1] != WILDCARD:
            if is_valid_hour_value(params[1]):
                pass
            else:
                print("Failed to parse config: given hours are incorrect " + str(params))
                quit()
    else:
        print("Failed to parse config line: given number of params is " + str(len(params)) + " " + str(params))
        quit()
    return params


def is_valid_minutes_value(minute):
    if int(minute) in range(0, 60):
        return True
    else:
        return False


def is_valid_hour_value(hour):
    if int(hour) in range(0, 24):
        return True
    else:
        return False


def process_param_line(params, input_time):
    if is_valid_hour_value(input_time[0]) and is_valid_minutes_value(input_time[1]):
        config_hours = params[1]
        config_minutes = params[0]
        config_task = params[2]

        input_hours = input_time[0]
        input_minutes = input_time[1]

        # run_me_every_minute
        if (config_minutes == WILDCARD) and (config_hours == WILDCARD):
            print_result(input_hours, input_minutes, True, config_task)
        # run_me_sixty_times
        elif (config_minutes == WILDCARD) and (config_hours != WILDCARD):
            fixed_hours_task(config_hours, input_hours, config_task)
        # run_me_hourly
        elif (config_minutes != WILDCARD) and (config_hours == WILDCARD):
            fixed_minutes_task(config_minutes, input_hours, input_minutes, config_task)
        # run_me_daily
        else:
            fixed_hours_and_minuts_task(config_hours, config_minutes, input_hours, input_minutes, config_task)
    else:
        print("Input time isn't in format: HH:MM: given " + str(input_time))
        quit()


def fixed_hours_task(config_hours, input_hours, config_task):
    if int(config_hours) > int(input_hours):
        print_result(config_hours, ZEROES, True, config_task)
    else:
        print_result(config_hours, ZEROES, False, config_task)


def fixed_minutes_task(config_minutes, input_hours, input_minutes, config_task):
    if int(config_minutes) >= int(input_minutes):
        print_result(input_hours, config_minutes, True, config_task)
    else:
        # next day
        if int(input_hours) == 23:
            print_result(ZEROES, config_minutes, False, config_task)
        else:
            print_result(str((int(input_hours) + 1)), config_minutes, True, config_task)


def fixed_hours_and_minuts_task(config_hours, config_minutes, input_hours, input_minutes, config_task):
    if int(config_hours) < int(input_hours):
        print_result(config_hours, config_minutes, False, config_task)
    else:
        if int(config_minutes) < int(input_minutes):
            print_result(config_hours, config_minutes, False, config_task)
        else:
            print_result(config_hours, config_minutes, True, config_task)


def print_result(hours, minutes, is_today, task_name):
    if is_today:
        print(hours + ":" + minutes + " today - " + task_name)
    else:
        print(hours + ":" + minutes + " tomorrow - " + task_name)


if __name__ == '__main__':
    main()
