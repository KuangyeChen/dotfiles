from abc import ABC, abstractmethod

from .utils import *


__all__ = [
    "Rye",
    "HomeBrew",
    "Starship",
    "Fish",
    "Rust",
    "RustApps",
    "Fisher",
    "FishPlugins",
]


class Package(ABC):
    def __init__(self, config):
        self.config = config

    @staticmethod
    @abstractmethod
    def name():
        pass

    @abstractmethod
    def run(self):
        pass


class Rye(Package):
    def __init__(self, config):
        super().__init__(config)

    @staticmethod
    def name():
        return "rye"

    @check_executable_exists("rye")
    def run(self):
        if self.config.os_type == self.config.MACOS:
            self.run_mac()
        elif self.config.os_type == self.config.LINUX:
            self.run_linux()
        else:
            print(f"Cannot run for os_type: {self.config.os_type}")

    def run_mac(self):
        homebrew_install("rye")

    def run_linux(self):
        confirm_then_execute_shell_command(
            "Do you want to install rye?",
            "curl -sSf https://rye-up.com/get | bash",
        )


class HomeBrew(Package):
    def __init__(self, config):
        super().__init__(config)

    @staticmethod
    def name():
        return "homebrew"

    @check_executable_exists("brew", "homebrew")
    def run(self):
        if self.config.os_type == self.config.MACOS:
            self.run_mac()
        else:
            print(f"Cannot run for os_type: {self.config.os_type}")

    def run_mac(self):
        confirm_then_execute_shell_command(
            "Do you want to install homebrew?",
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
        )


class Starship(Package):
    def __init__(self, config):
        super().__init__(config)

    @staticmethod
    def name():
        return "starship"

    @check_executable_exists("starship")
    def run(self):
        if self.config.os_type == self.config.MACOS:
            self.run_mac()
        elif self.config.os_type == self.config.LINUX:
            self.run_linux()
        else:
            print(f"Cannot run for os_type: {self.config.os_type}")

    def run_mac(self):
        homebrew_install("starship")

    def run_linux(self):
        confirm_then_execute_shell_command(
            "Do you want to install starship?",
            "curl -sS https://starship.rs/install.sh | sh",
        )


class Fish(Package):
    def __init__(self, config):
        super().__init__(config)

    @staticmethod
    def name():
        return "fish"

    @check_executable_exists("fish")
    def run(self):
        if self.config.os_type == self.config.MACOS:
            self.run_mac()
        elif self.config.os_type == self.config.LINUX:
            self.run_linux()
        else:
            print(f"Cannot run for os_type: {self.config.os_type}")

    def run_mac(self):
        homebrew_install("fish")

    def run_linux(self):
        linux_install("fish")


class Rust(Package):
    def __init__(self, config):
        super().__init__(config)

    @staticmethod
    def name():
        return "rust"

    @check_executable_exists("cargo")
    def run(self):
        if self.config.os_type in {self.config.MACOS, self.config.LINUX}:
            confirm_then_execute_shell_command(
                "Do you want to install rust?",
                "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
            )
        else:
            print(f"Cannot run for os_type: {self.config.os_type}")


class RustApps(Package):
    def __init__(self, config):
        super().__init__(config)

        self.apps = [
            {"brew": "zellij", "cargo": "zellij"},
            {"brew": "bat", "cargo": "bat"},
            {"brew": "eza", "cargo": "eza"},
            {"brew": "bottom", "cargo": "bottom"},
            {"brew": "grex", "cargo": "grex"},
            {"brew": "dust", "cargo": "du-dust"},
            {"brew": "sk", "cargo": "skim"},
            {"brew": "fd", "cargo": "fd-find"},
            {"brew": "sd", "cargo": "sd"},
            {"brew": "gitui", "cargo": "gitui"},
            {"brew": "zoxide", "cargo": "zoxide"},
            {"brew": "ripgrep", "cargo": "ripgrep"},
            {"brew": "ouch", "cargo": "ouch"},
            {"brew": "dotter", "cargo": "dotter"},
        ]

    @staticmethod
    def name():
        return "rust_apps"

    def run(self):
        if self.config.os_type == self.config.MACOS:
            self.run_mac()
        elif self.config.os_type == self.config.LINUX:
            self.run_linux()
        else:
            print(f"Cannot run for os_type: {self.config.os_type}")

    def run_linux(self):
        cargo_install([app["cargo"] for app in self.apps])

    def run_mac(self):
        homebrew_install([app["brew"] for app in self.apps if app["brew"] is not None])

        apps = [app["brew"] for app in self.apps if app["brew"] is None]
        if len(apps) > 0:
            cargo_install(apps)


class Fisher(Package):
    def __init__(self, config):
        super().__init__(config)

    @staticmethod
    def name():
        return "fisher"

    def run(self):
        if self.config.os_type == self.config.MACOS:
            self.run_mac()
        elif self.config.os_type == self.config.LINUX:
            self.run_linux()
        else:
            print(f"Cannot run for os_type: {self.config.os_type}")

    def run_linux(self):
        confirm_then_execute_shell_command(
            "Do you want to install fisher?",
            "curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher",
        )

    def run_mac(self):
        homebrew_install("fisher")


class FishPlugins(Package):
    def __init__(self, config):
        super().__init__(config)

        self.plugins = ["jhillyerd/plugin-git"]

    @staticmethod
    def name():
        return "fish_plugins"

    def run(self):
        if self.config.os_type in {self.config.MACOS, self.config.LINUX}:
            self.install_plugins(self.plugins)
        else:
            print(f"Cannot run for os_type: {self.config.os_type}")

    def install_plugins(self, targets):
        if isinstance(targets, str):
            targets_str = targets
        elif isinstance(targets, list):
            targets_str = " ".join(targets)
        else:
            raise ValueError(f"Get targets: {targets}")

        if is_executable_exists("fisher"):
            confirm_then_execute_shell_command(
                f"Do you want to install {targets_str}?",
                f"fisher install {targets_str}",
            )
        else:
            print("Need fisher, do nothing.")
