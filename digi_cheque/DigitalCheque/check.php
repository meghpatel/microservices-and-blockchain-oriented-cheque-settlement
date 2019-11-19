<?php
    require('fpdf181/fpdf.php');
    $pdf = new FPDF();
    $pdf->AddPage();
    $pdf->Image('cheque.png',0,0,200,100);
    $pdf->SetFont('Arial', '', 12);
    //$pdf->Cell(55, 5, 'Reference Code', 0, 0);
    //$pdf->Cell(58, 5, ': 026ETY', 0, 0);
    //$pdf->Cell(25, 5, 'Date', 0, 0);
    $pdf->Cell(100);
    $pdf->Cell(20, 5, ': 2019-09-29 11:47:10 AM', 0, 1);
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
    $pdf->Cell(58, 5, 'Naman Manish Kabra', 0, 1);
    $pdf->Ln(5);
    $pdf->Cell(50);
    $pdf->Cell(55, 5, 'Ten Thousands Only', 0, 0,'C');
    $pdf->Ln(5);
    $pdf->Cell(150);
    $pdf->Cell(58, 5, '10000', 0, 1);
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
    ?>