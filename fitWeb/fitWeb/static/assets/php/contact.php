<?php
	$name = $_POST['name'];
	$phone = $_POST['phone'];
	$email = $_POST['email'];
	$message = $_POST['message'];
	$for = 'mail@example.com';
	$subject = 'new message';
	$header = 'From: ' . $email;
	$msgMail = "Name: $name\n Phone: $phone\n E-Mail: $email\n Message:\n $message";
	  
	if ($_POST['submit']) {
		if (mail($for, $subject, $msgMail, $header)) {
			echo "<script language='javascript'>
			alert('Message Sent');
			window.location.href = '../../index.html';
			</script>";
		} 
		else {
			echo 'Something went wrong';
		}
	}
?>