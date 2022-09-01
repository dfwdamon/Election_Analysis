# Election_Analysis

## Overview of Election Audit
This project is to analyze election data using Python code, read and review the data provided by a third party with the purpose of conducting an audit of the data.  The audit will then produce a documented result of the audit and its assessment or the outcome.

## Purpose
The purpose of this project is to create a Python script that will run using data provided by the client (Colorado Board of Elections) and determing the total number of votes cast, produce a list of candidates who received votes, show the total number of votes each candidate received, the percentage of votes each candidate won, and present the winner of the election based on popular vote. 

## Election Outcome
The Python script assesed the data file provided by the client by reading the file, analyzing the content, then organizing the data and tabulating it on a per candidate, per district/county and voter ID detail to calculate the necessary outputs as described in the purpose.  When the script is ran using the inpu file, it reads and outputs both a terminal result and a printed result to a file.  The final results of the script for this election data producted the following outputs:

<ul>
<li> -Total Votes<br>
-County Votes<br>
-County name<br>
-Largest County Tournout<br>
-Candidate Name, Percent votes won, Vote total<br>
-Winning Candidate<br>
-Winning Vote Count<br>
 -Winning Percentage</li>
</ul>

## Statement to the Commission
The python script created for the election analysis and audit was developed in part to validate the results of the election utilizing data provided by the electoral commission.  This data was provided to help certify the election results and check that the data was complete and accurate.  

The script was desigend to be used on a go forwad basis to further validate election data for future elections.  Note that the data input into the script is analyzed and read based on the file content and containging data types.  The script will read and analyze the data, but give no guarantee to the content or nature of the file being provided by the election commision or third party.

As an example, the script may be modified in the following two ways:

<ol>
<li>``The script can load different file names and from other drive or folder locations to be read by editing the `file_to_load = os.path.join` line by changing the file location and/or file name within the ``("new file name")` at the end of this line of code.`` 

<li>``Second, the output of the election results can be sent to a different file name or file location by editing the script line of code for `txt_file.write(new_output_file name)`.  This will allow for saving the output in a file name and type as desired.`` </li>


