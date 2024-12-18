<div id="nav">
	<a href="register-view-users.php" title="View all registered users"><button class="button buttonn">View Users</button></a>
	<a href="search_user.php" title="Search User"><button class="button buttonn">Search User</button></a>
	<a href="change_password.php" title="New Password"><button class="button buttonn">New Password</button></a>
	<form method="post" action="">
		<a href="index.php" title="Logout" type="submit" name="logout"><button class="button buttonn">Logout</button></a>
	</form>
<div>

<?php
if (isset($_POST['logout'])) {
    session_unset();
    session_destroy();
    header("Location: index.php");
    exit();
}
?>