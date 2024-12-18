<?php
session_start();
if (!isset($_SESSION['user_id']) ||  $_SESSION['user_level'] !== 1 && $_SESSION['user_level'] !== 1) {
    header('Location: login.php');
    exit();
}?>

<!DOCTYPE html>
<html lang=en>
	<head>
		<title>Website ni Chan</title>
		<meta charset=utf-8>
		<link rel="stylesheet" type="text/css" href="css/design.css">
	</head>
	<body>
		<h2>Deleting Record...</h2>
		<div id="container">
				<?php
					if((isset($_GET['id'])) && (is_numeric($_GET['id']))) {
						$id = $_GET['id'];
					} elseif((isset($_POST['id'])) && (is_numeric($_POST['id']))) {
						$id = $_POST['id'];
					} else {//no valid id number. stop script
						echo '<p>nope</p>';
						echo '<h4><a href="register-view-users.php" >go back pls</a></h4>'; //redirect
						exit();
					}
					
					require('mysqli_connect.php');
					if($_SERVER['REQUEST_METHOD'] == 'POST') {
						if($_POST['sure'] == 'Yes') {
							$q = "DELETE from users where user_id=$id"; //delete specific user
							$result = @mysqli_query($dbcon, $q);
							if(mysqli_affected_rows($dbcon) == 1) {
								echo'<p>Deleted Successfully.</p>';
								echo '<h4><a href="register-view-users.php" >go back</a></h4>'; //link going back to view-users page
							} else {
								echo '<p>uhh something happened and idkwhat</p>';
								echo '<h4><a href="register-view-users.php" >go back</a></h4>'; //link going back to view-users page
							}
						} else { //if no
							echo '<p>record was not deleted</p>'; //record was not deleted
							echo '<h4><a href="register-view-users.php" >go back</a></h4>'; //link going back to view-users page
						}
					} else { //display details of user to be deleted
						$q = "SELECT CONCAT (fname, ' ', lname) from users where user_id=$id";
						$result = @mysqli_query($dbcon, $q);
						if(mysqli_num_rows($result) == 1) {
							$row = mysqli_fetch_array($result, MYSQLI_NUM);
							echo "<h3>Are you sure you want to delete $row[0]?</h3>";
							echo '
							<div class="center">
							<div class="button-container">
								<form action="delete_user.php" method="post">
									<input class="button buttonn" id="submit-yes" type="submit" name="sure" value="Yes">
									<input class="button buttonn" id="submit-no" type="submit" name="sure" value="No">
									<input type="hidden" name="id" value="'.$id.'">
								</form>
							</div>
							</div>
							';
						} else {//not valid id. no members found
							echo "<h3>who?</h3>";
							echo '<h4><a href="register-view-users.php" >go back pls</a></h4>'; //redirect
						}
					}
					mysqli_close($dbcon);
				?>
			</div>
		</div>
	</body>
</html>