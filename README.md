## 🦇 VampFetch 

### Neofetch like utility built in Python for Linux.

*This project does not aim to be a replacement to any of the already existing utilities as they are faster, better and more accurate. Mine is merely a fun project I did in like 2 hours.*

![example image](https://github.com/anshag2007/vampfetch/blob/master/ex.png?raw=true)

#### Issues
- Wasn't able to fetch GPU details
- Packages are only displayed for Arch-based distros, though that can be changed by changing the command that fetches the package list to your own distro's command
- Terminal only fetches $TERM env. variable and does not accurately display the name of the terminal application at times (Ex: when using tmux)
- Shell only fetches the $SHELL env. variable and displays the path of the shell binary

##### I have no intention of trying to fix the issues that persist since a utility like this is impractical in Python because of the speed limitations of the language. 
