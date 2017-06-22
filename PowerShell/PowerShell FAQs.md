PowerShell FAQs
------------------

__Q) What are the advantages of cmdlets?__

- They share a common and regular command-line syntax
- They support rich pipeline scenarios (using output of one command as input of another)
- They produce easily manageable object-based output, rather than error-prone plain-text output.


__Q)Redirect output of a command or pipeline into a file__

	Out-File:

		Get-ChildItem | Out-File unicodeFile.txt
		Get-Content filename.cs | Out-File -Encoding ASCII file.txt
		Get-ChildItem | Out-File -Width 120 unicodeFile.cs
	Redirection operators:
		Get-ChildItem > files.txt
		Get-ChildItem 2> errors.txt
		Get-ChildItem n> otherStreams.txt
	
Here, redirecting operator has greater control over redirecting individual streams

__Q)In PowerShell, the default output encoding format is UTF-16.__

__Q) TO append output of pipeline into a file__
	Out-File:
		Get-ChildItem | Out-File -Append files.txt
	Redirection operators:
		Get-ChildItem >> files.txt

__Q) How to use powershell cmdlets, providers, or script-based extensions written by 3rd party.__
If module is part of standard powershell module path, run
``` Invoke-NewCommand ```
If it is not, use Import-Module
	To import a module from a specific directory:
```	Import-Module C:\path\to\module ```
	To import a module from a specific file (module, script or assembly):
```Import-Module C:\path\to\module\file.extn```

__Q) Module vs snappins__

* snapins were packages for extensions in version 1 of powershell, and are rarely used. 
* snapins support only compiled extensions and are difficult to install.
	
* Modules are introduced in version 2. They are easy to install

__Q) Filter items in a list or command output__

To processes which have "Search" in their name:
```
Get-Process | Where-Object { $_.Name -like "*Search*" }
```
To list all processes not responding, test the Responding property:
```
Get-Process | Where-Object { -not $_.Responding }
```
To list all stopped services, 
```
Get-Service | Where-Object { $_.Status -eq "Stopped" }
```
For simple comparisions, script block can be eliminated
```
Get-Process | Where-Object Name -like "*Search*"
```	
In the script block, the $_ (or $PSItem) variable represents the current input object.