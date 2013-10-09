<script >
$(function () {
	var total = 0; 
    $.get('{{content.data_json}}', function (json_data) {
         $('#{{content.id}}').highcharts(
         {
         chart: {
                type:'pie',
             plotBackgroundColor: null,
             plotBorderWidth: null,
             plotShadow: false,
			events: {
			    load: function(event) {
			      $('.highcharts-legend-item').last().children("span").append('<div style="width:140px; margin-top:30px;"><span style="float:left; width:70px "> Total </span><span style="float:right"> ' + total + '</span> </div>')
			    }
			  }
         },
         credits:{enabled: false},
         title: {
             text: '{{content.description}}'
         },
         tooltip: {
             pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
         },
         plotOptions: {
             pie: {
                 allowPointSelect: true,
                 cursor: 'pointer',
                 showInLegend: true,
             }
         },
		 legend: {
                enabled: true,
                layout: 'vertical',
                align: 'right',
                width: 160,
                verticalAlign: 'middle',
                borderWidth: 0,
       			useHTML: true,
	            itemStyle: {
	                paddingBottom: '10px'
	            },
                labelFormatter: function() {
                	total = total + this.y;
                    return '<div style="width:140px; "><span>' + this.name + '</span></div><div style="width:140px;"><span style="float:left; margin-left:20px;">' + Math.round(this.percentage) +'%</span><span style="float:right">' + this.y + '</span></div>';
				}
            },
            
         series: [{
             type: 'pie',
             name: '{{content.title}}',
             data: json_data,
         }]
         
         });
    });
});
</script >