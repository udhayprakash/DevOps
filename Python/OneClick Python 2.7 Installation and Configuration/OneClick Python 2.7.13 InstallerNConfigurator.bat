powershell -command "iwr -Uri https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi -OutFile C:\users\""$env:USERNAME""\Downloads\python-2.7.13.msi"
powershell -command "msiexec /i "C:\users\""$env:USERNAME""\Downloads\python-2.7.13.msi" /passive /norestart ADDLOCAL=ALL"
powershell -command '$env:path="$env:Path;C:\Python27"'