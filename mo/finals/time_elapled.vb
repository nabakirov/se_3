Sub ElapsedTimeForTolerance_Click()
    Dim Solve As String
    Time_1 = Timer
    Solve = "_______ _______"
    Range("K18").Value = Null
    k_max = Cells(8, 11) 'Set number of iterations
    Range("H5").Value = 1
    Range("A7").Value = 0
    Range("H5").Value = 2
    k = 0
  Do While (Range("F7").Value <> Solve)
      Range("A7").Value = Range("A7").Value + 1
      k = k + 1
Loop
   Tolerance = Range("I5").Value
   Time_2 = Timer
   ElapsedTime1 = Time_2 - Time_1
   Range("K18").Value = " ElapsedTime (in sec) = " & ElapsedTime1 & _
   " for selected tolerance = " & Tolerance & _
   " and number of iterations = " & k
Cells(7, 1) = "=IF(H5=1,0,A7+1)" 'Restore the content of the cell A7
End Sub


Sub ElapsedTimeForK_max_Click()
Dim AA7, Solve As String
    Time_1 = Timer
    Range("K12").Value = Null
    k_max = Cells(8, 11) 'Set number of iterations
    Range("H5").Value = 1
    Range("A7").Value = 0
    Range("H5").Value = 2
    k = 0
 Do While (Range("A7").Value < k_max)
      Range("A7").Value = Range("A7").Value + 1
      k = k + 1
Loop
   Tolerance = Range("I5").Value
   Time_2 = Timer
   ElapsedTime1 = Time_2 - Time_1
   Range("K12").Value = " ElapsedTime (in sec) = " & ElapsedTime1 & _
   " for selected tolerance = " & Tolerance & _
   " and number of iterations = " & k
Cells(7, 1) = "=IF(H5=1,0,A7+1)" 'Restore the content of the cell A7
End Sub



' GSSM

Sub ElapsedTimeForK_max_Click()
Dim AA7, Solve As String
    Time_1 = Timer
    Range("A21").Value = Null
    k_max = Cells(8, 9) 'Set k_max a number of iterations
    Range("H6").Value = 1 'Set the program into the initial state
    Range("H8").Value = 0 ' Set the counter into zero
    Range("H6").Value = 2 'Set the program into the working state
    k = 0
 Do While (Range("H8").Value < k_max)
      Range("H8").Value = Range("H8").Value + 1
      k = k + 1
Loop
   Tolerance = Range("I6").Value 'Selected tolerance value
   Time_2 = Timer
   ElapsedTime1 = Time_2 - Time_1
   Range("A21").Value = " Elapsed Time (in sec) = " & ElapsedTime1 & _
   " at tolerance = " & Tolerance & _
   " and selected number of iterations = " & k
Cells(8, 8) = "=IF(H6=1,0,H8+1)" 'Restore the content of the cell H8
End Sub

Sub ElapsedTimeForTolerance_Click()
    Dim Solve As String
    Time_1 = Timer
    Solve = "The search is completed!!!"
    Range("E21").Value = Null
    k_max = Cells(8, 11) 'Set number of iterations
    Range("H6").Value = 1
    Range("H8").Value = 0
    Range("H6").Value = 2
    k = 0
  Do While (Range("H13").Value <> Solve)
      Range("H8").Value = Range("H8").Value + 1
      k = k + 1
Loop
   Tolerance = Range("I6").Value
   Time_2 = Timer
   ElapsedTime1 = Time_2 - Time_1
   Range("E21").Value = " ElapsedTime (in sec) = " & ElapsedTime1 & _
   " for selected tolerance = " & Tolerance & _
   " and at number of iterations = " & k - 1
Cells(8, 8) = "=IF(H6=1,0,H8+1)" 'Restore the content of the cell H8
End Sub

