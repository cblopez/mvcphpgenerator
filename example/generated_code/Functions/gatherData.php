<?php

include __DIR__.'/../Models/User_Championship.php';
include __DIR__.'/../Models/Championship.php';
include __DIR__.'/../Models/User.php';

function gatherDataUser_Championship(){

	$championshipID = '';
	$login = '';
	$inscriptionDate = '';

	if($_POST){

		if(!empty($_POST['championshipID'])) $championshipID = $_POST['championshipID'];
		if(!empty($_POST['login'])) $login = $_POST['login'];
		if(!empty($_POST['inscriptionDate'])) $inscriptionDate = $_POST['inscriptionDate'];

		return new User_Championship_Model($championshipID!,$login!,$inscriptionDate);

	} else {

		if(!empty($_GET['championshipID'])) $championshipID = $_GET['championshipID'];
		if(!empty($_GET['login'])) $login = $_GET['login'];
		if(!empty($_GET['inscriptionDate'])) $inscriptionDate = $_GET['inscriptionDate'];

		return new User_Championship_Model($championshipID!,$login!,$inscriptionDate);

	}

}

function gatherDataChampionship(){

	$champeionshipID = '';
	$name = '';
	$startDate = '';
	$endDate = '';
	$level = '';

	if($_POST){

		if(!empty($_POST['champeionshipID'])) $champeionshipID = $_POST['champeionshipID'];
		if(!empty($_POST['name'])) $name = $_POST['name'];
		if(!empty($_POST['startDate'])) $startDate = $_POST['startDate'];
		if(!empty($_POST['endDate'])) $endDate = $_POST['endDate'];
		if(!empty($_POST['level'])) $level = $_POST['level'];

		return new Championship_Model($champeionshipID!,$name,$startDate,$endDate,$level);

	} else {

		if(!empty($_GET['champeionshipID'])) $champeionshipID = $_GET['champeionshipID'];
		if(!empty($_GET['name'])) $name = $_GET['name'];
		if(!empty($_GET['startDate'])) $startDate = $_GET['startDate'];
		if(!empty($_GET['endDate'])) $endDate = $_GET['endDate'];
		if(!empty($_GET['level'])) $level = $_GET['level'];

		return new Championship_Model($champeionshipID!,$name,$startDate,$endDate,$level);

	}

}

function gatherDataUser(){

	$login = '';
	$name = '';
	$surname = '';
	$email = '';
	$password = '';

	if($_POST){

		if(!empty($_POST['login'])) $login = $_POST['login'];
		if(!empty($_POST['name'])) $name = $_POST['name'];
		if(!empty($_POST['surname'])) $surname = $_POST['surname'];
		if(!empty($_POST['email'])) $email = $_POST['email'];
		if(!empty($_POST['password'])) $password = $_POST['password'];

		return new User_Model($login!,$name,$surname,$email,$password);

	} else {

		if(!empty($_GET['login'])) $login = $_GET['login'];
		if(!empty($_GET['name'])) $name = $_GET['name'];
		if(!empty($_GET['surname'])) $surname = $_GET['surname'];
		if(!empty($_GET['email'])) $email = $_GET['email'];
		if(!empty($_GET['password'])) $password = $_GET['password'];

		return new User_Model($login!,$name,$surname,$email,$password);

	}

}

?>