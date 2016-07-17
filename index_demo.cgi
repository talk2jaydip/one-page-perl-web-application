#!/usr/bin/perl
use strict;

use CGI;
use DBI;
my $v = undef;
$v = CGI->new();
print $v->header();
 
 
sub load_page {
    
    print_html();
}



sub print_html {
    
    if ($v->param('action')){
        &Getresultdata();
    }
    else{
        if(defined $v->param('submit') && $v->param('submit') == 1){
            
            &InsertData();
        }
        
        &html_header();
        &html_content();
        &html_footer();
    }
    
    
}

sub html_header {
    
    print qq{
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html>
            <head>
                <title>Perl-CGI Demo</title>
                <link rel="stylesheet" type="text/css" href="../demo.css" />
                <script src="../jquery-3.1.0.min.js" type="text/javascript"></script>
                
                <script src="../index_demo.js" type="text/javascript"></script>
            </head>
            <body>
                
                <div class="container"><h1>welcome to CGI Demo</h1> <br><br>
    };
    
}

sub html_content {
    
    print qq{
        <form name="demo_form" id="demo_form_id" action="#" method="post" >
        <input type="button" id="new_button" name="nbutton" value="New">
        <input type="submit" id="add_button" name="sbutton" value="Add" style="display:none;"> 
        &nbsp;  <input type="button" value="Cancel" style="display:none;" id='cancel'></input>
            
            </br></br>
            <div id="add_form" style="display:none;">
                
                </br>
                Date: &nbsp;&nbsp; <input type="text" name="date" id="date"></input></br>
                Time:  &nbsp;&nbsp;  <input type="text" name="time" id="time"></input></br>
                Description:    <input type="text" name="desc" id="desc"></input></br>
                </br>
            </div>
        </form>
    };
    
    print qq{
        <input type="text" name="search" id="search_string" ></input> <input type="button" id="search_result" value="Search">
    
    };
    
    &Getresultdata();
}

sub Getresultdata {
    
    my ($result) = &GetAppointmentDetais();
    
    print qq{ </br> <div class="left-div" id="search_result_div">$result</div>};
}

sub GetAppointmentDetais {
    
    my $dbh = &GetDbHandeler();
    my $get_details_sql = qq{select Date,Time,Description from APPOINTMENTS };
    

    
    if($v->param('string')){
        my $search_string = $v->param('string');
        $get_details_sql .= qq{where Description like '%$search_string%' };
    }
    
    my $statement = $dbh->prepare($get_details_sql);
    $statement->execute;
    my $result = 0;
    my $response = qq{
       
        <table>
        <tr>
            <th>Date</th>
            <th>time</th>
            <th>Description</th>
        </tr>
    };
    while(my ($date,$time,$description) =  $statement->fetchrow){
        
        if ($date != '' || $time != '' || $description != ''){
            $response .= qq{
                <tr>
                    <td>$date</td>
                    <td>$time</td>
                    <td>$description</td>
                </tr> 
            };
            $result = 1;
        }
    }
    
    $response .= qq{
        </table>
        
    };
    $response = '' if !$result;
    
    return $response
    
    ;
}

sub InsertData {
    my $dbh = &GetDbHandeler();
    my $insert_sql = qq{
        INSERT INTO APPOINTMENTS (
            Description,Date,Time
        )
        values(
            ?,?,?
        )
    };
    
    my $desc = $v->param('desc') || '';
    my $date = $v->param('date') || '';
    my $time = $v->param('time') || '';
    
    $dbh->do($insert_sql, undef,$desc,$date,$time);
}
    

sub GetDbHandeler{
    
     my $dbh = DBI->connect("DBI:mysql:cgi_demo", 'root', 'root', { PrintError => 1 });
     return $dbh;
}

sub html_footer {
    
    print qq{
    </div>
            </body>
        </html>
        
        
    };
}


&load_page();