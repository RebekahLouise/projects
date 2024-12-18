<div id="nav">
	<a href="member-page.php" title="Home"><button class="button buttonn">Home</button></a>
	<a href="member-page1.php" title="Page 1"><button class="button buttonn">?</button></a>
	<a href="member-page2.php" title="Page 2"><button class="button buttonn">??</button></a>
	<a href="change_password.php" title="New Password"><button class="button buttonn">New Password</button></a>
	<form method="post" action="">
		<button class="button buttonn" type="submit" name="logout">Logout</button>
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