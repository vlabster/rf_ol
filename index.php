<?
// $out = null;
// $ret = null;
// system('python main.py');

// function issetParams($ms = []) {

//     foreach ($ms as $key => $value) {
//         var_dump($_REQUEST[$value]);
//         var_dump(!isset($_REQUEST[$value]));
//         if (!isset($_REQUEST[$value])) {

//             return false;
//         }
//     }

//     return true;
// }
// phpinfo();
ini_set('error_reporting', E_ALL);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
// if (issetParams(["first_name", "middle_name", "second_name", "birthdate", "country"])) {
$first_name = isset($_REQUEST["first_name"]) ? $_REQUEST["first_name"] : 'RANDOM';
$middle_name = isset($_REQUEST["middle_name"]) ? $_REQUEST["middle_name"] : 'RANDOM';
$second_name = isset($_REQUEST["second_name"]) ? $_REQUEST["second_name"] : 'RANDOM';
$birthdate = isset($_REQUEST["birthdate"]) ? $_REQUEST["birthdate"] : 'RANDOM';
$country = isset($_REQUEST["country"]) ? $_REQUEST["country"] : 'RANDOM';

$filename = uniqid();
$command = escapeshellcmd("main.py " . $first_name . ' ' 
. $middle_name . ' ' . $second_name . ' ' . $birthdate . ' ' 
. $country . ' ' . $filename);
// system('sudo python ' . $command);
$output = shell_exec($command);
echo "<img src='result/" . $filename . ".png'>";
// sleep(5);
// unlink('result/' . $filename . '.png');
// }
// else {
//     var_dump($_REQUEST);
//     var_dump($_GET);
// }
