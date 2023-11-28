AA1
Send Multiple Emails		
======================


In this activity, you will add multiple email ids which are separated by commas to send them emails.




<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10947277/118_aa1_op.gif" width = "480" height = "320">




Follow the given steps to complete this activity:
1. Send Multiple Emails 


* Open the file `app.py`.


* Get emails separated by commas and remove white spaces by using `split()` method.


    ```sh
    recipients_email = input("Enter Comma Separated Recipient Email\n").strip()
    ```


* Split the recipient email values by comma.


    ```sh
    recipients_email = recipients_email.split(",")
    ```
*  Write for loop to send email to multiple recipients which is separated by commas and stored in `recipients_emails` variable.


    ```sh
    for email_id in recipients_email:
        try:
        .
        .
        .
	```
* Save and run the code to check the output.
