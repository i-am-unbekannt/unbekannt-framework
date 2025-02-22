# Unbekannt Framework
The Unbekannt Framework is a hacking and penetration testing tool designed specifically for Windows.

<p align="center">
  <img src="https://raw.githubusercontent.com/i-am-unbekannt/unbekannt-framework/main/libreq/logo.png">
</p>

## End of Linux Support
The Linux version is no longer supported. The last supported version for Linux is 6.0, which can be found in this repository.
This decision was made because the Unbekannt Framework was originally designed for Windows, and not all features are compatible with Linux.

## Installing
Latest Version (Recommended):
* Download [Unbekannt Framework v7.5.0]
  Release Date: soon

Older versions:
* Download [Unbekannt Framework v7.2.2](https://www.mediafire.com/file/pw1ztzmh7x4i4dl/unbekannt-framework-v7.2.2-x64-installer.exe/file)
  Release Date: November 8, 2022

* Download [Unbekannt Framework v7.1](https://www.mediafire.com/file/fzmtezq4xdob3t0/unbekannt-framework-v7.1-windows-x64-installer.exe/file)
  Release Date: September 25, 2022

## Using the Unbekannt Framework
To see a list of all available commands in the framework, use the `help` command. For a list of all available modules, use the `modules` command.

Each module has a set of options which must be set before running. These can be seen with the `options` or `show options` command:

```
Unbekannt module(attack/ip_grabber) > options

 Module options (module/attack/ip_grabber):

  Name   Description      Current Setting
  ----   -----------      ---------------
  URL    Redirect url
  PORT   Localhost port   5000
  TOKEN  Ngrok API Token
```

### Setting option
Traditional usage of the Unbekannt Framework involves loading a module, and setting multiple options individually:

```
use module/attack/ip_grabber
set URL https://facebook.com
set TOKEN MySecretToken
run
```

### Module interface Commands
The following commands are available for every module to set values, execute the module, or exit the module interface:

```
Command    Description
-------    -----------
run        Run the module
set        Set a value for a object
back       Leave the module
clear      Clear the screen
options    Show available options for the module
help       List all commands
```

## Import Modules
As of February 22, 2025, only Python modules are supported. To import a module, navigate to your installation path and place the `.py` file into the `import` folder.

The default installation path is:
`C:\Program Files (x86)\i-am-unbekannt\Unbekannt Framework`

Make sure that Python is installed on your machine, along with all the required dependencies for the imported modules to run correctly. 

## Build Modules
To build your own modules, you can check out the default module `change_mac.py` as an example of the required structure.

If you want to share your module with the community, create an issue in the repository. Make sure to provide a detailed description of your module and include a contact method, so you can be informed if your module is added to the official set of default modules.

### Python Imports and Required Values
By default, all modules require the following imports and predefined values:

```
from colorama import Fore, init
from termcolor import colored

init()

RN = Fore.RED
R = Fore.LIGHTRED_EX
Y = Fore.YELLOW
G = Fore.LIGHTGREEN_EX
M = Fore.MAGENTA
C = Fore.CYAN
W = Fore.WHITE
B = Fore.LIGHTBLUE_EX
RB = Fore.RED
GR = Fore.LIGHTBLACK_EX
FB = Fore.BLACK
```

### Module Author
When creating your module, make sure to define the following metadata: Name, Description, and Author to give credit where it's due:

```
__CommandName__ = "change_mac"
__Description__ = "change the MAC address of a specific network interface"
__Author__      = "@i_am_unbekannt"
```

### Functions
Each command must be defined within a function and be callable. You may also create a class and add your functions there. Below is the default `help` function for the module:

```
def Module_Help():
    length = len(__CommandName__)
    print(f"""
 Information
 ===========

 {__Description__}
 By: {__Author__}
          
 Options for module(import/{__CommandName__})
 ==========================={'=' * length}

  Command                     Description
  ———————                     ———————————

  mac show all                displays the MAC addresses of all interfaces
  mac show                    shows your current MAC address
  mac set <INTERFACE> <MAC>   sets a specific MAC address for a given interface


 Module interface Commands
 =========================

  Command    Description
  ———————    ———————————
  back       leave the module
  clear      clear the screen
  help       list all commands
  """)
```

### Main Function
The example module `change_mac.py` is simple, and the following code represents the default structure for the main function of your module. It is recommended to use this structure as the default main function and simply add your custom commands to it:

```
def MAIN():
    try:
        while True:
            Ans_Input = input(colored('Unbekannt', 'white', attrs=['underline']) +' module('+RB+f'import/{__CommandName__}'+W+') '+R+'>'+W+' ')

            elif Ans_Input == "My Custom Command": # Your custom command
                MyCustomFunc()                     # Call your custom function

            elif Ans_Input == "":
                continue

            elif Ans_Input == "clear":
                os.system("cls")

            elif Ans_Input.lower() in ["exit", "back"]:
                return

            elif Ans_Input.lower() == "help" or Ans_Input.lower() == "options":
                Module_Help()

            else:
                print(R + "[-]" + W + " command not found: '" + Ans_Input + "'")

    except KeyboardInterrupt:
        return
    except Exception as E:
        print(R + "[-]" + W + f" Module Error: {E}")
        return

if __name__ == "__main__":
    MAIN()
```
