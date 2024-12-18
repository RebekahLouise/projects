<?php
session_start();
if (!isset($_SESSION['user_id']) || $_SESSION['user_level'] !== 0) {
    header('Location: login.php');
    exit();
}?>

<!DOCTYPE html>
<html lang=en>
	<head>
		<title>Members Page - Website ni Chan</title>
		<meta charset=utf-8>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<link rel="stylesheet" type="text/css" href="css/design.css">
	</head>
	<body>
		<img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="5">
		<div id="container">
		<?php include('header.php');?>
		<?php include('nav-members.php');?>
		<?php include('info-col.php');?>
			<div id="content">
				<a href="https://www.youtube.com/watch?v=SDrBW7QVL-A&ab_channel=Palpe" target="_blank">
					<img src="https://i.redd.it/suub141h9cj51.gif" alt="dog" height="500">
				</a>
				<p style="color: black;">ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ</p>
			</div>
			<?php include('footer.php');?>
		</div>
	</body>
<html>