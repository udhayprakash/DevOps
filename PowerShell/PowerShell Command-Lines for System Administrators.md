#### To save the session work:
``` 
Start-Transcript ./test.txt
```
#### To Install a certificate using powershell:
```
$cert = New-SelfSignedCertificate -certstorelocation cert:\localmachine\my -dnsname testcert.ca.com
$pwd = ConvertTo-SecureString -String ‘passw0rd!’ -Force -AsPlainText
$path = 'cert:\localMachine\my\' + $cert.thumbprint 
Export-PfxCertificate -cert $path -FilePath C:\Users\praud01\Desktop\cert.pfx -Password $pwd
```
#### To List all the installed certificates in the server using powershell:
```
Set-Location Cert:\CurrentUser\My
Get-ChildItem | Format-Table Subject, FriendlyName, Thumbprint -AutoSize

Get-ChildItem -Path Cert:\CurrentUser\My | Format-Table Subject, FriendlyName, Thumbprint -AutoSize
```
```
$Cert = New-SelfSignedCertificate -CertstoreLocation Cert:\LocalMachine\My -DnsName "myHost"
```

#### How to install a new module in powershell?
- The modules can be installled from PowerShell Gallery via PowerShellGet. 

There are TWO ways to install a powerShell module. 

A. Online Mode: Follow this mode, if you are connected to internet. 

	Step 1: Open PowerShell as Administrator. Run the below command:
			
			Find-Module -Name <Module Name> 
			
		NOTE: If you have not accessed the PowerShell Gallery before, or perhaps have an out of date version of NuGet, 
		you may receive a message indicating there is a missing or out-of-date NuGet provider. 
		NuGet is a Package Management provider. These are primarily used to install, upgrade, configure, and/or remove
		software in an automated fashion. To accept the installation of a proper version of NuGet, hit “Y”.
		
	Step 2: If your desired module is resulted in the search, then install the module using the below command:
		
			Install-Module -Name <Module Name>  –Scope CurrentUser -Force 
		NOTE: Using -Force will avoid asking for permissions. If you want to check the permissions, remove '-Force' from command. 
	
	Step 3: To confirm the installed module packages, run the below command:
	
			Get-Module <Module Name> -ListAvailable
			
	Now, Installation of the Module is completed. You can start using the module. 
	
B. Offline Mode: Prefer this mode, only if your machine is NOT connected to Internet. 

	Step 1: Open PowerShell as Administrator. Run the below command:
			
			Find-Module -Name <Module Name> 
			
		NOTE: If you have not accessed the PowerShell Gallery before, or perhaps have an out of date version of NuGet, 
		you may receive a message indicating there is a missing or out-of-date NuGet provider. 
		NuGet is a Package Management provider. These are primarily used to install, upgrade, configure, and/or remove
		software in an automated fashion. To accept the installation of a proper version of NuGet, hit “Y”.
		
	Step 2: Now, save the module in your local machine at your desired path
	
		Save-Module -Name <Module Name> -Path C:\Path\To\Desired\Folder
		
		Choose the path based on your requirement:
			Local User: $home\Documents\WindowsPowerShell\Modules
			All Users: $pshome\Modules
			
	Now, the module is ready for usage. 
	
#### To uninstall a software, 
```
$(Get-WmiObject -Class Win32_Product -Filter "Name = 'Software Name'").Uninstall
```
#### One liner to get all COM objects
```
gci HKLM:\Software\Classes -ea 0| ? {$_.PSChildName -match '^\w+\.\w+$' -and
(gp "$($_.PSPath)\CLSID" -ea 0)} | ft PSChildName
```
#### Monitor Memory Usage of PowerShell instance
```
"$('{0:n2}' -f ([double](Get-Process -Id $pid).WorkingSet/1MB)) MB"
```
#### Invoke the Compress-Archive command directly (creates subfolder inside ZIP)
```
Compress-Archive -Path c:\temp -DestinationPath c:\backup\temp.zip ;
```
#### Pipe in a list of files/folders to the Compress-Archive command
```
Get-ChildItem -Path c:\temp | Compress-Archive -DestinationPath c:\backup\temp.zip -Update;
```
#### Extract the archive
```
Expand-Archive -Path C:\backup\temp.zip -DestinationPath c:\temp -Force;
```
#### windows speak interface
```
$talkIt = New-Object -ComObject SAPI.SpVoice
$talkIt.speak("Dear $env:Username the time is Date and time is  is $(get-date)")
```