"A Wake-On-LAN script that is simple and easy to use eliminates the need to remember the MAC address of the single computer assigned to the script."

**Run**
python3 File/path/to/script/file/wake.py
python3 File/path/to/script/file/remsleep.py

**Or**

Follow the directions below in order to use the following
wake = wake.py
sleep = remsleep.py

**Notes:**
remsleep.py returns errors related to the paramiko library.  I have tried to make the code ignore these but they persist.  The errors do not impact the functionality of the code.  It performs as expected.
- paramiko/ file.py | channel.py | channel.py | channel.py | transport.py

**How to add Aliases to run commands from root:**
`cd ~`: ensure you are in the root directory
`echo $SHELL`: check which shell (zshrc or bashrc) you are running

zshrc:
- `nano .zshrc`
bashrc:
- `nano .bashrc`

**scroll to the bottom of the file that this opens (it may be empty)**
enter the following:
`alias wake="python3 /This/Is/The/File/Path/To/The/Script`
- you can replace 'wake' with anything you want to run the command

**save the file by using the options shown (^O to "write out" and ^X to "Exit")**

**restart the terminal**
`source .bashrc`
or
`source .zshrc`