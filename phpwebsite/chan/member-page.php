<?php
session_start();
if (!isset($_SESSION['user_id']) || $_SESSION['user_level'] !== 0) {
    header('Location: login.php');
    exit();
}?>

<!DOCTYPE html>
<html lang=en>
	<head>
		<title>Members Page - Website ni Chan</title>
		<meta charset=utf-8>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<link rel="stylesheet" type="text/css" href="css/design.css">
	</head>
	<body>
		<img src="https://media.tenor.com/mr9ZTxhFxVAAAAAj/annoying-dog-undertale.gif" alt="dog" height="5">
		<div id="container">
		<?php include('header.php');?>
		<?php include('nav-members.php');?>
		<?php include('info-col.php');?>
			<div id="content">
				<h2>Welcome to the Members Page</h2>
				<br>
				<a href="https://www.youtube.com/watch?v=SDrBW7QVL-A&ab_channel=Palpe" target="_blank">
					<img src="https://media.tenor.com/CNBGgG2DU10AAAAM/nyan-cat-poptart.gif" alt="dog">
				</a>
				<p style="color: black;">ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eget dignissim dolor. Morbi sagittis turpis quis augue porta, id venenatis eros consectetur. Cras porta urna sit amet risus accumsan, non ultrices urna imperdiet. Proin mattis aliquam bibendum. Donec sodales nulla id dolor luctus, ac hendrerit nisl blandit. Suspendisse in massa velit. Praesent dictum mollis justo, id varius justo efficitur nec. Proin interdum orci a maximus malesuada. Quisque nec nibh eros. Pellentesque ultrices eros augue, nec porta diam sagittis id.</p>
				<br>
				<a href="https://www.youtube.com/watch?v=SDrBW7QVL-A&ab_channel=Palpe" target="_blank">
					<img src="https://static.wikia.nocookie.net/78c578bd-542a-47ec-8adc-b959bc96bc3e/scale-to-width/370" alt="dog" width="100px">
				</a>
				<br>
				<br>
				<p>Aliquam erat volutpat. Maecenas facilisis faucibus ex nec mollis. Suspendisse nec orci et magna tincidunt blandit sit amet et magna. Nullam eget neque gravida, dapibus justo in, egestas lacus. Duis tempus maximus imperdiet. Curabitur sed placerat sem. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Fusce ac diam arcu. Nullam at nisi eget diam rutrum porttitor. Nulla sagittis orci vel nulla placerat, eget eleifend urna bibendum. Praesent maximus neque maximus mauris pretium ultricies. Aenean scelerisque nec turpis vitae varius.</p><br>
				<a href="https://www.youtube.com/watch?v=SDrBW7QVL-A&ab_channel=Palpe" target="_blank">
					<img src="https://static.wikia.nocookie.net/428b4fbe-acda-4145-80e1-61ac89004c77/scale-to-width/755" alt="dog" width="250px">
				</a>
				<br>
				<br>
				<p>Vestibulum viverra tellus nec enim vestibulum, et dignissim velit congue. Suspendisse id auctor est. Donec malesuada quis erat et semper. In tempor, elit eu lobortis rhoncus, ante dui pellentesque justo, sit amet eleifend libero dui eu felis. Fusce maximus arcu vitae ante iaculis aliquam. Praesent ipsum est, maximus ut erat id, maximus aliquet libero. Fusce gravida tellus a quam consectetur dapibus. Cras ut erat ut leo malesuada feugiat. Morbi vel viverra lectus, ac pretium ipsum. Phasellus metus elit, commodo eu ipsum non, mollis vehicula nunc. Aliquam consequat neque vitae sapien blandit, eget cursus mi sagittis. Etiam imperdiet mi a lacus dapibus porta.</p>
				<br>
				<br>
				<a href="https://www.youtube.com/watch?v=SDrBW7QVL-A&ab_channel=Palpe" target="_blank">
					<img src="https://media.tenor.com/2UYGTk1wkEwAAAAi/annoying-dog-undertale.gif" alt="dog" width="100px">
				</a>
			</div>
			<?php include('footer.php');?>
		</div>
	</body>
<html>