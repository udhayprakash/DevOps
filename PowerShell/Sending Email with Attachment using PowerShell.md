
## Sending Email With Attachment Within Domain Using PowerShell

If you are interested in sending Email to anyone within the domain, follow the below code:
The best part is that it doesn't ask for credentials; it will take the  `Active Directory` credentials of system user from where the script is getting executed.

```bash
$emailSender = "sender@domain.com"
$emailRecipientList = "receiver@domain.com"
$EmailBody = "This is email body."
$EmailSubject = "Email Subject"
$CompanySMTPServer = "mail.domain.Com"
$EmailAttachmentPath = "C:\path\of\file\to\attach.jpg"
try
{
    Send-MailMessage -From $emailSender -To $emailRecipientList -Subject $EmailSubject -SmtpServer $CompanySMTPServer -Body $EmailBody -Attachments $EmailAttachmentPath
}
catch
{
    write-Host "Unable to send email. The Exception is ", $_.Exception
}
```
If you have more than one Email attachment, separate them with comma. 

`P.S.` The hack is that this script can be used to send email from anyone to any other, within the domain, without informing the `sender`. It works as if the `sender` initiated the Email. 

Hail `Active Directory`