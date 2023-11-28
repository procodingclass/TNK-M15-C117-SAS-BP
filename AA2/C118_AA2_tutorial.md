AA2
Debug with correct parameters
======================


In this activity, you will debug the code with correct values and parameters.




<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10899395/118_3rd_outcome.gif" width = "480" height = "320">




Follow the given steps to complete this activity:
1. Debug with correct parameters


* Open the file `app.py`.


*  Fix the host and port number to set up the SMTP server.


  	```sh
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    ```


*  Add parameters to start the TLS service.
    ```sh
    smtp_server.starttls()
    ```


*  Use `login()` method to add username and password to login into gmail account.
    ```sh
    smtp_server.login(sender_email, sender_password)
    ```


* Save and run the code to check the output.