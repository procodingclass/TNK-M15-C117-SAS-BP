SA3

Setup Send Email and Handle Exceptions.
======================


In this activity, you will learn to Setup SMTP server to send email securely and handled errors and exceptions.




<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10899395/118_3rd_outcome.gif" width = "480" height = "320">




Follow the given steps to complete this activity:
1. Setup Send Email and handle Exceptions.


* Open the file app.py.


* Send an email with sender and recipient email along with a message using the `sendmail()` method.
    ```sh
    smtp_server.sendmail(sender_email, recipient_email, message.as_string())
    ```


* Close the SMTP server connection after sending the mail using the `quit()` method.


    ```sh
    smtp_server.quit()
    ```


* Notify the user with a message `"Email sent"` by using ‘print()’ method.
 
    ```sh
    print("Email Sent", "Email sent successfully!")":
    ```  
* Display an error on exceptions using try and except method.
	```sh
    try:
        < Code to send Email using SMPT >...
        ... < Code to send Email >        


    except Exception as e:
        print("Error", f"An error occurred: {str(e)}")
    ```
   


* Save and run the code to check the output.