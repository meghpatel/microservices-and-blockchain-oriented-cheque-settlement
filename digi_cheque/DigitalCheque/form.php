<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	<title>Print Digital Cheque</title>
</head>
<body style="background-image: url(static/totp.jpg);background-size:cover">	
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
		<h3>Enter the receiver's account details</h3>
		<div class="form-row">
				<div class="col-md-4 mb-3">
				  <label for="validationTooltip01">Name</label>
				  <input type="text" class="form-control" id="validationTooltip01" placeholder="First Name" value="Name" name="name" required>
				</div>
		</div>
		<div class="form-row">
					<div class="col-md-6 mb-3">
						  <label for="AccNumber">Account Number</label>
						  <input type="text" class="form-control" name="AccNo" id="AccNumber" placeholder="11 Digit AccNo" required>
					</div>
						<div class="col-md-3 mb-3">
								<label for="IFSC">IFSC</label>
								<input type="text" class="form-control" name="IFSC" id="IFSC" placeholder="SBI123" required>
						</div>
						<div class="col-md-3 mb-3">
								<label for="Amount">Amount (Rs.)</label>
								<input type="text" name="amount" class="form-control" id="amount" placeholder="1000 Rs." required>
						</div>
		</div>
		<button class="btn btn-primary" type="Submit" name="Submit">Register the customers</button>
	</form>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST")
{
	$name=$amount=$IFSC="";
	$name=$_POST['name'];
	$amount=$_POST['amount'];
	$IFSC=$_POST['IFSC'];
	ob_start();
	require('fpdf181/fpdf.php');
    $pdf = new FPDF();
    $pdf->AddPage();
    $pdf->Image('cheque.png',0,0,200,100);
    $pdf->SetFont('Arial', '', 18);
    //$pdf->Cell(55, 5, 'Reference Code', 0, 0);
    //$pdf->Cell(58, 5, ': 026ETY', 0, 0);
	//$pdf->Cell(25, 5, 'Date', 0, 0);
	$pdf->Ln(2);
    $pdf->Cell(100);
    $pdf->Cell(20, 5, '2019-09-29 11:47:10 AM', 0, 1);
    $pdf->Ln(15);
    //$pdf->Cell(55, 5, 'Amount', 0, 0);
    //$pdf->Cell(58, 5, ': 2674', 0, 0);
    //$pdf->Cell(25, 5, 'Channel', 0, 0);
    //$pdf->Cell(52, 5, ': WEB', 0, 1);
    //$pdf->Cell(55, 5, 'Status', 0, 0);
    //$pdf->Cell(58, 5, ': Complete', 0, 1);
    $pdf->Line(10, 30, 200, 30);
    $pdf->Cell(50);
    //$pdf->Cell(55, 5, 'Product Id', 0, 0);
    $pdf->Cell(58, 5, $name, 0, 1);
    $pdf->Ln(5);
    $pdf->Cell(50);
    $pdf->Cell(55, 5, 'Ten Thousands Only', 0, 0,'C');
    $pdf->Ln(5);
    $pdf->Cell(150);
    $pdf->Cell(58, 5, $amount, 0, 1);
    //$pdf->Cell(55, 5, 'Product Service Charge', 0, 0);
    //$pdf->Cell(58, 5, ': 0', 0, 1);
    //$pdf->Cell(55, 5, 'Product Delivery Charge', 0, 0);
    //$pdf->Cell(58, 5, ': 0', 0, 1);
    $pdf->Line(10, 60, 200, 60);
    //$pdf->Ln(10);//Line break
    //$pdf->Cell(55, 5, 'Paid by', 0, 0);
    //$pdf->Cell(58, 5, ': Nawaraj Shah', 0, 1,'C');
    //$pdf->Line(155, 75, 195, 75);
    $pdf->Ln(5);//Line break
    //$pdf->Cell(55, 5, 'Amount', 0, 0);
    //$pdf->Cell(50, 5, ': Signature', 0, 1, 'C');
	$pdf->Output();
	ob_end_flush(); 
}
    ?>