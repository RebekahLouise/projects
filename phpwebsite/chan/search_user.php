<?php
session_start();
if (!isset($_SESSION['user_id']) || $_SESSION['user_level'] !== 1) {
    header('Location: login.php');
    exit();
}?>

<!DOCTYPE html>
<html lang=en>
	<head>
		<title>New Password - Website ni Chan</title>
			<meta charset=utf-8>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
			<link rel="stylesheet" type="text/css" href="css/design.css">
	</head>
	<body>
		<img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="5">
		<div id="container">
			<?php include('header.php');?>
			<?php include('nav-return.php');?>
			<?php include('info-col.php');?>
			<div id="content">
				<h2>Search...</h2>
				<p>よせ、この機能はまだ使えないよ</p>
			</div>
			<?php include('footer.php');?>
		</div>
	</body>
<html>