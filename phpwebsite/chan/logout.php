<?php
session_start();

if (!isset($_SESSION['user_id']) || $_SESSION['user_level'] !== 0 && $_SESSION['user_level'] !== 1) {
    header('Location: index.php');
    exit();
}

if (isset($_POST['logout'])) {
    session_unset();
    session_destroy();
    header("Location: index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Logout - Website ni Chan</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="css/design.css">
</head>
<body>
    <h2>Are you sure you want to log out?</h2>
    <form method="post" action="">
        <button class="button buttonn" type="submit" name="logout">Yes</button>
        <button class="button buttonn"><a href="javascript:history.back()">No</a></button>
    </form>
</body>
</html>