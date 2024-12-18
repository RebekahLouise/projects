<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  require('mysqli_connect.php');
  $errors = [];

  if (empty($_POST['email'])) {
    $errors[] = 'Please enter your email address.';
  } else {
    $email = trim($_POST['email']);
  }

  if (empty($_POST['psword'])) {
    $errors[] = 'Please enter your password.';
  } else {
    $password = trim($_POST['psword']);
  }

  if (empty($errors)) {
    $hashed_password = sha1($password);
    $query = "SELECT user_id, fname, user_level FROM users WHERE email = '$email' AND psword = '$hashed_password'";
    $result = @mysqli_query($dbcon, $query);

    if (mysqli_num_rows($result) == 1) {
      $row = mysqli_fetch_assoc($result);

      session_start();
      $_SESSION['user_id'] = $row['user_id'];
      $_SESSION['user_level'] = (int)$row['user_level'];
      $url = ($_SESSION['user_level'] === 1) ? 'admin-page.php' : 'member-page.php';
      header('Location: ' . $url);
      mysqli_free_result($result);
      mysqli_close($dbcon);
      exit();
    } else {
      $errors[] = 'Invalid email or password.';
    }
  }

  mysqli_close($dbcon);
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Login - Website ni Chan</title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="css/design.css">
</head>
<body>
  <div id="container">
    <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="5">
    <?php include('header.php'); ?>
    <?php include('nav.php'); ?>
    <?php include('info-col.php'); ?>
    <div id="content">
    <?php if (!empty($errors)) : ?>
        <h2>Error!</h2>
        <p>The following error(s) occurred:</p>
        <ul>
            <?php foreach ($errors as $msg) : ?>
                <li>→ <?php echo $msg; ?><br></li>
            <?php endforeach; ?>
        </ul>
        <h3>Please try again.</h3>
    <?php endif; ?>

        <h2>Login</h2>
            <div class="login">
            <form action="login.php" method="post">
                <div class="form-group">
                    <label for="email">Email Address:</label>
                    <input type="email" id="email" name="email" size="30" maxlength="50" value="<?php if (isset($_POST['email'])) echo htmlspecialchars($_POST['email']); ?>">
                </div>
                <div class="form-group">
                    <label for="psword">Password:</label>
                    <input type="password" id="psword" name="psword" size="30" maxlength="40">
                </div>
                <div class="Login">
                    <div class="button-container">
                        <input class="button buttonn" type="submit" id="submit" name="submit" value="Login">
                    </div>
                </div>
            </form>
        </div>
            <br>
            <br>
            <br>
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
            <img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="15">
        </div>            

        <?php include('footer.php'); ?>
    </div>
</body>
</html>
