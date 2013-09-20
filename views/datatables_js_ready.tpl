<script >
        var asInitVals_{{ content.id_table }} = new Array();
        $(document).ready(function() {
    		var oTable_{{ content.id_table }} = $('#{{ content.id_table }}').dataTable( {
    	        "sDom": "{{!content.get_sDom_string() }}",
    	        "sAjaxSource": "{{content.ajax_url}}",
    			"sPaginationType": "bootstrap",
    	        "iDisplayLength": {{content.records_per_page}},
    	        "aLengthMenu": {{!str(content.drop_down_values)}},
    	        {{!content.row_callback}}
    			"oLanguage": {
    				"sLengthMenu": "_MENU_ {{content.drop_down_text}}",
    	            "sSearch": "{{content.global_search_text}}",
    	            "sInfo": "Got a total of _TOTAL_ entries to show (_START_ to _END_) <a target='_blank' href='{{content.csv_url}}' class='pull-right'><span class='glyphicon glyphicon-download'></span> Download CSV </a>"
    			}
		} );
	
	    %if content.column_search:
		$("#foot_{{ content.id_table }} input").keyup( function () {
			oTable_{{ content.id_table }}.fnFilter( this.value, $("#foot_{{ content.id_table }} input").index(this) );
		} );
		$("#foot_{{ content.id_table }} input").each( function (i) {
			asInitVals_{{ content.id_table }}[i] = this.value;
		} );
		$("#foot_{{ content.id_table }} input").focus( function () {
			if ( this.className == "search_init" )
			{
				this.className = "form-control input-small";
				this.value = "";
			}
		} );
		$("#foot_{{ content.id_table }} input").blur( function (i) {
			if ( this.value == "" )
			{
				this.className = "search_init form-control input-small";
				this.value = asInitVals_{{ content.id_table }}[$("#foot_{{ content.id_table }} input").index(this)];
			}
		} );
        var search_input = oTable_{{ content.id_table }}.closest('.dataTables_wrapper').find('div[id$=_filter] input');
        search_input.attr('placeholder', 'Search');
        search_input.addClass('form-control input-small');
        search_input.css('width', '250px');
 
        // SEARCH CLEAR - Use an Icon
        var clear_input = oTable_{{ content.id_table }}.closest('.dataTables_wrapper').find('div[id$=_filter] a');
        clear_input.html('<i class="icon-remove-circle icon-large"></i>');
        clear_input.css('margin-left', '5px');
 
        // LENGTH - Inline-Form control
        var length_sel = oTable_{{ content.id_table }}.closest('.dataTables_wrapper').find('div[id$=_length] select');
        length_sel.addClass('form-control input-small');
        length_sel.css('width', '75px');
 
        // LENGTH - Info adjust location
        var length_sel = oTable_{{ content.id_table }}.closest('.dataTables_wrapper').find('div[id$=_info]');
        length_sel.css('margin-left', '15px');
        });
</script>
