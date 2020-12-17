#!/usr/bin/env python3


"""
Program that installs the Django templates in the correct folders.
Works only for Linux
"""

import os
import sys


def install_prompt():
    print("")
    print("""
     ______                        __                __  __              __      __
    /      |                      /  |              /  |/  |            /  |    /  |
    $$$$$$/  _______    _______  _$$ |_     ______  $$ |$$ |  ______   _$$ |_   $$/   ______   _______
      $$ |  /       \\  /       |/ $$   |   /      \\ $$ |$$ | /      \\ / $$   |  /  | /      \ /       \\
      $$ |  $$$$$$$  |/$$$$$$$/ $$$$$$/    $$$$$$  |$$ |$$ | $$$$$$  |$$$$$$/   $$ |/$$$$$$  |$$$$$$$  |
      $$ |  $$ |  $$ |$$      \\   $$ | __  /    $$ |$$ |$$ | /    $$ |  $$ | __ $$ |$$ |  $$ |$$ |  $$ |
     _$$ |_ $$ |  $$ | $$$$$$  |  $$ |/  |/$$$$$$$ |$$ |$$ |/$$$$$$$ |  $$ |/  |$$ |$$ \\__$$ |$$ |  $$ |
    / $$   |$$ |  $$ |/     $$/   $$  $$/ $$    $$ |$$ |$$ |$$    $$ |  $$  $$/ $$ |$$    $$/ $$ |  $$ |
    $$$$$$/ $$/   $$/ $$$$$$$/     $$$$/   $$$$$$$/ $$/ $$/  $$$$$$$/    $$$$/  $$/  $$$$$$/  $$/   $$/

    """)

    print("")


def get_index_ide():
    print("")
    IDE_folder = int(input("Select the number of a folder >> "))
    return IDE_folder


def os_operations():
    start_directory = os.getcwd()
    # print(start_directory)
    # Changes directory

    home = os.path.expanduser("~")

    # Defines JetBrains products config
    jetbrains_config = f"{home}/.config/JetBrains/"

    # Defines if the JetBrains directory exists.
    # It only works for linux
    if not os.path.exists(jetbrains_config):
        print("""You don't have any jetbrains IDE installed,
        or your OS is not supported""")
        print("Copy Django.xml manually")
        sys.exit()

    os.chdir(jetbrains_config)
    config_list = os.listdir()

    for index, directory in enumerate(config_list):
        print(f"[{str(index)}] {directory}")

    try:
        ide_index = get_index_ide()
        print(f"Selected folder: {config_list[ide_index]}")
    except IndexError:
        raise Exception("You selected an uncorrect folder")

    try:
        os.chdir(config_list[ide_index] + "/" + "templates")
        last_directory = os.getcwd()
        copy_comand = f"cp {start_directory}/Django.xml {last_directory}"
        os.system(copy_comand)

        print("Program finished succesfully")

    except FileNotFoundError:
        raise Exception("Templates folder doesn't exist")


def main():
    install_prompt()
    os_operations()


if __name__ == "__main__":
    main()
