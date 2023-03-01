import os

from .utils import *
from .config import Config

__all__ = [
    "mac_install_zsh",
    "mac_install_homebrew",
    "mac_install_homebrew_brewfile",
]


def check_is_mac(func):
    def wrapper(*args, **kwargs):
        if Config.os_type == "DARWIN":
            return func(*args, **kwargs)

    return wrapper


@check_is_mac
def mac_install_zsh():
    if not is_executable_exists("zsh"):
        print("WARNING!!! MacOS should always has zsh installed.")
    else:
        print("Zsh already installed.")


@check_is_mac
def mac_install_homebrew():
    if not is_executable_exists("brew"):
        confirm_then_execute_shell_command(
            "Do you want to install homebrew?",
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
        )
    else:
        print("Homebrew already installed.")


@check_is_mac
def mac_install_homebrew_brewfile():
    if not is_executable_exists("brew"):
        print("Need homebrew, do nothing")
        return

    confirm_then_execute_shell_command(
        "Do you want to install everything in brewfile?",
        "brew bundle install --file={}".format(
            os.path.join(Config.dotfiles_dir, "mackup/.Brewfile")
        ),
    )
