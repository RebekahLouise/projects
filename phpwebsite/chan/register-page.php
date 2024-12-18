<!DOCTYPE html>
<html lang="en">
<head>
    <title>Register Page - Website ni Chan</title>
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
            <?php
                if ($_SERVER['REQUEST_METHOD'] == 'POST') {
                    $errors = array();
                    if (empty($_POST['fname'])) {
                        $errors[] = 'Please enter your first name.';
                    } else {
                        $fn = trim($_POST['fname']);
                    }

                    if (empty($_POST['lname'])) {
                        $errors[] = 'Please enter your last name.';
                    } else {
                        $ln = trim($_POST['lname']);
                    }

                    if (empty($_POST['email'])) {
                        $errors[] = 'Please enter your email address.';
                    } else {
                        $e = trim($_POST['email']);
                    }

                    if (!empty($_POST['psword1'])) {
                        if ($_POST['psword1'] != $_POST['psword2']) {
                            $errors[] = 'Your passwords do not match.';
                        } else {
                            $p = trim($_POST['psword1']);
                        }
                    } else {
                        $errors[] = 'Please enter your password.';
                    }

                    if (empty($errors)) {
                        require('mysqli_connect.php');
                        $hash = sha1($p);
                        $q = "INSERT INTO users (fname, lname, email, psword, registration_date) VALUES ('$fn', '$ln', '$e', '$hash', NOW())";
                        $result = @mysqli_query($dbcon, $q);
                        if ($result) {
                            header("location: register-thanks.php");
                            exit();
                        } else {
                            echo '<h2>System Error</h2>
                            <p class="error">You could not be registered due to a system error. We apologize for any inconvenience.</p>';
                            echo '<p>' . mysqli_error($dbcon) . '</p>';
                        }
                        mysqli_close($dbcon);
                        include('footer.php');
                        exit();

                    } else {
                        echo '<h2>Error!</h2>
                        <p>The following error(s) occurred:<br/>';
                        foreach ($errors as $msg) {
                            echo "→ $msg<br/>";
                        }
                        echo '</p><h3>Please try again.</h3><br/><br/>';
                    }
                }
            ?>

            <h2>Register</h2>
            <div class="register">
                <form action="register-page.php" method="post">
                    <div class="form-group">
                        <label for="fname">First Name:</label>
                        <input type="text" id="fname" name="fname" size="30" maxlength="40" value="<?php if (isset($_POST['fname'])) echo htmlspecialchars($_POST['fname']); ?>">
                    </div>
                    <div class="form-group">
                        <label for="lname">Last Name:</label>
                        <input type="text" id="lname" name="lname" size="30" maxlength="40" value="<?php if (isset($_POST['lname'])) echo htmlspecialchars($_POST['lname']); ?>">
                    </div>
                    <div class="form-group">
                        <label for="email">Email Address:</label>
                        <input type="email" id="email" name="email" size="30" maxlength="50" value="<?php if (isset($_POST['email'])) echo htmlspecialchars($_POST['email']); ?>">
                    </div>
                    <div class="form-group">
                        <label for="psword1">Password:</label>
                        <input type="password" id="psword1" name="psword1" size="30" maxlength="40">
                    </div>
                    <div class="form-group">
                        <label for="psword2">Confirm Password:</label>
                        <input type="password" id="psword2" name="psword2" size="30" maxlength="40">
                    </div>
                    <div class="form-group">
                        <div class="button-container">
                            <input class="button buttonn" type="submit" id="submit" name="submit" value="Register">
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
