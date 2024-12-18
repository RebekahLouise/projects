<?php
session_start();
if (!isset($_SESSION['user_id']) || $_SESSION['user_level'] !== 1) {
    header('Location: login.php');
    exit();
}?>

<!DOCTYPE html>
<html lang=en>
	<head>
		<title>Registered Users - Website ni Chan</title>
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
				<h2>Registered Users</h2>
				<p>
					<?php
						//require db connection
						require("mysqli_connect.php");
						//query to get data from db
						$q = "SELECT CONCAT(lname ,', ', fname) AS fullname, email, DATE_FORMAT(registration_date, '%M %d, %Y') AS regdat, user_id FROM users ORDER BY user_id ASC";
						$result = @mysqli_query($dbcon, $q);
						//if query SUCCESS!... 
						if($result) {
							echo '<table><tr class="top">
							<td><strong>Name</strong></td>
							<td><strong>Email</strong></td>
							<td><strong>Registered Date</strong></td>
							<td colspan=2><strong>Actions</strong></td>
							</tr>';
							while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
								echo '<tr><td>'.$row['fullname'].'</td>
								<td>'.$row['email'].'</td>
								<td>'.$row['regdat'].'</td>
								<td class="icon"><a href="edit_user.php?id='.$row['user_id'].'" class="fa fa-edit"></a></td>
								<td class="icon"><a href="delete_user.php?id='.$row['user_id'].'" class="fa fa-trash-o"></a></td>
								</tr>';
							}
							echo '</table>';
							mysqli_free_result($result);

						} else { // if not success...
							echo'<p>The current registered users could not be retrieved. Contact the system administration</p>';
                        }
						mysqli_close($dbcon);
					?>
				</p>
			</div>
			<?php include('footer.php');?>
		</div>
	</body>
<html>