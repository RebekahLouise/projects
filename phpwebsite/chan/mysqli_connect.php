<?php
$dbcon = @mysqli_connect('localhost', 'reisechan', 'reisechan', 'members_chan')
OR die('Could not connect to the MySQL server: '. mysqli_connect_error());
mysqli_set_charset($dbcon, 'utf8');
