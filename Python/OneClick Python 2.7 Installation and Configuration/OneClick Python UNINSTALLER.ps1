$app = Get-WmiObject -Class Win32_Product | Where-Object { 
    $_.Name -match "python" 
}
$app.Uninstall()