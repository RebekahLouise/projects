<?php
session_start();
if (!isset($_SESSION['user_id']) || $_SESSION['user_level'] !== 1) {
    header('Location: login.php');
    exit();
}?>

<!DOCTYPE html>
<html lang=en>
	<head>
		<title>Admin Page - Website ni Chan</title>
		<meta charset=utf-8>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<link rel="stylesheet" type="text/css" href="css/design.css">
	</head>
	<body>
		<img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="5">
		<div id="container">
		<?php include('header.php');?>
		<?php include('nav-admin.php');?>
		<?php include('info-col.php');?>
			<div id="content">
				<h2>Welcome to the Admin Page</h2>
				<img src="https://media.tenor.com/9w7GOqvx2yYAAAAM/toby-fox.gif" alt="dog" width="150px"><br><br>	
				<h2>Dashboard?</h2>
				<img src="https://img.freepik.com/free-vector/colorful-infographic-graphs-diagrams-illustration_53876-18029.jpg" alt="uhhh..." width="1000px"><br><br><br><br>
				<img src="https://media.tenor.com/2UYGTk1wkEwAAAAi/annoying-dog-undertale.gif" width="100px" alt="dog">
			</div>
			<?php include('footer.php');?>
		</div>
	</body>
<html>
