$(document).ready(function(){
    $("#new_button").click(function(e){
        //$("#new_button").attr('value', 'Add');
        //$("#new_button").attr('id', 'form_submit');
        $("#new_button").css({'display':'none'});
        $('#add_button').css({'display':'inline'});
        $('#cancel').css({'display':'inline'});
        $("#add_form").css({'display':'inline'});
        //$('input[name="nbutton"]').attr("type", "submit");
         e.preventDefault();
         
    });
    
    $("#demo_form_id").submit( function() {
      $('<input />').attr('type', 'hidden')
          .attr('name', "submit")
          .attr('value', "1")
          .appendTo('#demo_form_id');
      return true;
  });
    
    
    
    
    $("#cancel").click(function(){
        //$("#form_submit").attr('value', 'New');
        $("#new_button").css({'display':'inline'});
        $("#add_button").css({'display':'none'});
        //$("#new_button").attr('type', 'button');
        $("#add_form").css({'display':'none'});
        $('#cancel').css({'display':'none'});
        
    });
    
    $('#search_result').click(function(){
        getAppointments(); 
    });
    
    function getAppointments (){    
        $('#search_result_div').html('');
        $.ajax({
			url: 'index_demo.cgi',
			type: 'POST',
			data: {
			    'action'  : 'search',
			    'string'  : $('#search_string').val() || '',
			},
            success: function(data) {
                if(data){
                    
                    $('#search_result_div').html(data);
                    
                }
               
            }
        });
    }
    
    
    
    
    
});
