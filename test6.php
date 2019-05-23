<?php

    include "static/data.php";
    if(isset($_POST['Sensor1']))
    {    
        $conn = mysqli_connect($HOST, $USER,$PASSWORD);
        if(!$conn)
            echo "Connect Error ".mysqli_error();
        else
        {   
            mysqli_select_db($conn, $DATABASE);
            $RESULT = mysqli_query($conn, "SELECT * FROM $TABLE1");
            $num = mysqli_num_rows($RESULT);
            $sensor = new Sensor1;
            for($i=0; $i<$num; $i++)
            {
                $tmp = mysqli_fetch_assoc($RESULT);
                array_push($sensor->temp, $tmp["$COLUM_TEMP"]);
                array_push($sensor->hum, $tmp["$COLUM_HUM"]);
                array_push($sensor->winspeed, $tmp["$COLUM_Winspeed"]);
                array_push($sensor->wstatus, $tmp["$COLUM_Wstatus"]);
                array_push($sensor->time, $tmp["$COLUM_TIME"]);
            }
            echo json_encode($sensor);
            mysqli_close($conn);
        }    
    }
	
?>
